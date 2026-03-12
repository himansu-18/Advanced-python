orders = {}
class OrderError(Exception):
    pass
def place_order():
    order_id = input("Enter order ID:")
    product = input("Enter product name:")  
    if product not in ["Laptop", "Phone", "Headphones"]:
        try:
            raise OrderError("Invalid product. Please choose a valid product.")
        except OrderError as e:
            print(e)
            return
    orders[order_id] = product
    print(f"Order {order_id} placed successfully for {product}.")
def view_orders():
    if not orders:
        try:
            raise OrderError("Out of stock.")
        except OrderError as e:            
            print(e)
    else:
        print("Current Orders:")
        for order_id, product in orders.items():
            print(f"{order_id} - {product}")


while True:
    print("\n1. Place an order")
    print("2. View orders")
    print("3. Exit")
    choice = input("Enter your choice:")
    if choice == "1":
        place_order()
    elif choice == "2":
        view_orders()
    elif choice == "3":
        print("Exiting the order system.")
        break
    else:
        print("Invalid choice. Please enter 1, 2, or 3.")