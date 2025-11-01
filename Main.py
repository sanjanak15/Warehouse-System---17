# -*- coding: utf-8 -*-
"""
Created on Tue Oct 14 18:43:33 2025

@author: User
"""

from Item import Item
from Location_manager import LocationManager
from Inventory_manager import InventoryManager
from Database_handler import DatabaseHandler
from Report_generator import ReportGenerator


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