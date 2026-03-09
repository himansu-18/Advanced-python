class BillingSystem:

    def __init__(self):
        self.items = []


    def add_item(self, name, price, quantity):
        total = price * quantity
        self.items.append({
            "name": name,
            "price": price,
            "quantity": quantity,
            "total": total
        })

    
    def calculate_total(self):
        total_bill = 0
        for item in self.items:
            total_bill += item["total"]
        return total_bill

    
    def generate_bill(self):
        print("\n------ BILL RECEIPT ------")
        print("{:<15}{:<10}{:<10}{:<10}".format("Item", "Price", "Qty", "Total"))

        for item in self.items:
            print("{:<15}{:<10}{:<10}{:<10}".format(
                item["name"],
                item["price"],
                item["quantity"],
                item["total"]
            ))

        print("---------------------------")
        print("Total Amount:", self.calculate_total())
        print("---------------------------")



def main():

    bill = BillingSystem()

    while True:
        print("\n1. Add Item")
        print("2. Generate Bill")
        print("3. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            name = input("Enter item name: ")
            price = float(input("Enter item price: "))
            qty = int(input("Enter quantity: "))
            bill.add_item(name, price, qty)

        elif choice == "2":
            bill.generate_bill()

        elif choice == "3":
            print("Thank you!")
            break

        else:
            print("Invalid choice")


if __name__ == "__main__":
    main()