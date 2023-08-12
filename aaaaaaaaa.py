class BusRoute():
    def __init__(self, max_capacity): #Constructor used to  initialize attributes of class Busroute 
        self.route_number = None
        self.num_stops = None
        self.max_capacity = max_capacity
        self.happy_customers = 0
        self.unhappy_customers = 0
        self.current_passengers = 0
        
    
    def get_positive_integer(self, prompt): ## method used to get positive integers from user.
        while True:    
            try:
                value = int(input(prompt))
                if value <= 0:
                    raise ValueError
                return value
            except ValueError:
                print("Please enter a positive integer.")


    def get_non_negative_integer(self, prompt):
        #method to get non negative integers from the users
        while True:
            try:
                value = int(input(prompt))
                if value < 0:
                    raise ValueError
                return value
            except ValueError:
                print("Please enter a non-negative integer.")


def main(): # initialize to get maximum capacity equals to thirty-five
    bus_route_obj = BusRoute(max_capacity=35)
    print("Welcome to Codetown Bus Data Collection")

    bus_route_obj.route_number = bus_route_obj.get_positive_integer("Enter the route number: ")
    bus_route_obj.num_stops = bus_route_obj.get_positive_integer("Enter the number of stops (at least 3): ")
    # asking user to provide at least greaer than 3 steps
    while bus_route_obj.num_stops < 3:
        print("Please enter at least 3 stops.")
        bus_route_obj.num_stops = bus_route_obj.get_positive_integer("Enter the number of stops (at least 3): ")

    for stop in range(1, bus_route_obj.num_stops+1):
        while True:
            if stop == 1:
                break
            #collect no of clients in busstop
            passengers_leaving = bus_route_obj.get_non_negative_integer(
                f"Enter the number of passengers leaving at stop {stop}: "
            )
            if passengers_leaving <= bus_route_obj.current_passengers:
                bus_route_obj.current_passengers -= passengers_leaving
                break
            else:
                print(
                    "Error: Passengers leaving cannot be more than current passengers. Try again."
                )
                
        if stop== bus_route_obj.num_stops:
            break
        passengers_waiting = bus_route_obj.get_non_negative_integer(
            f"Enter the number of passengers waiting to get on at stop {stop}: "
        )
        available_seats = bus_route_obj.max_capacity - bus_route_obj.current_passengers

        if passengers_waiting <= available_seats:##if passenger seat are limited, update passenger seats
            bus_route_obj.current_passengers += passengers_waiting
            bus_route_obj.happy_customers += passengers_waiting
        else:     ## go to cout the bus seat, if not enough seats are avliable.
            bus_route_obj.happy_customers += available_seats
            bus_route_obj.unhappy_customers += passengers_waiting - available_seats
            bus_route_obj.current_passengers = bus_route_obj.max_capacity
         ##steps to calculate ratio of happy to unhappy customers of bus.
    if bus_route_obj.unhappy_customers == 0:
        ratio = 0
    else:
        ratio = bus_route_obj.happy_customers / bus_route_obj.unhappy_customers
    print("\nRoute Number:", bus_route_obj.route_number)
    print("Total Happy Customers:", bus_route_obj.happy_customers)
    print("Total Unhappy Customers:", bus_route_obj.unhappy_customers)
    print(f"Happy Customers to Unhappy Customers Ratio: {ratio:.2f}")


if __name__ == "__main__":
    main()