'''
Definition of Location:
class Location:
    # @param {double} latitude, longitude
    # @param {Location}
    @classmethod
    def create(cls, latitude, longitude):
        # This will create a new location object

Definition of Restaurant:
class Restaurant:
    # @param {str} name
    # @param {Location} location
    # @return {Restaurant}
    @classmethod
    def create(cls, name, location):
        # This will create a new restaurant object,
        # and auto fill id

Definition of Helper
class Helper:
    # @param {Location} location1, location2
    @classmethod
    def get_distance(cls, location1, location2):
        # return calculate the distance between two location

Definition of GeoHash
class GeoHash:
    # @param {Location} location
    # @return a string
    @classmethom
    def encode(cls, location):
        # return convert location to a geohash string

    # @param {str} hashcode
    # @return {Location}
    @classmethod
    def decode(cls, hashcode):
        # return convert a geohash string to location
'''
from YelpHelper import Location, Restaurant, GeoHash, Helper
import heapq

class MiniYelp:

    def __init__(self):
        # initialize your data structure here.
        self.restaurants = {} #restaurant_id, restaurant
        self.restaurant_name_2_id = {} #name, restaurant_id
        self.restaurants_2_geolocation_prefix = {} #keep tracks of geo location prefixes of restaurants, easier to delte later
        self.geo_location_table = {} #redis 分级存储, key=geocode, 4位， 5位， 6位, val= restaurant_id
        self.geohashing_precision = [2500, 630, 78, 20, 2.4, 0.61, 0.076, 0.019] #for prefix 1 - 8 geohashing precision


    # @param {str} name
    # @param {Location} location
    # @return {int} restaurant's id
    def add_restaurant(self, name, location):
        # Write your code here
        if name in self.restaurant_name_2_id:
            return self.restaurant_name_2_id[name]
        new_restaurant = Restaurant.create(name, location)
        self.restaurants[new_restaurant.id] = new_restaurant
        self.restaurant_name_2_id[name] = new_restaurant.id
        self.create_geo_location_item(location, new_restaurant.id)
        return new_restaurant.id

    """
    for each new restaurant, generate a geolocation prefix of length 1 - 8 and put them in the geo_location_table.
    it's value is the restaurant_id
    @param: location, restaurant_id
    @return: None
    """
    def create_geo_location_item(self, location, restaurant_id):
        geohash_string = GeoHash.encode(location)
        for i in range(1, 9): #calulate geohash prefix 1-8
            prefix = geohash_string[0:i]
            if prefix not in self.geo_location_table:
                self.geo_location_table[prefix] = set()
            self.geo_location_table[prefix].add(restaurant_id)
            if restaurant_id not in self.restaurants_2_geolocation_prefix:
                self.restaurants_2_geolocation_prefix[restaurant_id] = set()
            self.restaurants_2_geolocation_prefix[restaurant_id].add(prefix)

    """
    using nearest geolocation to find restaurant
    """
    def find_neighbors_by_gelocation(self, location, k):
        geohash_string = GeoHash.encode(location)
        prefix_index_to_search = self.binary_search(0, 7, self.geohashing_precision, k) #find the next largest number
        if prefix_index_to_search == -1:
            #that means the distance required is larger than the maximum precision, has to search the entire table, this should rarely happen
            return self.search_all_restaurants_for_nearest(location, k)
        if geohash_string[0:prefix_index_to_search + 1] in self.geo_location_table:
            return self.search_loc_list(geohash_string[0:prefix_index_to_search + 1], location, k)
        return []

    """
    find the next largest number in geocashing error precision table.
    we only have to serach from k to next largest error.
    example k = 6.8km, we only need to search in error range <= 20km. which is a geohashing prefix with 4 charcters
    @param: start, end, nums, target
    @return: next bigger index in prefix error table
    """
    def binary_search(self, start, end, nums, target):
        while start + 1 < end:
            mid =  (start + end) // 2
            if nums[mid] < target:
                end = mid
            else:
                start = mid
        if nums[end] > target:
            return end
        if nums[start] > target:
            return start
        return -1

    """
    if k > lowest precision (2500km) in the geohashing algorithm, that means all restaurants need to be searched.
    this should rarely happen
    """
    def search_all_restaurants_for_nearest(self, location, k):
        result = [] #(dist, restaurant name)
        for restaurant_id, restaurant in self.restaurants.items():
            curr_dist = Helper.get_distance(restaurant.location, location)
            if curr_dist < k:
                result.append((curr_dist, restaurant.name))
        result.sort()
        return [restaurant[1] for restaurant in result]

    """
    search only 1 prefix for a location which distance < k
    this simulate a single db on a single machine.
    @param: prefix: geohashing prefix
    @param: location, k
    @return: a list of restaurant names
    """
    def search_loc_list(self, prefix, location, k):
        heap = []
        result = []
        for restaurant_id in self.geo_location_table[prefix]:
            curr_dist = Helper.get_distance(self.restaurants[restaurant_id].location, location)
            if curr_dist < k:
                heapq.heappush(heap, (curr_dist, self.restaurants[restaurant_id].name))
        while heap:
            result.append(heapq.heappop(heap)[1])
        return result

    # @param {int} restaurant_id
    # @return nothing
    def remove_restaurant(self, restaurant_id):
        # Write your code here
        if restaurant_id in self.restaurants:
            restaurant = self.restaurants[restaurant_id]
            del self.restaurant_name_2_id[restaurant.name]
            for prefix in self.restaurants_2_geolocation_prefix[restaurant_id]:
                self.geo_location_table[prefix].remove(restaurant_id)
            del self.restaurants_2_geolocation_prefix[restaurant_id]
            del self.restaurants[restaurant_id]


    # @param {Location} location
    # @param {double} k, distance smaller than k miles
    # @return {str[]} a list of restaurant's name and sort by
    # distance from near to far.
    def neighbors(self, location, k):
        # Write your code here
        return self.find_neighbors_by_gelocation(location, k)
