"""
Student Grade Manager with @property

Author: Abinash Prasana

This program demonstrates encapsulation using property decorators in Python.
It validates and manages a student's grade, enforcing rules using getters and setters.
"""

class Student:
    def __init__(self, name, grade):
        self.name = name
        self._grade = None  # Initialize the private attribute
        self.grade = grade  # Use the setter for initial validation

    @property
    def grade(self):
        """Getter for the grade attribute."""
        return self._grade

    @grade.setter
    def grade(self, value):
        """Setter for the grade attribute with validation."""
        if not isinstance(value, (int, float)):
            raise TypeError("Grade must be a number.")
        if not 0 <= value <= 100:
            raise ValueError("Grade must be between 0 and 100.")
        self._grade = value

    def __str__(self):
        return f"Student: {self.name}, Grade: {self.grade}"

# Example usage
try:
    student = Student("Abinash", 85)
    print(student)  # Output: Student: Abinash, Grade: 85

    student.grade = 92  # Update grade
    print(student)  # Output: Student: Abinash, Grade: 92

    student.grade = 105  # Attempt to set an invalid grade
except (TypeError, ValueError) as e:
    print(f"Error: {e}")
