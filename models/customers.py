class Customer:
    """
    This class represents a customer object.

    Attributes:
        id (int): The customer's unique identifier.
        name (str): The customer's name.
        address (str): The customer's address.
        email (str): The customer's email address.
        password (str): The customer's password.
    """

    def __init__(self, id, name, address, email, password):
        self.id = id
        self.name = name
        self.address = address
        self.email = email
        self.password = password

# Creating a new Customer object
new_customer = Customer(1, "John Smith", "8422 Johnson Pike", "jsmith@email.com", "password")
