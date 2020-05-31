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


class MiniYelp:

    def __init__(self):
        # initialize your data structure here.
        self.restaurants = {} #restaurant_id, restaurant
        self.restaurant_name_2_id = {} #name, restaurant_id


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
        return new_restaurant.id




    # @param {int} restaurant_id
    # @return nothing
    def remove_restaurant(self, restaurant_id):
        # Write your code here
        if restaurant_id in self.restaurants:
            restaurant = self.restaurants[restaurant_id]
            del self.restaurant_name_2_id[restaurant.name]
            del self.restaurants[restaurant_id]



    # @param {Location} location
    # @param {double} k, distance smaller than k miles
    # @return {str[]} a list of restaurant's name and sort by
    # distance from near to far.
    def neighbors(self, location, k):
        # Write your code here
        all_neighbors = []
        for restaurant_id, restaurant in self.restaurants.items():
            curr_dist = Helper.get_distance(restaurant.location, location)
            if curr_dist < k:
                all_neighbors.append((curr_dist, restaurant.name))
        all_neighbors.sort()
        return [x[1] for x in all_neighbors]
