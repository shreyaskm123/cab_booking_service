from Services.CabService import cab_service


class CabController(object):
    def __init__(self):
        self.cab_service = cab_service

    def create_driver(self, driver_name):
        """
        This creates driver object for a particular driver name
        :param driver_name:
        :return: driver_id
        """
        return self.cab_service.createDriver(driver_name)

    def update_driver_availability(self, driver_id, availability_status):
        """
        This updates the status of the driver.
        :param driver_id:
        :param availability_status:
        :return:
        """
        return self.cab_service.updateDriverAvailability(driver_id, availability_status)

    def create_cab(self, driver_id, location_x, location_y):
        """
        This creates an Cab object and maps a driver for a particular cab and update the location of all of them.
        :param driver_id:
        :param location_x:
        :param location_y:
        :return:
        """
        driver = self.cab_service.getDriver(driver_id)
        return self.cab_service.createCab(driver, location_x, location_y)

    def update_cab_availability(self, cab_id, availability_status):
        """
        This updates the cab availability status
        :param cab_id:
        :param availability_status:
        :return:
        """
        return self.cab_service.updateCabAvailability(cab_id, availability_status)
