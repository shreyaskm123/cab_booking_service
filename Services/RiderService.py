from Helpers import get_unique_identifier
from Models.Location import Location
from Models.Rider import Rider


class RiderService(object):
    def __init__(self):
        self.all_riders = dict()

    def createRider(self, rider_name, rider_location_x, rider_location_y):

        rider_id = get_unique_identifier()
        location = Location(get_unique_identifier(), rider_location_x, rider_location_y)
        my_rider = Rider(rider_id, rider_name, location)
        self.all_riders[rider_id] = my_rider
        return rider_id

    def getRider(self, rider_id):
        return self.all_riders[rider_id]

    def updateRiderLocation(self, rider, new_location_x, new_location_y):
        rider_current_location = rider.location
        rider_current_location.update_location(new_location_x, new_location_y)

    def getRiderHistory(self, rider):
        return rider.rider_history

    def updateRiderHistory(self, rider, booking):
        rider.rider_history.append(booking)


rider_service = RiderService()

