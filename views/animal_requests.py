import sqlite3
import json
from models import Animal
from models import Location

ANIMALS = [
    {
        "id": 1,
        "name": "Elle",
        "status": "Admitted",
        "breed": "Dog",
        "customer_id": 4,
        "location_id": 1
    },
    {
        "id": 2,
        "name": "Elf",
        "status": "Admitted",
        "breed": "Fox",
        "customer_id": 2,
        "location_id": 2
    },
]

# Convert the list of Animal instances to a JSON string
json_data = json.dumps(ANIMALS)

# Now, json_data contains a JSON representation of your Animal instances
print(json_data)

def get_all_animals():
    """gets all animals."""
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
            a.breed,
            a.status,
            a.location_id,
            a.customer_id,
            l.name AS location_name,
            l.address AS location_address
        FROM Animal a
        JOIN Location l
        ON l.id = a.location_id
            """)

        # Initialize an empty list to hold all animal representations
        animals = []

        # Convert rows of data into a Python list
        dataset = db_cursor.fetchall()

        # Iterate list of data returned from database
        for row in dataset:

    # Create an animal instance from the current row
            animal = Animal(row['id'], row['name'], row['breed'], row['status'],
                    row['location_id'], row['customer_id'])

    # Create a Location instance from the current row
            location = Location(row['id'], row['location_name'], row['location_address'])

    # Add the dictionary representation of the location to the animal
            animal.location = location.__dict__

    # Add the dictionary representation of the animal to the list
    animals.append(animal.__dict__)

    return animals

def get_single_animal(id):
    """return a single animal."""
    with sqlite3.connect("./kennel.sqlite3") as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        # Use a ? parameter to inject a variable's value
        # into the SQL statement.
        db_cursor.execute("""
        SELECT
            a.id,
            a.name,
            a.breed,
            a.status,
            a.location_id,
            a.customer_id
        FROM animal a
        WHERE a.id = ?
        """, ( id, ))

        # Load the single result into memory
        data = db_cursor.fetchone()

        # Create an animal instance from the current row
        animal = Animal(data['id'], data['name'], data['breed'],
                            data['status'], data['location_id'],
                            data['customer_id'])

        return animal.__dict__

def create_animal(animal):
    """Function to create animals."""
    # Get the id value of the last animal in the list
    max_id = ANIMALS[-1]["id"]

    # Add 1 to whatever that number is
    new_id = max_id + 1

    # Add an `id` property to the animal dictionary
    animal["id"] = new_id

    # Add the animal dictionary to the list
    ANIMALS.append(animal)

    # Return the dictionary with `id` property added
    return animal

def delete_animal(id):
    """delete item"""
    with sqlite3.connect("./kennel.sqlite3") as conn:
        db_cursor = conn.cursor()

        db_cursor.execute("""
        DELETE FROM animal
        WHERE id = ?
        """, (id, ))

def update_animal(id, new_animal):
    """update item"""
    with sqlite3.connect("./kennel.sqlite3") as conn:
        db_cursor = conn.cursor()

        db_cursor.execute("""
        UPDATE Animal
            SET
                name = ?,
                breed = ?,
                status = ?,
                location_id = ?,
                customer_id = ?
        WHERE id = ?
        """, (new_animal['name'], new_animal['breed'],
              new_animal['status'], new_animal['locationId'],
              new_animal['customerId'], id, ))

        # Were any rows affected?
        # Did the client send an `id` that exists?
        rows_affected = db_cursor.rowcount

    # return value of this function
    if rows_affected == 0:
        # Forces 404 response by main module
        return False
    else:
        # Forces 204 response by main module
        return True

def get_animals_by_location(location_id):
    """Return animals by location."""
    with sqlite3.connect("./kennel.sqlite3") as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        db_cursor.execute("""
        SELECT
            a.id,
            a.name,
            a.breed,
            a.status,
            a.location_id,
            a.customer_id
        FROM animal a
        WHERE a.location_id = ?
        """, (location_id, ))
        animals = []
        dataset = db_cursor.fetchall()

        for row in dataset:
            animal = Animal(row['id'], row['name'], row['breed'],
                            row['status'], row['location_id'],
                            row['customer_id'])
            animals.append(animal.__dict__)

    return animals

def get_animals_by_status(status):
    """Return animals by status."""
    with sqlite3.connect("./kennel.sqlite3") as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        db_cursor.execute("""
        SELECT
            a.id,
            a.name,
            a.breed,
            a.status,
            a.location_id,
            a.customer_id,
            l.name location_name,
            l.address location_address
        FROM Animal a
        JOIN Location l
            ON l.id = a.location_id
        """, (status, ))
        animals = []
        dataset = db_cursor.fetchall()

    for row in dataset:

        # Create an animal instance from the current row
        animal = Animal(row['id'], row['name'], row['breed'], row['status'],
                        row['location_id'], row['customer_id'])

        # Create a Location instance from the current row
        location = Location(row['id'], row['location_name'], row['location_address'])

        # Add the dictionary representation of the location to the animal
        animal.location = location.__dict__

        # Add the dictionary representation of the animal to the list
        animals.append(animal.__dict__)

    return animals
