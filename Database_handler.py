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