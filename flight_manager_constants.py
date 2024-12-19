from enum import Enum

# Define the Enum for seat classes
class SeatClass(Enum):
    ECONOMY = "economy"
    BUSINESS = "business"
    PREMIUM = "premium"

class FlightConstants:
    # Define the percentage of seats for each class
    ECONOMY_SEATS_PERCENTAGE = 0.5
    BUSINESS_SEATS_PERCENTAGE = 0.3
    PREMIUM_SEATS_PERCENTAGE = 0.2

    # Define the total capacity of the flight
    CAPACITY = 50

    # Define the default number of available seats
    AVAILABLE_SEATS = 50


class FlightStatus(Enum):
    SCHEDULED = "scheduled"
    CANCELLED = "cancelled"
    DEPARTED = "departed"
    ARRIVED = "arrived"
    DIVERTED = "diverted"


class BookingStatus(Enum):
    BOOKED = "booked"
    CANCELLED = "cancelled"