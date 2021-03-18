from API.RideController import RideController
from Services.BookingService import booking_service
from Services.CabService import cab_service
from Services.RiderService import rider_service
import threading


class BookingController(object):
    def __init__(self):
        self.booking_service = booking_service
        self.cab_service = cab_service
        self.rider_service = rider_service
        self.rider_controller = RideController()

    def book_my_cab(self, lock, rider_id, destination_location_x, destination_location_y):
        """
        This should create a booking object for a particular rider and also update the rider's history.
        Based on the current location of the rider , it get's the nearest cab available with in the range.
        :param rider_id: rider ID
        :param destination_location_x: X-Co-ordinate of the destination
        :param destination_location_y: Y- Co-ordinate of the destination
        :return: booing_id
        """

        rider = self.rider_service.getRider(rider_id)
        rider_location_x = rider.get_rider_x_location()
        rider_location_y = rider.get_rider_y_location()
        cab = self.cab_service.get_nearest_cab(rider_location_x, rider_location_y)

        if cab is not None:
            booking_id = self.booking_service.createBooking(rider, cab, destination_location_x, destination_location_y)
            self.rider_controller.update_rider_history(rider_id, booking_id)
            booking = self.booking_service.getBooking(booking_id)
            print(booking.cab.driver.driver_name)
            print(booking.rider.rider_name)
            self.confirm_booking(booking_id)

        else:
            print("No cabs available in your location")

    def confirm_booking(self, booking_id):
        """
        For a particular booking it confirms by changing the status of the booking.
        Also, updates the cab availability status to booked.
        :param booking_id:
        :return:
        """
        return self.booking_service.confirmBooking(booking_id)

    def cancel_booking(self, booking_id):
        """
        This should update booking status and also update the cab availability status.
        :param booking_id:
        :return:
        """
        return self.booking_service.cancelBooking(booking_id)
