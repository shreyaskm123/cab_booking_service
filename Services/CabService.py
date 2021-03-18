import ENV_VAR
from Helpers import get_unique_identifier, get_cartesian_distance
from Models.Cab import Cab
from Models.CabStatus import CabStatus
from Models.Driver import Driver
from Models.Location import Location
from Models.Vehicle import Vehicle


class CabService(object):
    def __init__(self):
        self.all_cabs = dict()
        self.all_vehicles = dict()
        self.all_drivers = dict()

    def createVehicle(self, vehicle_name):
        vehicle_id = get_unique_identifier()
        my_vehicle = Vehicle(vehicle_id, vehicle_name)
        return my_vehicle

    def createCab(self, driver, location_x, location_y):
        vehicle = self.createVehicle("Etios")
        cab_id = get_unique_identifier()
        location = Location(get_unique_identifier(), location_x, location_y)
        my_cab = Cab(cab_id, driver, vehicle, location)
        self.all_cabs[cab_id] = my_cab
        return cab_id

    def getCab(self, cab_id):
        return self.all_cabs[cab_id]

    def createDriver(self, driver_name):
        driver_id = get_unique_identifier()
        my_driver = Driver(driver_id, driver_name)
        self.all_drivers[driver_id] = my_driver
        return driver_id

    def getDriver(self, driver_id):
        return self.all_drivers[driver_id]

    def updateDriverAvailability(self, driver_id, availability_status):
        my_driver = self.all_drivers[driver_id]
        my_driver.update_status(availability_status)

    def updateCabAvailability(self, cab_id, availability_status):
        my_cab = self.getCab(cab_id)
        my_cab.update_status(availability_status)

    def get_nearest_cab(self, rider_location_x, rider_location_y):

        for x in self.all_cabs:
            my_cab = self.all_cabs[x]
            cab_location_x = my_cab.location.get_x_location()
            cab_location_y = my_cab.location.get_y_location()
            if my_cab.status is CabStatus.AVAILABLE:
                distance = get_cartesian_distance(cab_location_x, cab_location_y, rider_location_x, rider_location_y)
                if distance < ENV_VAR.ACCEPTABLE_DISTANCE:
                    return my_cab

        return None


cab_service = CabService()
