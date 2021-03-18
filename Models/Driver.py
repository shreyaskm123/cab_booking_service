from Models.DriverStatus import DriverStatus


class Driver(object):
    def __init__(self, driver_id, driver_name):
        self.driver_id = driver_id
        self.driver_name = driver_name
        self.driver_status = DriverStatus.AVAILABLE

    def update_status(self, status):
        self.driver_status = status
