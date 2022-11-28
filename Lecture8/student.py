class Student:
    def __init__(self, name, house):
        self.name = name
        self.house = house

    # Getter
    @property
    def house(self):
        return self._house

    # Setter
    @house.setter
    def house(self, house):
        if house not in ["guatemala", "Huehuetenango"]:
            raise ValueError("Invalid House")
        self._house = house

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        if not name:
            raise ValueError("Missing name")
        self._name = name

    def __str__(self):
        return f"{self.name} from {self.house}"
    
    @classmethod
    def get(cls):
        name = input("Name: ")
        house = input("House: ")
        return cls(name, house)

def main():
    student = Student.get()
    print(f"{student.name} from {student.house}")


if __name__ == "__main__":
    main()
