from Models.TripStatus import TripStatus


class Trip(object):
    def __init__(self, trip_id, booking, start_time, end_time):
        self.trip_id = trip_id
        self.booking = booking
        self.start_time = start_time
        self.end_time = end_time
        self.status = TripStatus.ACTIVE

    def update_end_time(self, time):
        self.end_time = time

    def update_trip_status(self, status):
        self.status = status
