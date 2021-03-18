import unittest
from unittest import TestCase

from API.CabController import CabController
from Models.CabStatus import CabStatus
from Models.DriverStatus import DriverStatus
from Services.CabService import cab_service


class TestCabController(TestCase):
    def setUp(self) -> None:
        self.cab_controller = CabController()
        self.cab_service = cab_service

    def test_create_driver(self):

        driver_name = "Shreyas"
        driver_id = self.cab_controller.create_driver(driver_name)

        my_driver = self.cab_service.getDriver(driver_id)
        self.assertEqual(my_driver.driver_id, driver_id)
        self.assertEqual(my_driver.driver_name, driver_name)

    def update_driver_availability(self):
        driver_id = self.cab_controller.create_driver("ABC")

        self.cab_controller.update_driver_availability(driver_id, DriverStatus.AVAILABLE)
        driver = self.cab_service.getDriver(driver_id)
        self.assertEqual(driver.driver_status, DriverStatus.AVAILABLE)

        self.cab_controller.update_driver_availability(driver_id, DriverStatus.UNAVAILABLE)
        driver = self.cab_service.getDriver(driver_id)
        self.assertEqual(driver.driver_status, DriverStatus.UNAVAILABLE)

    def test_create_cab(self):

        driver_id = self.cab_controller.create_driver("Random_name")
        cab_id = self.cab_controller.create_cab(driver_id, 0, 0)
        my_cab = self.cab_service.getCab(cab_id)

        self.assertEqual(cab_id, my_cab.cab_id)
        self.assertEqual(my_cab.location.get_x_location(), 0)
        self.assertEqual(my_cab.location.get_y_location(), 0)

    def test_update_cab_availability(self):

        driver_id = self.cab_controller.create_driver("My_Driver")
        cab_id = self.cab_controller.create_cab(driver_id, 3, 3)
        my_cab = self.cab_service.getCab(cab_id)

        self.cab_controller.update_cab_availability(cab_id, CabStatus.UNAVAILABLE)
        self.assertEqual(my_cab.status, CabStatus.UNAVAILABLE)

        self.cab_controller.update_cab_availability(cab_id, CabStatus.BOOKED)
        self.assertEqual(my_cab.status, CabStatus.BOOKED)


if __name__ == 'main':
    unittest.main()

