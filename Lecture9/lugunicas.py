students = [
    {"name": "Rem", "house": "Lugunica"},
    {"name": "Emilia", "house": "Lugunica"},
    {"name": "Arakia", "house": "Volachia"},
    {"name": "Yorna", "house": "Volachia"},
]

# List comprehesion with condicionals
# luginicas = [student["name"] for student in students if student["house"] == "Lugunica"]

# for lugunica in sorted(luginicas):
#     print(lugunica)


# Improved
def is_lugunica(s: dict):
    return s["house"] == "Lugunica"


# Filter
lugunicas = filter(is_lugunica, students)

for lugunica in sorted(lugunicas, key=lambda s: s["name"]):
    print(lugunica["name"])
