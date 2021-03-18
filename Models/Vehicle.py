from Models.VehicleType import VehicleType


class Vehicle(object):
    def __init__(self, vehicle_id, vehicle_name):
        self.vehicle_id = vehicle_id
        self.vehicle_name = vehicle_name
        self.vehicle_type = VehicleType.CAR
