from flight_manager_constants import SeatClass
from flight import Flight

class FareManager:
    def __init__(self):
        pass

    # -------------------------------------------------------------------------
    # @params          flight: Flight               Flight to be booked
    # @params          seat_class: SeatClass        Class of seat to be booked
    # @params          num_seats: integer           Number of seats to be booked
    # Ruote            /fare_manager/fetch_fare_by_seat_class_type
    # -------------------------------------------------------------------------
    def getFare(self, flight: Flight, seat_class: SeatClass, num_seats: int):
        # Check if enough seats are available for the selected class
        seat_price = 0
        seat_class_fare = self.fetchFareBySeatClassType(flight, seat_class)
        seat_price = self.handleDynamicFare(flight, seat_class, seat_class_fare)

        if seat_class == SeatClass.ECONOMY:
            if flight.economy_seats < num_seats:
                return [False, "Not enough economy seats available.", 0]

        elif seat_class == SeatClass.BUSINESS:
            if flight.business_seats < num_seats:
                return [False, "Not enough business seats available.", 0]

        elif seat_class == SeatClass.PREMIUM:
            if flight.premium_seats < num_seats:
                return [False, "Not enough premium seats available.", 0]
        else:
            return [False, "Invalid seat class.", 0]

        # Calculate total fare
        total_fare = seat_price * num_seats
        return [True, None, total_fare]
    

    # -------------------------------------------------------------------------
    # @params          flight: Flight               Flight to be booked
    # @params          seat_class: SeatClass        Class of seat to be booked
    # Ruote            /fare_manager/fetch_fare_by_seat_class_type
    # -------------------------------------------------------------------------
    def fetchFareBySeatClassType(self, flight: Flight, seat_class: SeatClass):
        # Economy seats use the base fare
        if seat_class == SeatClass.BUSINESS:
            return flight.base_fare * 2
        
        # Premium class is typically three times the base fare
        elif seat_class == SeatClass.PREMIUM:
            return flight.base_fare * 3
        
        return flight.base_fare

    
    # -------------------------------------------------------------------------
    # @params          flight: Flight               Flight to be booked
    # @params          seat_class: SeatClass        Class of seat to be booked
    # @params          base_fare: integer           Base seat class fare for the flight 
    # Ruote            /fare_manager/fetch_dynamic_fare
    # -------------------------------------------------------------------------
    def handleDynamicFare(self, flight: Flight, seat_class: SeatClass, base_fare: int):
        if flight.available_seats < flight.capacity * 0.3:
            # if less than 30% of the seats are available
            return base_fare * 1.5
        elif flight.available_seats < flight.capacity * 0.2:
            # if less than 20% of the seats are available
            return base_fare * 2
        elif flight.available_seats < flight.capacity * 0.1:
            # if less than 10% of the seats are available
            return base_fare * 3
        
        return base_fare
        
