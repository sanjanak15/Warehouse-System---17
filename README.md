# Team Members
-K. Sanjana
-P. Beaula
-M. Ashwini
# Warehouse-System---17
## Domain
---------
Supply Chain / Inventory Management

## Problem Statement
---------------------
Warehouses need systems to efficiently manage stock.  
Manual records are error-prone and delay supply chain operations.  

This system allows:
- Managing **items** (ID, name, quantity, location).
- Updating **inventory** on inbound/outbound transactions.
- Tracking **storage locations** (zones/shelves).
- Generating **reports** for items and overall warehouse utilization.
- Using a **menu-driven CLI** for staff operations.

---
## Project Structure
---------------------
warehouse_system/
│
├── item.py              # Define Item class (ID, name, quantity, location)
├── inventory_manager.py # Manage stock (receive/dispatch) & prevent negative stock
├── location_manager.py  # Manage zones/shelves and assign locations
├── database_handler.py  # Simulate storage with dictionaries/files
├── report_generator.py  # Generate item and warehouse reports
├── main.py              # CLI entry point for warehouse staff
├── README.md            # Project overview & student guide
└── instructions.txt     # Step-by-step student instructions

---

## Topics Covered
------------------
- Classes & Objects (OOP)
- Lists & Dictionaries
- Exception Handling
- Reports & Summaries
- Modular Programming
- CLI-based menu navigation

---

## Step-by-Step Workflow
-------------------------
1. Create an **Item class** with attributes for ID, name, quantity, location.  
2. Build an **Inventory Manager** for stock updates.  
3. Add **Location Manager** for managing zones/shelves.  
4. Create a **Database Handler** for storing/retrieving items.  
5. Implement **Report Generator** for summaries.  
6. Write a **menu-driven CLI** in `main.py`.  

---

## Students Work
----------------
- **Student A**: Item (`item.py`) + Location Manager (`location_manager.py`)  
- **Student B**: Inventory Manager (`inventory_manager.py`) + Database Handler (`database_handler.py`)  
- **Student C**: Report Generator (`report_generator.py`) + Main CLI (`main.py`)  

---

## How to run
cd warehouse_system/
python main.py
