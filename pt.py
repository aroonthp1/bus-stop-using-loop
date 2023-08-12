def get_positive_integer(prompt):
    while True:
        try:
            value = int(input(prompt))
            if value <= 0:
                raise ValueError
            return value
        except ValueError:
            print("Please enter a positive integer.")

def get_non_negative_integer(prompt):
    while True:
        try:
            value = int(input(prompt))
            if value < 0:
                raise ValueError
            return value
        except ValueError:
            print("Please enter a non-negative integer.")

def process_stop(stop_number, current_passengers, max_capacity):
    passengers_leaving = get_non_negative_integer(
        f"Enter the number of passengers leaving at stop {stop_number}: "
    )
    while passengers_leaving > current_passengers:
        print("Error: Passengers leaving cannot be more than current passengers. Try again.")
        passengers_leaving = get_non_negative_integer(
            f"Enter the number of passengers leaving at stop {stop_number}: "
        )
    current_passengers -= passengers_leaving

    passengers_waiting = get_non_negative_integer(
        f"Enter the number of passengers waiting to get on at stop {stop_number}: "
    )
    available_seats = max_capacity - current_passengers

    if passengers_waiting <= available_seats:
        current_passengers += passengers_waiting
        return current_passengers, passengers_waiting, 0
    else:
        return max_capacity, available_seats, passengers_waiting - available_seats

def main():
    print("Welcome to Codetown Bus Data Collection")

    route_number = get_positive_integer("Enter the route number: ")
    num_stops = get_positive_integer("Enter the number of stops (at least 3): ")
    while num_stops < 3:
        print("Please enter at least 3 stops.")
        num_stops = get_positive_integer("Enter the number of stops (at least 3): ")

    max_capacity = 35
    current_passengers = get_non_negative_integer(
        "Enter the number of passengers at the start of the route: "
    )

    stops = range(1, num_stops)
    passenger_info = [process_stop(stop, current_passengers, max_capacity) for stop in stops]
    current_passengers = passenger_info[-1][0]
    happy_customers = sum(info[1] for info in passenger_info)
    unhappy_customers = sum(info[2] for info in passenger_info)

    ratio = happy_customers / max(1, unhappy_customers)
    print("\nRoute Number:", route_number)
    print("Total Happy Customers:", happy_customers)
    print("Total Unhappy Customers:", unhappy_customers)
    print(f"Happy Customers to Unhappy Customers Ratio: {ratio:.2f}")

if __name__ == "__main__":
    main()
