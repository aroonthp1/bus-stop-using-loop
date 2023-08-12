class BusRoute():
    def __init__(self):
        self.route_number = None
        self.num_stops = None
        self.max_capacity = 35
        self.happy_customers = 0
        self.unhappy_customers = 0
        
    
    def get_positive_integer(self, prompt): ##function creted for taking positive number 
        while True:    ## using while loop for condion check only for value greater than zero, if other value it generate message .
            try:
                value = int(input(prompt))
                if value <= 0:
                    raise ValueError
                return value
            except ValueError:
                print("Please enter a positive integer.")


    def get_non_negative_integer(self, prompt):
        while True:
            try:
                value = int(input(prompt))
                if value < 0:
                    raise ValueError
                return value
            except ValueError:
                print("Please enter a non-negative integer.")


def main():
    bus_route_obj = BusRoute()
    print("Welcome to Codetown Bus Data Collection")

    bus_route_obj.route_number = bus_route_obj.get_positive_integer("Enter the route number: ")
    bus_route_obj.num_stops = bus_route_obj.get_positive_integer("Enter the number of stops (at least 3): ")
    while bus_route_obj.num_stops < 3:
        print("Please enter at least 3 stops.")
        bus_route_obj.num_stops = bus_route_obj.get_positive_integer("Enter the number of stops (at least 3): ")

    current_passengers = bus_route_obj.get_non_negative_integer(
       "Enter the number of passengers at the start of the route: "
    )

    for stop in range(1, bus_route_obj.num_stops):
        while True:
            passengers_leaving = bus_route_obj.get_non_negative_integer(
                f"Enter the number of passengers leaving at stop {stop}: "
            )
            if passengers_leaving <= current_passengers:
                current_passengers -= passengers_leaving
                break
            else:
                print(
                    "Error: Passengers leaving cannot be more than current passengers. Try again."
                )

        passengers_waiting = bus_route_obj.get_non_negative_integer(
            f"Enter the number of passengers waiting to get on at stop {stop}: "
        )
        available_seats = bus_route_obj.max_capacity - current_passengers

        if passengers_waiting <= available_seats:
            current_passengers += passengers_waiting
            bus_route_obj.happy_customers += passengers_waiting
        else:
            bus_route_obj.happy_customers += available_seats
            bus_route_obj.unhappy_customers += passengers_waiting - available_seats
            current_passengers = bus_route_obj.max_capacity

    ratio = bus_route_obj.happy_customers / max(1, bus_route_obj.unhappy_customers)
    print("\nRoute Number:", bus_route_obj.route_number)
    print("Total Happy Customers:", bus_route_obj.happy_customers)
    print("Total Unhappy Customers:", bus_route_obj.unhappy_customers)
    print(f"Happy Customers to Unhappy Customers Ratio: {ratio:.2f}")


if __name__ == "__main__":
    main()