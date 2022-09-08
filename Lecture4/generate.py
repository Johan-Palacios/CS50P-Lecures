from random import shuffle

# coin = choice(["Emilia", "Roxy", "Rem", "Rias Gremory"])
# print(coin)

# number = randint(1, 10)
# print(number)

cards = ["Emilia", "Rem", "Rias Gremory"]

shuffle(cards)

for card in cards:
    print(card)
