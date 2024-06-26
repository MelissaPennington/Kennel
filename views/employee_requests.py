import sqlite3
import json
from models import Employee

EMPLOYEES = [
  {
    "id": 1,
    "name": "Emma Beaton",
    "address": "54 Sycamore Avenue",
    "location_id": 2,
  },
  {
    "id": 2,
    "name": "Emma Bea",
    "address": "54 Sycamore Ave",
    "location_id": 2,
  },
  {
    "id": 3,
    "name": "E. Beaton",
    "address": "54 Sycamore Avenue",
    "location_id": 2,
  }
]
# Convert the list of Animal instances to a JSON string
json_data = json.dumps(EMPLOYEES)

# Now, json_data contains a JSON representation of your Animal instances
print(json_data)

def get_all_employees():
    """gets all employees."""
    # Open a connection to the database
    with sqlite3.connect("./kennel.sqlite3") as conn:

        # Just use these. It's a Black Box.
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        # Write the SQL query to get the information you want
        db_cursor.execute("""
        SELECT
            a.id,
            a.name,
            a.address,
            a.location_id
        FROM employee a
        """)

        # Initialize an empty list to hold all animal representations
        employees = []

        # Convert rows of data into a Python list
        dataset = db_cursor.fetchall()

        # Iterate list of data returned from database
        for row in dataset:

            # Create an animal instance from the current row.
            # Note that the database fields are specified in
            # exact order of the parameters defined in the
            # Animal class above.
            employee = Employee(row['id'], row['name'], row['address'],
                            row['location_id'])

            employees.append(employee.__dict__)
            # see the notes below for an explanation on this line of code.

    return employees

def get_single_employee(id):
    """return a single employee."""
    with sqlite3.connect("./kennel.sqlite3") as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        # Use a ? parameter to inject a variable's value
        # into the SQL statement.
        db_cursor.execute("""
        SELECT
            a.id,
            a.name,
            a.address,
            a.location_id
        FROM employee a
        WHERE a.id = ?
        """, ( id, ))

        # Load the single result into memory
        data = db_cursor.fetchone()

        # Create an animal instance from the current row
        employee = Employee(data['id'], data['name'], data['address'],
                            data['location_id'])

        return employee.__dict__
def create_employee(employee):
    """Creates new employee."""
    # Get the id value of the last animal in the list
    max_id = EMPLOYEES[-1]["id"]

    # Add 1 to whatever that number is
    new_id = max_id + 1

    # Add an `id` property to the animal dictionary
    employee["id"] = new_id

    # Add the animal dictionary to the list
    EMPLOYEES.append(employee)

    # Return the dictionary with `id` property added
    return employee

def delete_employee(id):
    """Delete employee."""
    with sqlite3.connect("./kennel.sqlite3") as conn:
        db_cursor = conn.cursor()

        db_cursor.execute("""
        DELETE FROM employee
        WHERE id = ?
        """, (id, ))

def update_employee(id, new_employee):
    """update item"""
    # Iterate the ANIMALS list, but use enumerate() so that
    # you can access the index value of each item.
    for index, employee in enumerate(EMPLOYEES):
        if employee["id"] == id:
            # Found the animal. Update the value.
            EMPLOYEES[index] = new_employee
            break

def get_employees_by_location(location_id):
    """Return employees by location."""
    with sqlite3.connect("./kennel.sqlite3") as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        db_cursor.execute("""
        SELECT
            a.id,
            a.name,
            a.address,
            a.location_id
        FROM employee a
        WHERE a.location_id = ?
        """, (location_id, ))
        employees = []
        dataset = db_cursor.fetchall()

        for row in dataset:
            employee = Employee(row['id'], row['name'], row['address'], row['location_id'],)
            employees.append(employee.__dict__)

    return employees
