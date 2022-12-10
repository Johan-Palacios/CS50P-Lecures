students = [
    {"name": "Rem", "house": "Lugunica"},
    {"name": "Emilia", "house": "Lugunica"},
    {"name": "ArakiArakia", "house": "Volachia"},
]

houses = set()

for student in students:
    houses.add(student["house"])

for house in sorted(houses):
    print(house)
