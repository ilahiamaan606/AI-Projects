class Snack:
    def __init__(self, snack_id, snack_name, price, availability):
        self.snack_id = snack_id
        self.snack_name = snack_name
        self.price = price
        self.availability = availability


class InventoryManagementSystem:
    def __init__(self):
        self.inventory = []
        self.sales_records = []

    def add_snack(self, snack_id, snack_name, price, availability):
        snack = Snack(snack_id, snack_name, price, availability)
        self.inventory.append(snack)
        print("Snack added to inventory.")

    def remove_snack(self, snack_id):
        for snack in self.inventory:
            if snack.snack_id == snack_id:
                self.inventory.remove(snack)
                print("Snack removed from inventory.")
                break
        else:
            print("Snack not found in inventory.")

    def update_snack_availability(self, snack_id, availability):
        for snack in self.inventory:
            if snack.snack_id == snack_id:
                snack.availability = availability
                print("Snack availability updated.")
                break
        else:
            print("Snack not found in inventory.")

    def sell_snack(self, snack_id):
        for snack in self.inventory:
            if snack.snack_id == snack_id:
                if snack.availability == "yes":
                    self.sales_records.append(snack)
                    snack.availability = "no"
                    print("Snack sold.")
                    break
                else:
                    print("Snack is not available.")
                    break
        else:
            print("Snack not found in inventory.")

    def display_inventory(self):
        print("Inventory:")
        for snack in self.inventory:
            print("ID: {}, Name: {}, Price: {}, Availability: {}".format(snack.snack_id,snack.snack_name,snack.price,snack.availability))

    def display_sales_records(self):
        print("Sales Records:")
        for snack in self.sales_records:
            print("ID: {}, Name: {}, Price: {}".format(snack.snack_id,snack.snack_name,snack.price))


# Creating Manual System
system = InventoryManagementSystem()

while True:
    print("\nMenu:")
    print("1. Add a snack to the inventory")
    print("2. Remove a snack from the inventory")
    print("3. Update snack availability")
    print("4. Sell a snack")
    print("5. Display inventory")
    print("6. Display sales records")
    print("0. Exit")
    
    choice = input("Enter your choice (0-6): ")

    if choice == "0":
        break

    elif choice == "1":
        snack_id = input("Enter snack ID: ")
        snack_name = input("Enter snack name: ")
        price = float(input("Enter price: "))
        availability = input("Enter availability (yes/no): ")
        system.add_snack(snack_id, snack_name, price, availability)

    elif choice == "2":
        snack_id = input("Enter snack ID: ")
        system.remove_snack(snack_id)

    elif choice == "3":
        snack_id = input("Enter snack ID: ")
        availability = input("Enter availability (yes/no): ")
        system.update_snack_availability(snack_id, availability)

    elif choice == "4":
        snack_id = input("Enter snack ID: ")
        system.sell_snack(snack_id)

    elif choice == "5":
        system.display_inventory()

    elif choice == "6":
        system.display_sales_records()

    else:
        print("Invalid choice. Please try again.")