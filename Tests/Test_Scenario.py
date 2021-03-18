# Testing for concurrency by threading implementation. # threads should call the same task simulatneously
import concurrent
from unittest import TestCase

from API.BookingController import BookingController
from API.CabController import CabController
from Services.BookingService import booking_service
from Services.CabService import cab_service
from Services.RiderService import rider_service
from concurrent import futures
import threading
from threading import Thread

from Services.TripService import trip_service


class TestConcurrency(TestCase):
    def setUp(self) -> None:
        self.booking_controller = BookingController()
        self.cab_controller = CabController()
        self.rider_service = rider_service
        self.booking_service = booking_service
        self.cab_service = cab_service
        self.trip_service = trip_service

        self.first_rider = self.rider_service.createRider("Shreyas", 1, 1)
        self.second_rider = self.rider_service.createRider("Ashwin", 0, 0)
        self.third_rider = self.rider_service.createRider("Aditya", 3, 3)

        self.first_rider_destination_x = 5
        self.first_rider_destination_y = 5

        self.second_rider_destination_x = 4
        self.second_rider_destination_y = 4

        self.third_rider_destination_x = 6
        self.third_rider_destination_y = 6

        self.first_driver = self.cab_controller.create_driver("Amit")
        self.second_driver = self.cab_controller.create_driver("Sudeep")
        # self.third_driver = self.cab_controller.create_driver("Sumit")

        self.first_cab_id = self.cab_controller.create_cab(self.first_driver, -3, -3)
        self.second_cab_id = self.cab_controller.create_cab(self.second_driver, 0, 0)
        # self.third_cab_id = self.cab_controller.create_cab(self.third_driver, -2, -2)

    def test_book_my_cab_concurrency(self):
        # import ipdb
        # ipdb.set_trace()

        # with concurrent.futures.ThreadPoolExecutor() as executor:
        #     parameters = [(self.first_rider, self.first_rider_destination_x, self.first_rider_destination_y),
        #                   (self.second_rider, self.second_rider_destination_x, self.second_rider_destination_y),
        #                   (self.third_rider, self.third_rider_destination_x, self.third_rider_destination_y)]
        #
        #     results = [executor.map(self.booking_controller.book_my_cab, param) for param in parameters]
        #
        #     for res in results:
        #         print(next(res))
        lock = threading.Lock()
        with lock:

            first_thread = Thread(target=self.booking_controller.book_my_cab,
                                  args=(lock, self.first_rider,
                                        self.first_rider_destination_x,
                                        self.first_rider_destination_y))
            second_thread = Thread(target=self.booking_controller.book_my_cab,
                                   args=(lock, self.second_rider,
                                         self.second_rider_destination_x,
                                         self.second_rider_destination_x))
            third_thread = Thread(target=self.booking_controller.book_my_cab,
                                  args=(lock, self.third_rider,
                                        self.third_rider_destination_x,
                                        self.third_rider_destination_y))

            first_thread.start()
            second_thread.start()
            third_thread.start()
            first_thread.join()
            second_thread.join()
            third_thread.join()

    # def tearDown(self) -> None:
    #     self.booking_service.all_bookings.clear()
    #     self.trip_service.all_trips.clear()
    #     self.cab_service.all_cabs.clear()
    #     self.cab_service.all_vehicles.clear()
    #     self.cab_service.all_vehicles.clear()

