import csv

anime = input("Whats is your anime? ")
description = input("Where's your description? ")


with open("exercice.csv", "a") as file:
    writer = csv.DictWriter(file, fieldnames=["anime", "description"])
    writer.writerow({"anime": anime, "description": description})

animes = []

with open("exercice.csv") as file:
    reader = csv.DictReader(file)
    for row in reader:
        animes.append({"anime": row["anime"], "description": row["description"]})

for anime in sorted(animes, key=lambda anime: anime["anime"]):
    print(f"{anime['anime']} is a {anime['description']}")
