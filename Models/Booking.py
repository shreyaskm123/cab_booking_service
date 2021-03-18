from datetime import datetime

from Models.BookingStatus import BookingStatus


class Booking(object):
    def __init__(self, booking_id, cab, rider, fare_estimate, destination_location):
        self.booking_id = booking_id
        self.cab = cab
        self.rider = rider
        self.fare_estimate = fare_estimate
        self.created_time = datetime.now()
        self.destination_location = destination_location
        self.booking_status = BookingStatus.CREATED

    def update_booking_status(self, status):
        self.booking_status = status
