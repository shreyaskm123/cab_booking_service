class Rider(object):
    def __init__(self, rider_id, rider_name, location):
        self.rider_id = rider_id
        self.rider_name = rider_name
        self.location = location
        self.rider_history = list()  # List of booking ID's

    def get_rider_x_location(self):
        return self.location.get_x_location()

    def get_rider_y_location(self):
        return self.location.get_y_location()
