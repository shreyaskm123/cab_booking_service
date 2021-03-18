from API.CabController import CabController
from Helpers import get_unique_identifier, get_fair_estimate
from Models.Booking import Booking
from Models.BookingStatus import BookingStatus
from Models.CabStatus import CabStatus
from Models.Location import Location


class BookingService(object):
    def __init__(self):
        self.all_bookings = dict()
        self.cab_controller = CabController()

    def createBooking(self, rider, cab, destination_location_x, destination_location_y):
        booking_id = get_unique_identifier()
        fare_estimate = get_fair_estimate
        destination_location = Location(get_unique_identifier(), destination_location_x, destination_location_y)
        my_booking = Booking(booking_id, cab, rider, fare_estimate, destination_location)
        self.all_bookings[booking_id] = my_booking
        return booking_id

    def getBooking(self, booking_id):

        try:
            return self.all_bookings[booking_id]
        except:
            print('Invalid Booking ID')

    def confirmBooking(self, booking_id):
        booking = self.getBooking(booking_id)
        booking.update_booking_status(BookingStatus.CONFIRMED)
        cab_id = booking.cab.cab_id
        self.cab_controller.update_cab_availability(cab_id, CabStatus.BOOKED)

    def cancelBooking(self, booking_id):
        booking = self.getBooking(booking_id)
        booking.update_booking_status(BookingStatus.CANCELLED)
        cab_id = booking.cab.cab_id
        self.cab_controller.update_cab_availability(cab_id, CabStatus.AVAILABLE)


booking_service = BookingService()
