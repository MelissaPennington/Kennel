class Employee:
    """This class represents an employee object.

    Attributes:
        id (int): The unique identifier for the employee.
        name (str): The name of the employee.
        address (str): The address of the employee.
        locqation_id (int): The employees location.
    """

    def __init__(self, id, name, address, location_id):
        self.id = id
        self.name = name
        self.address = address
        self.location_id = location_id

# Creating a new Employee object
new_employee = Employee(1, "John Smith", "8422 Johnson Pike", 2)
