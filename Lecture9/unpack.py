# def total(galleons, sickels, knuts):
#     return (galleons * 17 + sickels) * 29 + knuts


# coins = {"galleons": 100, "sickels": 50, "knuts": 25}
# coins2 = [100, 50, 25]
# # Lists
# print(total(*coins2), "Knuts")
# # For dictionary
# print(total(**coins), "Knuts")


def f(*args, **kwargs):
    print("Positinal", args)
    print("Named: ", kwargs)


f(100,2,3)
f(test1=100, test2=2, test3=100)
