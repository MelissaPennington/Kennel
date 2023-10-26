class Location:
    """
    This class represents a location object.

    Attributes:
        id (int): The unique identifier for the location.
        name (str): The name of the location.
        address (str): The address of the location.
    """

    def __init__(self, id, name, address):
        self.id = id
        self.name = name
        self.address = address

# Creating a new Location object
new_location = Location(1, "Jon Williams", "8422 Johnson Pike")
