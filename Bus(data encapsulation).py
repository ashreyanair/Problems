from datetime import datetime


class Bus:
    def __init__(self, bno, ac, cap):
        self.bno = bno
        self.ac = ac
        self.cap = cap

    def get_bno(self):
        return self.bno

    def get_ac(self):
        return self.ac

    def get_cap(self):
        return self.cap

    def display(self):
        print("1. Bus No:", self.get_bno())
        print("2. AC:", "Yes" if self.get_ac() else "No")
        print("3. Capacity:", self.get_cap())


class Booking:
    def __init__(self, name, bno, date):
        self.name = name
        self.bno = bno
        self.date = date

    def make_booking(self, Buses, Bookings):
        if self.is_available(Buses, Bookings, self.bno, self.date):
            Bookings.append(self)
            print("Booking confirmed for", self.name)
        else:
            print("Bus is full on this date")

    def is_available(self, Buses, Bookings, bno, date):
        booked = 0
        capacity = 0
        for bus in Buses:
            if bus.get_bno() == bno:
                capacity = bus.get_cap()
        for book in Bookings:
            if book.bno == bno and book.date == date:
                booked += 1
        return booked < capacity

    def display_book_info(self):
        print(f"Name: {self.name}, Bus No: {self.bno}, Date: {self.date.strftime('%d-%m-%Y')}")


# Main Execution

BUSES = [Bus(1, True, 2), Bus(2, False, 60), Bus(3, True, 55)]
print("Available buses are:")
for bus in BUSES:
    bus.display()
    print("-----------------------------------------------------")

BOOKINGS = []

while True:
    print("\nMenu:")
    print("1. Book Ticket")
    print("2. View Bookings")
    print("3. Exit")
    ch = int(input("Enter your choice: "))

    if ch == 1:
        try:
            name = input("Enter your name: ")
            bno = int(input("Enter bus number: "))
            d = input("Enter the date (dd-mm-yyyy): ")
            date = datetime.strptime(d, "%d-%m-%Y")
            booking = Booking(name, bno, date)
            booking.make_booking(BUSES, BOOKINGS)
        except ValueError:
            print("Invalid date or input format.")
    elif ch == 2:
        if not BOOKINGS:
            print("No bookings available so far.")
        else:
            print("\n--- Booking Details ---")
            for book in BOOKINGS:
                book.display_book_info()
    elif ch == 3:
        print("Exiting system. Thank you!")
        break
    else:
        print("Invalid choice.")