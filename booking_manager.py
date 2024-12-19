from flight import Flight
from fare_manager import FareManager
from flight_manager_constants import SeatClass, BookingStatus
from uniq_id import UniqId

class BookingManager:
    def __init__(self, pasenger, flight: Flight, fare: int, seat_class: SeatClass, num_seats: int): 
        self.id = UniqId().getId()
        self.flight = flight
        self.pasenger = pasenger
        self.fare = fare
        self.seat_class = seat_class
        self.num_seats = num_seats
        self.status = BookingStatus.BOOKED

    def __str__(self):
        return '{} | {} | {} | {} | {} | {} | {} | {}'.format(self.id, self.flight.name, self.pasenger.name, self.fare, self.seat_class, self.num_seats, self.status, self.flight.status)


    # -------------------------------------------------------------------------
    # @params          pasenger: User               User who is booking the flight
    # @params          flight: Flight               Flight to be booked
    # @params          seat_class: SeatClass        Class of seat to be booked
    # @params          num_seats: integer           Number of seats to be booked
    # Route            /book_flight
    # -------------------------------------------------------------------------
    def bookFlight(self):
        if self.pasenger.scheduled_flights.get(self.id):
            print('Flight with id {} already booked'.format(self.id))
            return
        
        # Adding the flight to the pasenger's bookings
        self.pasenger.scheduled_flights[self.id] = self

        # Adding the bookings to the flights
        self.flight.bookings[self.id] = self
        self.flight.available_seats -= self.num_seats

        if self.seat_class == SeatClass.ECONOMY:
            self.flight.economy_seats -= self.num_seats
        elif self.seat_class == SeatClass.BUSINESS:
            self.flight.business_seats -= self.num_seats
        elif self.seat_class == SeatClass.PREMIUM:
            self.flight.premium_seats -= self.num_seats
        else:
            return "Invalid seat class."
        
        print('Flight with id {} booked successfully'.format(self.flight.id))
        return self
        


