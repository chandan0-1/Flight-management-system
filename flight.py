from uniq_id import UniqId
from flight_manager_constants import FlightConstants, FlightStatus

class Flight:
    def __init__(self, name, origin, destination, airline, schedule, capacity = 50, available_seats = 50, base_fare = 1000, id = None):
        self.name = name
        self.origin = origin
        self.destination = destination
        self.airline = airline
        self.schedule = schedule
        self.capacity = capacity
        self.available_seats = available_seats
        self.base_fare = base_fare
        self.bookings = {}
        self.status = FlightStatus.SCHEDULED
        self.id = id or UniqId().getId()

        # Seats allocation based on type of pasanger class
        self.economy_seats = capacity * FlightConstants.ECONOMY_SEATS_PERCENTAGE # 50% of the total capacity
        self.business_seats = capacity * FlightConstants.BUSINESS_SEATS_PERCENTAGE # 30% of the total capacity
        self.premium_seats = capacity * FlightConstants.PREMIUM_SEATS_PERCENTAGE # 20% of the total capacity

    def __str__(self):
        if self.status == FlightStatus.CANCELLED:
            return '{} | {} <-> {} | {} | schedules to departs at {} | has total {} seats & currently available = {} seats | Flight is Cancelled'.format(self.name, self.origin, self.destination, self.airline, self.schedule, self.capacity, self.available_seats)
        return '{} | {} <-> {} | {} | schedules to departs at {} | has total {} seats & currently available = {} seats'.format(self.name, self.origin, self.destination, self.airline, self.schedule, self.capacity, self.available_seats)
    

    # -------------------------------------------------------------------------
    # Ruote            /flight/show_all_bookings
    # -------------------------------------------------------------------------
    def showAllBookings(self):
        print('...........' * 10)
        print('             \t\tBookings for Flight => {} | {} | {}'.format(self.name, self.origin, self.destination))
        print('...........' * 10)
        print()
        
        if self.status == FlightStatus.CANCELLED:
            print('Flight is Cancelled. No bookings available. please check below booking details.')
            print('Booking amount will be refunded to the respective pasanger.')
        
        for index, booking in enumerate(self.bookings.values(), start=1):
            print(f"Booking #{index}: {booking.pasenger}")
            print()

    # -------------------------------------------------------------------------
    # Ruote            /flight/cancel_flight
    # -------------------------------------------------------------------------
    def cancelFlight(self):
        self.status = FlightStatus.CANCELLED
        self.available_seats = 0
        self.economy_seats = 0
        self.business_seats = 0
        self.premium_seats = 0
        print('Flight {} | {} cancelled successfully'.format(self.id, self.name))
        return self
