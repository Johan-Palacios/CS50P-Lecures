# students = {
#     "Johan": "Palacios", 
#     "Emilia": "Re:Zero", 
#     "Rem": "Re:Zero", 
#     "Roxy": "Migurdia"
# }
#
# for student in students:
#     print(student, students[student], sep=", ")

students = [
    {"name":"Johan", "house": "Huehuetenango", "patronus": None},
    {"name":"Rem", "house": "Lugunica", "patronus": "Roswald"},
    {"name":"Emilia", "house": "Luginica", "patronus": "Roswald"}
]

for student in students:
    print(student["name"], student["house"], student["patronus"])
