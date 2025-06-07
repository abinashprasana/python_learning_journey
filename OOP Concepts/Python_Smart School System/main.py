# Base class
class Person:
    def __init__(self, name):
        self.name = name

    def show_name(self):
        print(f"Name: {self.name}")

# 1. Single Inheritance: Student inherits from Person
class Student(Person):
    def __init__(self, name, student_id):
        super().__init__(name)
        self.student_id = student_id

    def show_student(self):
        print(f"Student ID: {self.student_id}")

# 2. Multilevel Inheritance: Person -> Teacher -> HeadTeacher
class Teacher(Person):
    def __init__(self, name, subject):
        super().__init__(name)
        self.subject = subject

    def show_teacher(self):
        print(f"Teaches: {self.subject}")

class HeadTeacher(Teacher):
    def __init__(self, name, subject, experience):
        super().__init__(name, subject)
        self.experience = experience

    def show_head(self):
        print(f"Experience: {self.experience} years")

# 3. Multiple Inheritance: Sports & Music both provide roles
class Sports:
    def sport_role(self):
        print("Handles sports events")

class Music:
    def music_role(self):
        print("Manages music club")

class ActivityManager(Sports, Music):  # Multiple
    def role(self):
        print("Activity Manager Roles:")
        self.sport_role()
        self.music_role()

# 4. Hierarchical Inheritance: Admin and Librarian from Staff
class Staff:
    def work(self):
        print("General staff duties")

class Admin(Staff):
    def duty(self):
        print("Admin work")

class Librarian(Staff):
    def duty(self):
        print("Library management")

# 5. Hybrid Inheritance: AssistantProfessor inherits from both Teacher & Researcher
class Researcher:
    def __init__(self, field):
        self.field = field

    def show_research(self):
        print(f"Research Field: {self.field}")

class AssistantProfessor(Teacher, Researcher):  # Hybrid (Multilevel + Multiple)
    def __init__(self, name, subject, field):
        Teacher.__init__(self, name, subject)
        Researcher.__init__(self, field)

    def show_info(self):
        self.show_name()
        self.show_teacher()
        self.show_research()
# 1. Single
s = Student("Abinash", "S001")
s.show_name()
s.show_student()

# 2. Multilevel
h = HeadTeacher("Dr. Smith", "Physics", 15)
h.show_name()
h.show_teacher()
h.show_head()

# 3. Multiple
a = ActivityManager()
a.role()

# 4. Hierarchical
ad = Admin()
lib = Librarian()
ad.work()
ad.duty()
lib.work()
lib.duty()

# 5. Hybrid
ap = AssistantProfessor("Mr. John", "Chemistry", "Organic Compounds")
ap.show_info()
