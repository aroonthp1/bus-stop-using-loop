def get_positive_integer(prompt): ##function creted for taking positive number 
    while True:    ## using while loop for condion check only for value greater than zero, if other value it generate message .
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

    happy_customers = 0
    unhappy_customers = 0

    for stop in range(1, num_stops):
        while True:
            passengers_leaving = get_non_negative_integer(
                f"Enter the number of passengers leaving at stop {stop}: "
            )
            if passengers_leaving <= current_passengers:
                current_passengers -= passengers_leaving
                break
            else:
                print(
                    "Error: Passengers leaving cannot be more than current passengers. Try again."
                )

        passengers_waiting = get_non_negative_integer(
            f"Enter the number of passengers waiting to get on at stop {stop}: "
        )
        available_seats = max_capacity - current_passengers

        if passengers_waiting <= available_seats:
            current_passengers += passengers_waiting
            happy_customers += passengers_waiting
        else:
            happy_customers += available_seats
            unhappy_customers += passengers_waiting - available_seats
            current_passengers = max_capacity

    ratio = happy_customers / max(1, unhappy_customers)
    print("\nRoute Number:", route_number)
    print("Total Happy Customers:", happy_customers)
    print("Total Unhappy Customers:", unhappy_customers)
    print(f"Happy Customers to Unhappy Customers Ratio: {ratio:.2f}")


if __name__ == "__main__":
    main()
