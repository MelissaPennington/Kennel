class Employee:
    """
    This class represents an employee object.

    Attributes:
        id (int): The unique identifier for the employee.
        name (str): The name of the employee.
        address (str): The address of the employee.
        status (str): The employment status of the employee (e.g., 'active' or 'inactive').
    """

    def __init__(self, id, name, address, status):
        self.id = id
        self.name = name
        self.address = address
        self.status = status

# Creating a new Employee object
new_employee = Employee(1, "John Smith", "8422 Johnson Pike", "active")
