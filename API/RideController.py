from Services.BookingService import booking_service
from Services.RiderService import rider_service


class RideController(object):
    def __init__(self):
        self.rider_service = rider_service
        self.booking_service = booking_service

    def create_rider(self, rider_name, rider_location_x, rider_location_y):
        """
        This creates a rider object with a rider name and updates the rider current location
        :param rider_name:
        :param rider_location_x:
        :param rider_location_y:
        :return: rider_id
        """
        return self.rider_service.createRider(rider_name, rider_location_x, rider_location_y)

    def update_rider_location(self, rider_id, new_location_x, new_location_y):
        """
        This updates the rider location to a new location of x and y
        :param rider_id:
        :param new_location_x:
        :param new_location_y:
        :return: rider_id
        """
        rider = self.rider_service.getRider(rider_id)
        self.rider_service.updateRiderLocation(rider, new_location_x, new_location_y)

    def get_rider_history(self, rider_id):
        """
        Returns the list of booking ID's for a particular rider. This includes all the cancelled and successful bookings
        made by a rider
        :param rider_id:
        :return:
        """

        rider = self.rider_service.getRider(rider_id)
        return self.rider_service.getRiderHistory(rider)

    def update_rider_history(self, rider_id, booking_id):
        """
        This updates the rider history by appending all the additional booking the rider has made.
        :param rider_id:
        :param booking_id:
        :return: rider_id
        """
        rider = self.rider_service.getRider(rider_id)
        booking = self.booking_service.getBooking(booking_id)
        return self.rider_service.updateRiderHistory(rider, booking)
