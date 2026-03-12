bookings = {}
class InvalidBookingError(Exception):
    pass
def book_flight():
    name = input("Enter your name:")
    flight = input("Enter flight number:")
    if flight not in ["AA101", "BA202", "CA303"]:
        try:
            raise InvalidBookingError("Invalid flight number. Please choose a valid flight.")
        except InvalidBookingError as e:
            print(e)
            return
    bookings[name] = flight
    print(f"Flight {flight} booked successfully for {name}.")

def view_bookings():
    if not bookings:
        print("No bookings found.")
    else:
        print("Current Bookings:")
        for name, flight in bookings.items():
            print(f"{name} - {flight}")

while True:
    print("\n1. Book a flight")
    print("2. View bookings")
    print("3. Exit")
    choice = input("Enter your choice:")
    if choice == "1":
        book_flight()
    elif choice == "2":
        view_bookings()
        break
    elif choice == "3":
        print("Exiting the booking system.")
        break
    else:
        print("Invalid choice. Please enter 1, 2, or 3.")