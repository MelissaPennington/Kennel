class Customer:
    """
    This class represents a customer object.

    Attributes:
        id (int): The customer's unique identifier.
        name (str): The customer's name.
        address (str): The customer's address.
        status (str): The customer's status (e.g., 'active' or 'inactive').
    """

    def __init__(self, id, name, address, status):
        self.id = id
        self.name = name
        self.address = address
        self.status = status

# Creating a new Customer object
new_customer = Customer(1, "John Smith", "8422 Johnson Pike", "active")
