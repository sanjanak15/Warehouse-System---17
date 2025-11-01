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
