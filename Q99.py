class Employee:
    def __init__(self, name, salary):
        self.name = name
        self._salary = salary

    @property
    def salary(self):
        return self._salary

    @salary.setter
    def salary(self, value):
        if value >= 0:
            self._salary = value
        else:
            raise ValueError("Salary cannot be negative.")

employee = Employee("John", 5000)
print(f"Salary: {employee.salary}")
employee.salary = 6000
print(f"Updated Salary: {employee.salary}")
