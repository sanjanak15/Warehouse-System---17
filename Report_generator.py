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
        
        