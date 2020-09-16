'''
Definition of Trip:
class Trip:
    self.id; # trip's id, primary key
    self.driver_id, self.rider_id; # foreign key
    self.lat, self.lng; # pick up location
    def __init__(self, rider_id, lat, lng):

Definition of Helper
class Helper:
    @classmethod
    def get_distance(cls, lat1, lng1, lat2, lng2):
        # return calculate the distance between (lat1, lng1) and (lat2, lng2)
'''
from Trip import Trip, Helper


class Driver:
    def __init__(self, driver_id):
        self.driver_id = driver_id
        self.status = 0
        self.lat = None
        self.lng = None
        self.trip_id = None

    def update_loc(self, lat, lng):
        self.lat = lat
        self.lng = lng

    def mark_available(self):
        self.status = 0

    def mark_unavailable(self, trip_id):
        self.status = 1
        self.trip_id = trip_id

    def is_available(self):
        if self.status == 0:
            return True
        else:
            return False

    def get_tripid(self):
        return self.trip_id

    def get_location(self):
        return (self.lat, self.lng)

class MiniUber:

    def __init__(self):
        # initialize your data structure here.
        self.drivers = {} #a map of drivers, driver_id:Driver
        self.trips = {} #a map of trips, trip_id: Trip

    # @param {int} driver_id an integer
    # @param {double} lat, lng driver's location
    # return {trip} matched trip information if there have matched rider or null
    def report(self, driver_id, lat, lng):
        # Write your code here
        if driver_id not in  self.drivers:
            self.drivers[driver_id] = Driver(driver_id)
        driver = self.drivers[driver_id]
        driver.update_loc(lat, lng)
        if not driver.is_available():
            trip_id = driver.get_tripid()
            return self.trips[trip_id]
        return None



    # @param rider_id an integer
    # @param lat, lng rider's location
    # return a trip
    def request(self, rider_id, lat, lng):
        # Write your code here
        new_trip = Trip(rider_id, lat, lng)
        min_distance_driver_id, min_distance = None, sys.maxsize
        for driver_id, driver in self.drivers.items():
            if not driver.is_available():
                continue
            driver_lat, driver_lng = driver.get_location()
            curr_distance = Helper.get_distance(driver_lat, driver_lng, lat, lng)
            if curr_distance < min_distance:
                min_distance_driver_id = driver_id
                min_distance = curr_distance
        #unable to find a driver
        if min_distance_driver_id == None:
            return None
        new_trip.driver_id = min_distance_driver_id
        self.trips[new_trip.id] = new_trip
        self.drivers[min_distance_driver_id].mark_unavailable(new_trip.id)
        return new_trip
