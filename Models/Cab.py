from Models.CabStatus import CabStatus


class Cab(object):
    def __init__(self, cab_id, driver, vehicle, location):
        self.cab_id = cab_id
        self.driver = driver
        self.vehicle = vehicle
        self.location = location
        self.status = CabStatus.AVAILABLE

    def update_status(self, status):
        self.status = status
