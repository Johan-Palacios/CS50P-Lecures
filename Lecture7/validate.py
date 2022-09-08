import re

email = input("Whats is oyour email? ").strip()


# . cualquier caracter menos una nueva linea
# * cualquier caracters incluido nada
# + más de un caracter
# ^ marca el inicio de un string
# $ marca el finall de un string
# ? 0 o 1 repeticion
# {m} m repeticiones
# {m-n} m-n repeticiones
# [] conjunto de caracteres
# [^] el opuesto del conjunto /los caracteres que se desean exluir caracteres


# CHARACTER CLASSES
# \d decimal digit
# \D not decimal digit
# \s whitespace characters
# \S not a whitespace character
# \w word characters as well numbers and the underscore
# \W not a word character


# GRUPOS
# A| B
# (...) a group
# (?:...) non-capturing version

if re.search(r"^\w+@(\w+\.)*\w+\.edu$", email, re.IGNORECASE):
    print("valid")
else:
    print("invalid")
