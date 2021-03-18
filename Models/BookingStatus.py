from enum import Enum


class BookingStatus(Enum):
    CREATED, CONFIRMED, CANCELLED = 0, 1, 2
