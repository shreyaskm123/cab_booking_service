from Services.BookingService import booking_service
from Services.TripService import trip_service


class TripController(object):
    def __init__(self):
        self.trip_service = trip_service
        self.booking_service = booking_service

    def start_my_trip(self, booking_id):
        """
        Creates a trip object by mapping a booking_id. Should also update cab's location to rider's current location
        :param booking_id:
        :return: trip_id
        """
        booking = self.booking_service.getBooking(booking_id)

        return self.trip_service.startTrip(booking)

    def end_my_trip(self, trip_id):
        """
        This should update rider's and cab's current location to destination location of the rider.
        It also updates the status of the trip and cab.
        :param trip_id:
        :return: trip_id
        """
        trip = self.trip_service.getTrip(trip_id)
        return self.trip_service.endTrip(trip)

    def get_my_trip(self, trip_id):
        """
        Returns the trip object corresponding to a particular trip_id
        :param trip_id:
        :return:
        """
        return self.trip_service.getTrip(trip_id)
