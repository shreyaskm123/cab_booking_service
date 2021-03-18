import math
from decimal import Decimal
from uuid import uuid4


def get_unique_identifier():
    return uuid4()


@property
def get_fair_estimate():
    return Decimal('100')


def get_cartesian_distance(first_x, first_y, second_x, second_y):

    my_distance = math.sqrt(pow(second_x-first_x, 2) + pow(second_y-first_y, 2))
    return my_distance
