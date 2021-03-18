class Location(object):
    def __init__(self, location_id, x_cordinate, y_cordinate):
        self.location_id = location_id
        self.x_cordinate = x_cordinate
        self.y_cordinate = y_cordinate

    def update_location(self, new_x_cordinate, new_y_cordinate):
        self.x_cordinate = new_x_cordinate
        self.y_cordinate = new_y_cordinate

    def get_x_location(self):
        return self.x_cordinate

    def get_y_location(self):
        return self.y_cordinate
