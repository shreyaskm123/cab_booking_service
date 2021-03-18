import unittest
from unittest import TestCase

from API.BookingController import BookingController
from API.CabController import CabController
from API.TripController import TripController
from Models.TripStatus import TripStatus
from Services.BookingService import booking_service
from Services.RiderService import rider_service


class TestTripController(TestCase):
    def setUp(self) -> None:
        self.trip_controller = TripController()
        self.cab_controller = CabController()
        self.rider_service = rider_service
        self.booking_service = booking_service
        self.booking_controller = BookingController()

        self.driver_id = self.cab_controller.create_driver("Ashwin")
        self.cab_id = self.cab_controller.create_cab(self.driver_id, 3, 2)

        self.rider_id = self.rider_service.createRider("Aditya", 1, 1)
        self.my_rider = rider_service.getRider(self.rider_id)

        self.booking_id = self.booking_controller.book_my_cab(self.rider_id, 3, 3)
        self.my_booking = self.booking_service.getBooking(self.booking_id)

    def test_start_and_end_my_trip(self):
        booking_service.confirmBooking(self.booking_id)
        trip_id = self.trip_controller.start_my_trip(self.booking_id)
        my_trip = self.trip_controller.get_my_trip(trip_id)

        self.assertEqual(my_trip.trip_id, trip_id)
        self.assertEqual(my_trip.booking.booking_id, self.my_booking.booking_id)
        self.assertEqual(my_trip.status, TripStatus.ACTIVE)

        self.trip_controller.end_my_trip(trip_id)

        self.assertEqual(my_trip.status, TripStatus.INACTIVE)


if __name__ == "main":
    unittest.main()
