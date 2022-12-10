# def main():
#     yell("This", "is", "CS50")


# def yell(*args: str):
#     # Map
#     # upercased = map(str.upper, args)
#     # List comprehension
#     upercased = [word.upper() for word in args]
#     print(*upercased)


# if __name__ == "__main__":
#     main()

# characters = ["Emilia", "Rem", "Ram", "Arakia", "Pricila"]


# # Dict comprehension
# places = [{"name": character, "place": "Lugunica"} for character in characters]
# places2 = {character: "Emilia" for character in characters}

# print(places)
# print(places2)

characters = ["Emilia", "Rem", "Ram", "Arakia", "Pricila"]

for i, character in enumerate(characters):
    print(i+1, character)
