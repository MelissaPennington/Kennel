class Location:
    """
    This class represents a location object.

    Attributes:
        id (int): The unique identifier for the location.
        address (str): The address of the location.
    """

    def __init__(self, id, address):
        self.id = id
        self.address = address

# Creating a new Location object
new_location = Location(1, "8422 Johnson Pike")
