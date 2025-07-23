from datetime import datetime

class bus:
    def __init__(self, bno, cap, ac):
        self.bno = bno
        self.cap = cap
        self.ac = ac

    def get_bno(self):
        return self.bno

    def get_cap(self):
        return self.cap

    def get_ac(self):
        return self.ac

    def display(self):
        print("Bus no      :", self.get_bno())
        print("Capacity    :", self.get_cap())
        print("AC:", self.get_ac())
        print()

BUSES = [bus(1, 2, True), bus(2, 50, False), bus(3, 60, True)]

print("Available buses:")
for i in BUSES:
    i.display()

class Booking:
    def __init__(self):
        self.name = input("Enter your name: ")
        self.bno = int(input("Enter the bus no: "))
        d = input("Enter the date (dd-mm-yyyy): ")
        self.date = datetime.strptime(d, "%d-%m-%Y").date()

    def make_booking(self, BUSES, BOOKINGS):
        bus_exists = any(bus.get_bno() == self.bno for bus in BUSES)

        if not bus_exists:
            print(f"Bus number {self.bno} does not exist.")
            return

        if self.is_available(BUSES, BOOKINGS, self.bno, self.date):
            BOOKINGS.append(self)
            print("Booking successful!")
        else:
            print("Bus is full on that date.")

    def is_available(self, BUSES, BOOKINGS, bno, date):
        booked = 0
        capacity = 0
        for i in BUSES:
            if i.bno == bno:
                capacity = i.cap
                break
        for i in BOOKINGS:
            if i.bno == bno and i.date == date:
                booked += 1
        return booked < capacity

    def dis_book_info(self):
        print(f"{'Passenger':15}: {self.name}")
        print(f"{'Bus No':15}: {self.bno}")
        print(f"{'Date':15}: {self.date}")
        print()

BOOKINGS = []

while True:
    print("\n--- Menu ---")
    print("1. Book ticket")
    print("2. View bookings")
    print("3. Exit")
    ch = int(input("Enter your choice: "))

    if ch == 1:
        b = Booking()
        b.make_booking(BUSES, BOOKINGS)

    elif ch == 2:
        if not BOOKINGS:
            print("No bookings available.")
        else:
            for i in BOOKINGS:
                i.dis_book_info()

    elif ch == 3:
        print("Exiting")
        break

    else:
        print("Invalid choice. Try again.")
