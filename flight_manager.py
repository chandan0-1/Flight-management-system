from flight import Flight

class FlightManager:
    def __init__(self):
        self.flights = {}

    # -----------------------------------------------------------------------
    #                       Flight Section
    # -----------------------------------------------------------------------

    # -------------------------------------------------------------------------
    # @params          flight: Flight               Flight to be added
    # Ruote            /flight_manager/add_flight
    # -------------------------------------------------------------------------
    def addFlight(self, flight):
        if self.flights.get(flight.id):
            print('Flight with id {} already exists'.format(flight.id))
            return
        
        self.flights[flight.id] = flight
        print('Flight with id {} added successfully'.format(flight.id))
        return flight

    # -------------------------------------------------------------------------
    # @params          name: str                    Name of the flight
    # @params          origin: str                  Origin of the flight
    # @params          destination: str             Destination of the flight
    # @params          airline: str                 Airline of the flight
    # @params          schedule: str                Schedule of the flight
    # @params          capacity: int                Total capacity of the flight
    # @params          available_seats: int         Available seats in the flight
    # @params          base_fare: int               Base fare of the flight
    # @params          id: str  (optional)          Unique id of the flight (optional)
    # -------------------------------------------------------------------------
    def verifyAndAddFlight(self, name, origin, destination, airline, schedule, capacity, available_seats, base_fare, id = None):
        if not name or len(name) < 1:
            print('Flight Name is mandatory or should be more than 1 character')
            return
        
        if not origin or not destination or len(origin) < 2 or len(destination) < 2:
            print('Origin and Destination are mandatory or should be more than 2 characters')
            return
        
        flight = Flight(name, origin, destination, airline, schedule, capacity, available_seats, base_fare, id)
        self.addFlight(flight)
        return flight

    # -------------------------------------------------------------------------
    # @params          flightId: str                Id of the flight to be removed
    # Ruote            /flight_manager/remove_flight
    # -------------------------------------------------------------------------
    def removeFlight(self, flightId):
        if not self.flights.get(flightId):
            print('Flight with id {} does not exist'.format(flightId))
            return

        del self.flights[flightId]
        print('Flight with id {} removed successfully'.format(flightId))

    # -------------------------------------------------------------------------
    # Ruote            /flight_manager/display_all_flights
    # -------------------------------------------------------------------------
    def displayAllFlights(self):
        print('             ...............................................')
        print('             Flight Details')
        print('             ...............................................\n')
        for flight in self.flights.values():
            print(flight)
            print()


    # -------------------------------------------------------------------------
    # @params          flightId: str                Id of the flight to be fetched
    # Ruote            /flight_manager/fetch_flight_by_id
    # -------------------------------------------------------------------------
    def fetchFlightById(self, flightId: str):
        if not self.flights.get(flightId):
            print('Flight with id {} does not exist'.format(flightId))
            return
        return self.flights[flightId]
    
    # -------------------------------------------------------------------------
    # @params          origin: str                  Origin of the flight to be fetched
    # Ruote            /flight_manager/fetch_flights_by_origin
    # -------------------------------------------------------------------------
    def fetchFlightsByOrigin(self, origin: str):
        flights = [flight for flight in self.flights.values() if flight.origin == origin]
        if not flights:
            print('No flights available for origin {}'.format(origin))
            return
        return flights
    
    # -------------------------------------------------------------------------
    # @params          name: str             Name of the flight to be searched
    # Ruote            /flight_manager/search_flight
    # -------------------------------------------------------------------------
    def searchFlightByName(self, name: str):
        # Checking if partially contains flight name
        flights = [flight for flight in self.flights.values() if name in flight.name]
        if not flights:
            print('No flights available with name {}'.format(name))
            return
        
        # Matching flights with the name
        print('...........' * 10)
        print('\t\t\tMatching Flights with name => {}'.format(name))
        print('...........' * 10)
        for i, flight in enumerate(flights, start=1):
            print(f'Flight #{i}: {flight}')
            print()
        return flights


    # -----------------------------------------------------------------------
    # ---------------------------   User Section ----------------------------
    # -----------------------------------------------------------------------

    # ------------------------------------------------------------------------------------------------
    # @params          name: str                    Name of the user
    # @params          email: str                   Email of the user
    # @params          phone_number: int            Phone number of the user
    # @params          id: str  (optional)          Unique id of the user (optional)  required: false
    # Ruote            /flight_manager/create_user
    # ------------------------------------------------------------------------------------------------
    def createUser(self, name, email, phone_number, id = None):
        if not name or not email or not phone_number:
            print('All fields are mandatory')
            return
        
        if len(name) < 4 or len(email) < 4 or len(str(phone_number)) < 5:
            print('Name and email should be more than 4 characters and Phone number should be more than 5 characters')
            return
        
        from user import User
        user = User(name, email, phone_number, id)

        print('User created successfully')
        print(user)
        print()

        return user


    # -----------------------------------------------------------------------
    # --------------------   Booking Section Driver Code --------------------
    # -----------------------------------------------------------------------
    def initProgram(self):
        from flight_manager_constants import SeatClass

        f1 = self.verifyAndAddFlight('F1', 'Bangalore', 'Delhi', 'Indigo', '2024-12-20 10:00AM', 50, 50, 5000)
        f2 = self.verifyAndAddFlight('F2', 'Bangalore', 'Mumbai', 'SpiceJet', '2024-12-21 11:00AM', 50, 50, 4000)
        f3 = self.verifyAndAddFlight('F3', 'Bangalore', 'Chennai', 'Air India', '2024-12-22 12:00PM', 50, 50, 3000)
        f4 = self.verifyAndAddFlight('A1', 'Bangalore', 'Kolkata', 'Vistara', '2024-12-23 01:00PM', 50, 50, 2000)

        u1 = self.createUser('Chandan', 'chandan@gmail.com', 123425, 'u1')
        u2 = self.createUser('Rahul', 'rahul@gmail.com', 123456)
        u3 = self.createUser('Rajesh', 'rajesh@gmail.com', 123457)
        u4 = self.createUser('Ramesh', 'ramesh@gmail.com', 123458)

        b1 = u1.bookFlight(f1, SeatClass.ECONOMY)
        b2 = u2.bookFlight(f1, SeatClass.BUSINESS)
        b3 = u2.bookFlight(f2, SeatClass.ECONOMY)
        b4 = u3.bookFlight(f2, SeatClass.PREMIUM)
        b5 = u4.bookFlight(f3, SeatClass.ECONOMY)
        b6 = u2.bookFlight(f4, SeatClass.BUSINESS)

        u2.displayScheduledFlights()
        u3.displayScheduledFlights()
        u4.displayScheduledFlights()
        u1.displayScheduledFlights()

        self.searchFlightByName('F')

        u2.cancelBookingByBookingId(b2.id)
        f4.cancelFlight()
        u2.cancelBookingByBookingId(b6.id)

        u2.displayScheduledFlights()
        u3.displayScheduledFlights()
        u4.displayScheduledFlights()
        u1.displayScheduledFlights()

        f1.showAllBookings()
        f2.showAllBookings()
        f3.showAllBookings()
        f4.showAllBookings()



flight_manager = FlightManager()
flight_manager.initProgram()