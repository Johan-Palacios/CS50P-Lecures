class Wizard(object):
    def __init__(self, name):
        if not name:
            raise ValueError("Missing Name")


class Student(Wizard):
    def __init__(self, name, house):
        super().__init__(name)
        self.house = house

    ...


class Professor(Wizard):
    def __init__(self, name, subject):
        super().__init__(name)
        self.subject = subject

    ...


student = Student("Harry", "Mansion")
wizard = Wizard("Magic")
professor = Professor("Severus", "CS")
