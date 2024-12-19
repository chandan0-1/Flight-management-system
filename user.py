from flight_manager_constants import SeatClass
from fare_manager import FareManager
from uniq_id import UniqId
from booking_manager import BookingManager


class User:
    def __init__(self, name, email, phone_number, id = None):
        self.id = id or UniqId().getId()
        self.name = name
        self.email = email
        self.phone_number = phone_number
        self.scheduled_flights = {}


    def __str__(self):
        return '{} | {} | {} | {}'.format(self.id, self.name, self.email, self.phone_number)
    

    # -------------------------------------------------------------------------
    # Ruote            /user/show_all_flights
    # -------------------------------------------------------------------------
    def displayScheduledFlights(self):
        print('...........' * 10)
        print('             \t\tScheduled Flights for => {} | {}'.format(self.name, self.email))
        print('...........' * 10)
        print()

        for index, bookings in enumerate(self.scheduled_flights.values(), start=1):  # start=1 to start index from 1
            if bookings.status == 'Cancelled':
                print(f"Booking #{index}: {bookings.flight.name} | {bookings.flight.origin} -> {bookings.flight.destination} is Cancelled.\n")
                continue
            print(f"Scheduled Flight #{index}: {bookings.flight.name} | {bookings.flight.origin} -> {bookings.flight.destination}")
            print('\t\tBooking Details: {} Rs. with total {} seats in {} class.\n'.format(bookings.fare, bookings.num_seats, bookings.seat_class))


    # -------------------------------------------------------------------------
    # @params          flight: Flight               Flight to be booked
    # @params          seat_class: SeatClass        Class of seat to be booked
    # Route            /user/book_flight
    # -------------------------------------------------------------------------
    def bookFlight(self, flight, seat_class: SeatClass):
        if self.scheduled_flights.get(flight.id):
            print('Flight with id {} already scheduled'.format(flight.id))
            return
        
        is_success, message, fare = FareManager().getFare(flight, seat_class, 1)
        if not is_success:
            print(message)
            return
        
        scheduledFlight = BookingManager(self, flight, fare, seat_class, 1)
        scheduledFlight.bookFlight()

        self.scheduled_flights[scheduledFlight.id] = scheduledFlight

        print('Flight with id {} scheduled successfully'.format(flight.id))
        return scheduledFlight
    
    # -------------------------------------------------------------------------
    # @params          booking_id: str               Booking with matching id to be cancelled
    # Route            /user/cancel_booking_by_id
    # -------------------------------------------------------------------------
    def cancelBookingByBookingId(self, booking_id):
        if not self.scheduled_flights.get(booking_id):
            print('Booking with id {} does not exist'.format(booking_id))
            return
        
        booking = self.scheduled_flights[booking_id]
        booking.flight.available_seats += booking.num_seats
        
        if booking.seat_class == SeatClass.ECONOMY:
            booking.flight.economy_seats += booking.num_seats
        elif booking.seat_class == SeatClass.BUSINESS:
            booking.flight.business_seats += booking.num_seats
        elif booking.seat_class == SeatClass.PREMIUM:
            booking.flight.premium_seats += booking.num_seats
        else:
            return "Invalid seat class."
        
        booking.status = 'Cancelled'
        print('Booking with id {} cancelled successfully'.format(booking_id))
        return booking
