# Step 1: Item Class
class Item:
    def __init__(self, item_id, name, quantity, location):
        self.item_id = item_id
        self.name = name
        self.quantity = quantity
        self.location = location

    def __str__(self):  # ✅ double underscores
        return f"Item ID: {self.item_id}, Name: {self.name}, Quantity: {self.quantity}, Location: {self.location}"