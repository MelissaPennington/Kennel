class Animal:
    """
    This class represents an animal object.

    Attributes:
        id (int): The unique identifier for the animal.
        name (str): The name of the animal.
        breed (str): The breed or species of the animal.
        status (str): The status of the animal (e.g., 'Recreation', 'Active', etc.).
        location_id (int): The identifier of the location where the animal is kept.
        customer_id (int): The identifier of the customer who owns the animal.
    """

    def __init__(self, id, name, breed, status, location_id, customer_id):
        self.id = id
        self.name = name
        self.breed = breed
        self.status = status
        self.location_id = location_id
        self.customer_id = customer_id

# Creating a new Animal object
new_animal = Animal(1, "Snickers", "Dog", "Recreation", 1, 4)
