class Dish:
    def __init__(self, dish_id, dish_name, price, availability):
        self.dish_id = dish_id
        self.dish_name = dish_name
        self.price = price
        self.availability = availability


class Order:
    def __init__(self, order_id, customer_name, dishes):
        self.order_id = order_id
        self.customer_name = customer_name
        self.dishes = dishes
        self.status = "received"


class InventorySystem:
    def __init__(self):
        self.menu = {}
        self.orders = {}
        self.next_order_id = 1
        self.order_status_choices = {
            "1": "received",
            "2": "preparing",
            "3": "ready for pickup",
            "4": "delivered"
        }

    def add_dish(self, dish_id, dish_name, price, availability):
        dish = Dish(dish_id, dish_name, price, availability)
        self.menu[dish_id] = dish

    def remove_dish(self, dish_id):
        if dish_id in self.menu:
            del self.menu[dish_id]

    def update_dish_availability(self, dish_id, availability):
        if dish_id in self.menu:
            self.menu[dish_id].availability = availability

    def take_order(self, customer_name, dish_ids):
        dishes = []
        for dish_id in dish_ids:
            if dish_id in self.menu:
                dish = self.menu[dish_id]
                if dish.availability == "yes":
                    dishes.append(dish)
                else:
                    print(f"Dish {dish_id} is not available.")
            else:
                print(f"Dish {dish_id} does not exist.")

        if dishes:
            order_id = self.next_order_id
            order = Order(order_id, customer_name, dishes)
            self.orders[order_id] = order
            self.next_order_id += 1
            print(f"Order {order_id} received for {customer_name}.")

    def update_order_status(self, order_id, status):
        if order_id in self.orders:
            self.orders[order_id].status = status
            print(f"Order {order_id} status updated: {status}.")
            if status == "delivered":
                self.save_completed_order(order_id)
        else:
            print(f"Order {order_id} does not exist.")

    def review_orders(self):
        for order_id, order in self.orders.items():
            print(f"Order ID: {order.order_id}")
            print(f"Customer Name: {order.customer_name}")
            print("Dishes:")
            for dish in order.dishes:
                print(f" - {dish.dish_name}")
            print(f"Status: {order.status}")
            print()

    def save_completed_order(self, order_id):
        order = self.orders.get(order_id)
        if order:
            file_path = "completedOrders.txt"
            with open(file_path, "a") as file:
                file.write("Order ID: {}\n".format(order.order_id))
                file.write("Customer Name: {}\n".format(order.customer_name))
                file.write("Dishes:\n")
                total_bill = 0
                for dish in order.dishes:
                    file.write(" - {}: ₹{}\n".format(dish.dish_name, dish.price))
                    total_bill += dish.price
                file.write("Total Bill: ₹{}\n".format(total_bill))
                file.write("\n")
            print("Order {} data saved to completedOrders.txt.".format(order.order_id))
        else:
            print("Order {} does not exist.".format(order_id))

    def check_inventory(self):
        print("Menu Inventory:")
        for dish_id, dish in self.menu.items():
            print(f"Dish ID: {dish.dish_id}")
            print(f"Dish Name: {dish.dish_name}")
            print(f"Price: {dish.price}")
            print(f"Availability: {dish.availability}")
            print()

    def check_sales_list(self):
        print("Sales List:")
        for order_id, order in self.orders.items():
            print(f"Order ID: {order.order_id}")
            print(f"Customer Name: {order.customer_name}")
            print("Dishes:")
            for dish in order.dishes:
                print(f" - {dish.dish_name}")
            print(f"Status: {order.status}")
            print()

    def total_sales(self):
        total = 0
        for order_id, order in self.orders.items():
            for dish in order.dishes:
                total += dish.price
        return total

    def run(self):
        while True:
            print("\n----- Zesty Zomato Menu and Order Management System -----")
            print("1. Add a dish to the menu")
            print("2. Remove a dish from the menu")
            print("3. Update dish availability")
            print("4. Take a new order")
            print("5. Update order status")
            print("6. Review all orders")
            print("7. Check inventory")
            print("8. Check sales list")
            print("9. Total sales")
            print("10. Exit")

            choice = input("Enter your choice: ")

            if choice == "1":
                dish_id = input("Enter dish ID: ")
                dish_name = input("Enter dish name: ")
                price = float(input("Enter dish price: "))
                availability = input("Enter dish availability (yes/no): ")
                self.add_dish(dish_id, dish_name, price, availability)
                print("Dish added to the menu.")
            elif choice == "2":
                dish_id = input("Enter dish ID to remove: ")
                self.remove_dish(dish_id)
                print("Dish removed from the menu.")
            elif choice == "3":
                dish_id = input("Enter dish ID to update availability: ")
                availability = input("Enter new availability (yes/no): ")
                self.update_dish_availability(dish_id, availability)
                print("Dish availability updated.")
            elif choice == "4":
                customer_name = input("Enter customer name: ")
                dish_ids = input("Enter dish IDs (separated by space): ").split()
                self.take_order(customer_name, dish_ids)
            elif choice == "5":
                order_id = int(input("Enter order ID to update status: "))
                print("Order status choices:")
                for key, value in self.order_status_choices.items():
                    print(f"{key}. {value}")
                status_choice = input("Enter status choice number: ")
                if status_choice in self.order_status_choices:
                    status = self.order_status_choices[status_choice]
                    self.update_order_status(order_id, status)
                else:
                    print("Invalid status choice.")
            elif choice == "6":
                self.review_orders()
            elif choice == "7":
                self.check_inventory()
            elif choice == "8":
                self.check_sales_list()
            elif choice == "9":
                total = self.total_sales()
                print(f"Total Sales: {total}")
            elif choice == "10":
                print("Exiting the system...")
                break
            else:
                print("Invalid choice. Please try again.")



inventory_system = InventorySystem()
inventory_system.run()