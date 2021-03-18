import unittest
from unittest import TestCase

from API.BookingController import BookingController
from API.CabController import CabController
from API.RideController import RideController
from Services.CabService import cab_service
from Services.RiderService import rider_service


class TestRideController(TestCase):
    def setUp(self) -> None:
        self.ride_controller = RideController()
        self.rider_service = rider_service
        self.booking_controller = BookingController()
        self.cab_controller = CabController()
        self.cab_service = cab_service

        self.driver_id = self.cab_controller.create_driver("Random_name")
        self.cab_id = self.cab_controller.create_cab(self.driver_id, 0, 0)
        self.my_cab = self.cab_service.getCab(self.cab_id)

    def test_create_rider(self):

        rider_id = self.ride_controller.create_rider("Rahul", 2, 3)
        my_rider = self.rider_service.getRider(rider_id)

        self.assertEqual(my_rider.rider_id, rider_id)
        self.assertEqual(my_rider.rider_name, "Rahul")
        self.assertEqual(my_rider.location.get_x_location(), 2)
        self.assertEqual(my_rider.location.get_y_location(), 3)

    def test_update_rider_location(self):
        rider_id = self.ride_controller.create_rider("Amit", 4, 5)
        my_rider = self.rider_service.getRider(rider_id)

        self.assertEqual(my_rider.rider_name, "Amit")
        self.assertEqual(my_rider.location.get_x_location(), 4)
        self.assertEqual(my_rider.location.get_y_location(), 5)

        self.ride_controller.update_rider_location(rider_id, 5, 5)
        self.assertEqual(my_rider.location.get_x_location(), 5)
        self.assertEqual(my_rider.location.get_y_location(), 5)

    def test_get_and_update_rider_history(self):

        rider_id = self.ride_controller.create_rider("Ashish", 1, 2)
        my_rider = self.rider_service.getRider(rider_id)

        booking_id = self.booking_controller.book_my_cab(rider_id, 0, 0)
        rider_history = self.ride_controller.get_rider_history(rider_id)

        self.assertEqual(rider_history[0].booking_id, booking_id)


if __name__ == "main":
    unittest.main()

