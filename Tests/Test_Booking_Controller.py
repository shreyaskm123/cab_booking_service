import unittest
from unittest import TestCase

from API.BookingController import BookingController
from API.CabController import CabController
from Models.BookingStatus import BookingStatus
from Models.CabStatus import CabStatus
from Services.BookingService import booking_service
from Services.RiderService import rider_service


class TestBookingController(TestCase):
    def setUp(self) -> None:
        self.booking_controller = BookingController()
        self.rider_service = rider_service
        self.cab_controller = CabController()
        self.booking_service = booking_service

        # Create Cabs at multiple locations
        self.driver_1_id = self.cab_controller.create_driver("Ashwin")
        self.cab_1_id = self.cab_controller.create_cab(self.driver_1_id, 0, -2)

        self.driver_2_id = self.cab_controller.create_driver("Sayak")
        self.cab_2_id = self.cab_controller.create_cab(self.driver_2_id, -2, -2)

        self.driver_3_id = self.cab_controller.create_driver("Sudeep")
        self.cab_3_id = self.cab_controller.create_cab(self.driver_3_id, 4, 4)

    def test_book_my_cab(self):

        rider_id = rider_service.createRider("Aditya", -1, -1)
        my_rider = rider_service.getRider(rider_id)

        booking_id = self.booking_controller.book_my_cab(rider_id, 3, 3)
        my_booking = self.booking_service.getBooking(booking_id)

        self.assertEqual(booking_id, my_booking.booking_id)
        self.assertEqual(rider_id, my_booking.rider.rider_id)
        self.assertEqual("Aditya", my_booking.rider.rider_name)
        self.assertEqual(self.driver_1_id, my_booking.cab.driver.driver_id)
        self.assertEqual("Ashwin", my_booking.cab.driver.driver_name)

        self.assertEqual(my_booking.rider.location.get_x_location(), my_rider.location.get_x_location())
        self.assertEqual(my_booking.rider.location.get_y_location(), my_rider.location.get_y_location())

    def test_confirm_booking(self):

        rider_id = rider_service.createRider("Nithish", 4, 3)
        my_rider = rider_service.getRider(rider_id)

        booking_id = self.booking_controller.book_my_cab(rider_id, 6, 6)
        my_booking = self.booking_service.getBooking(booking_id)

        self.assertEqual(my_booking.booking_status, BookingStatus.CREATED)

        self.booking_service.confirmBooking(booking_id)
        self.assertEqual(my_booking.booking_status, BookingStatus.CONFIRMED)
        self.assertEqual(my_booking.cab.status, CabStatus.BOOKED)

    def test_cancel_booking(self):
        rider_id = rider_service.createRider("Sharan", 0, 0)
        my_rider = rider_service.getRider(rider_id)

        booking_id = self.booking_controller.book_my_cab(rider_id, 1, 1)
        my_booking = self.booking_service.getBooking(booking_id)

        self.assertEqual(my_booking.booking_status, BookingStatus.CREATED)

        self.booking_service.cancelBooking(booking_id)
        self.assertEqual(my_booking.booking_status, BookingStatus.CANCELLED)
        self.assertEqual(my_booking.cab.status, CabStatus.AVAILABLE)


if __name__ == "main":
    unittest.main()
