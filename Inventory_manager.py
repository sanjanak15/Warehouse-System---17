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