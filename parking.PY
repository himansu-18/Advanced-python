class Park:
    def __init__(self):
        self.parking_lot = {
            1: None,
            2: None,
            3: None,
            4: None
        }
        self.occupied = set()
    def locate(self):
        self.slot_number = int(input("Enter slot number to locate: "))
        if self.slot_number in self.parking_lot:
            if self.parking_lot[self.slot_number] is None:
                print("Slot",self.slot_number,"is available.")
            else:
                print("Slot" ,self.slot_number, "is occupied by ",self.parking_lot[self.slot_number])
        else:
            print("Invalid slot number.")
    def allocate(self):
        self.slot_number = int(input("Enter slot number to allocate: "))
        if self.slot_number in self.parking_lot:
            if self.parking_lot[self.slot_number] is None:
                self.vehicle_number = input("Enter vehicle number: ")
                self.parking_lot[self.slot_number] = self.vehicle_number
                self.occupied.add(self.slot_number)
                print("Slot",self.slot_number,"allocated to ",self.vehicle_number)
            else:
                print("Slot",self.slot_number,"is already occupied by",self.parking_lot[self.slot_number])
        else:
            print("Invalid slot number.")

    def deallocate(self):
        self.slot_number = int(input("Enter slot number to deallocate: "))
        if self.slot_number in self.parking_lot:
            if self.parking_lot[self.slot_number] is not None:
                self.parking_lot[self.slot_number] = None
                self.occupied.remove(self.slot_number)
                print("Slot",self.slot_number,"deallocated successfully.")
            else:
                print("Slot",self.slot_number,"is already vacant.")
        else:
            print("Invalid slot number.")
    def ext(self):
        print("Exiting the program.")
        exit()

   x = Park()
while True:
    print("1.Locate Slot")
    print("2.Allocate Slot")
    print("3.Deallocate Slot")
    print("4.Exit")
    choice = int(input("Enter your choice: "))


    if choice == 1:
        x.locate()
    elif choice == 2:
        x.allocate()
    elif choice == 3:
        x.deallocate()
    elif choice == 4:
        x.ext()
    else:
        print("Invalid choice. Please try again.")
        
        