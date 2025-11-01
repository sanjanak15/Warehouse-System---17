# -*- coding: utf-8 -*-
"""
Created on Sun Oct 12 21:27:56 2025

@author: User
"""

# Step 1: Item Class
class Item:
    def __init__(self, item_id, name, quantity, location):
        self.item_id = item_id
        self.name = name
        self.quantity = quantity
        self.location = location

    def __str__(self):  # ✅ double underscores
        return f"Item ID: {self.item_id}, Name: {self.name}, Quantity: {self.quantity}, Location: {self.location}"


# Step 2: InventoryManager Class
class InventoryManager:
    def __init__(self):
        # Dictionary to store items: {item_id: ItemObject}
        self.items = {}

    def add_item(self, item):
        """Add a new item to inventory."""
        # HINT: Check if item_id already exists; if not, add item
        if item.item_id in self.items:
            print("⚠️ Item already exists! Use 'Receive Stock' instead.")
        else:
            self.items[item.item_id] = item
            print("✅ Item added successfully!")

    def receive_stock(self, item_id, qty):
        """Increase stock for an item (inbound)."""
        # HINT: Find the item and add qty; handle KeyError if item_id not found
        if item_id in self.items:
            self.items[item_id].quantity += qty
            print(f"📦 Received {qty} units. New quantity: {self.items[item_id].quantity}")
        else:
            print("❌ Item not found in inventory!")

    def dispatch_stock(self, item_id, qty):
        """Decrease stock for an item (outbound), prevent negative."""
        # HINT: Check if enough stock exists before reducing
        if item_id in self.items:
            if self.items[item_id].quantity >= qty:
                self.items[item_id].quantity -= qty
                print(f"🚚 Dispatched {qty} units. Remaining: {self.items[item_id].quantity}")
            else:
                print("⚠️ Not enough stock to dispatch!")
        else:
            print("❌ Item not found in inventory!")


# Step 3: LocationManager Class
class LocationManager:
    def __init__(self):
        self.locations = {}

    def add_zone(self, zone_name, shelves):
        """Add a zone with shelves."""
        self.locations[zone_name] = shelves

    def is_valid_location(self, location):
        """Check if a location exists in the warehouse."""
        for shelves in self.locations.values():
            if location in shelves:
                return True
        return False


# Step 4: DatabaseHandler Class
class DatabaseHandler:
    def __init__(self):
        """Storage as dictionary {item_id: ItemObject}"""
        self.storage = {}

    def save_item(self, item):
        """Save or update an item in storage."""
        self.storage[item.item_id] = item

    def get_item(self, item_id):
        """Retrieve an item by ID."""
        return self.storage.get(item_id)

    def get_all_items(self):
        """Retrieve all items."""
        return list(self.storage.values())


# Step 5: ReportGenerator Class
class ReportGenerator:
    def __init__(self, database_handler):
        self.db = database_handler

    def generate_item_report(self):
        """Print report of all items."""
        items = self.db.get_all_items()
        if not items:
            print("No items found in inventory.")
        else:
            print("\n📋 Inventory Report:")
            for item in items:
                print(f"{item.item_id} - {item.name} ({item.quantity}) @ {item.location}")

    def generate_summary(self):
        """Generate warehouse summary: total items, total stock."""
        items = self.db.get_all_items()
        total_items = len(items)
        total_quantity = sum(item.quantity for item in items)
        print("\n🏭 Warehouse Summary:")
        print(f"Total item types: {total_items}")
        print(f"Total quantity of all items: {total_quantity}")


# Step 6: Main CLI
def main():
    db = DatabaseHandler()
    inventory = InventoryManager()
    reports = ReportGenerator(db)
    locations = LocationManager()

    # Example predefined zones
    locations.add_zone("Z1", ["S1", "S2"])
    locations.add_zone("Z2", ["S3", "S4"])

    while True:
        print("\n===================================")
        print("   🏭 Warehouse Management System  ")
        print("===================================")
        print("1. Add Item")
        print("2. Receive Stock")
        print("3. Dispatch Stock")
        print("4. View Inventory Report")
        print("5. View Summary Report")
        print("6. Exit")
        print("===================================")

        choice = input("Enter your choice: ")

        if choice == "1":
            item_id = input("Enter item ID: ")
            name = input("Enter item name: ")
            quantity = int(input("Enter quantity: "))
            location = input("Enter location: ")
            if locations.is_valid_location(location):
                item = Item(item_id, name, quantity, location)
                inventory.add_item(item)
                db.save_item(item)
            else:
                print("❌ Invalid location!")

        elif choice == "2":
            item_id = input("Enter item ID: ")
            quantity = int(input("Enter quantity to receive: "))
            inventory.receive_stock(item_id, quantity)

        elif choice == "3":
            item_id = input("Enter item ID: ")
            quantity = int(input("Enter quantity to dispatch: "))
            inventory.dispatch_stock(item_id, quantity)

        elif choice == "4":
            reports.generate_item_report()

        elif choice == "5":
            reports.generate_summary()

        elif choice == "6":
            print("👋 Exiting Warehouse Management System. Goodbye!")
            break

        else:
            print("❌ Invalid choice. Please try again.")


if __name__ == "__main__":
    main()

