from datetime import datetime

from Helpers import get_unique_identifier
from Models.CabStatus import CabStatus
from Models.Trip import Trip
from Models.TripStatus import TripStatus


class TripService(object):
    def __init__(self):
        self.all_trips = dict()

    def startTrip(self, booking):
        trip_id = get_unique_identifier()
        start_time = datetime.now()
        my_trip = Trip(trip_id, booking, start_time, None)
        self.all_trips[trip_id] = my_trip
        return trip_id

    def getTrip(self, trip_id):
        return self.all_trips[trip_id]

    def endTrip(self, trip):
        current_time = datetime.now()
        trip.update_end_time(current_time)
        status = TripStatus.INACTIVE
        trip.update_trip_status(status)

        booking = trip.booking
        booking.cab.location.update_location(booking.destination_location.get_x_location(),
                                             booking.destination_location.get_y_location())

        booking.cab.update_status(CabStatus.AVAILABLE)

        booking.rider.location.update_location(booking.destination_location.get_x_location(),
                                               booking.destination_location.get_y_location())


trip_service = TripService()

