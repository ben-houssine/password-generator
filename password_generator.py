import string
import random

## all characters
characters = list(string.ascii_letters + string.digits + "!@#$%^&*()_-")

## length of the password
char1 = []
char2 = []
char3 = []
char4 = []
char5 = []
char6 = []
char7 = []
char8 = []
char9 = []
char10 = []

## every char, only gets on random char from "characters"
char1.append(random.choice(characters))
char2.append(random.choice(characters))
char3.append(random.choice(characters))
char4.append(random.choice(characters))
char5.append(random.choice(characters))
char6.append(random.choice(characters))
char7.append(random.choice(characters))
char8.append(random.choice(characters))
char9.append(random.choice(characters))
char10.append(random.choice(characters))

## now combine it all together to a single varaible
combine_all_char = char1 + char2 + char3 + char4 + char5 +char6 + char7 + char8 + char9 + char10

## join it together without the "" in between
password = "".join(combine_all_char)

##output to the console
print("pasword:", password)



## crated 12.02.2022
## by Mr. Youssef Ben Houssine
## https://github.com/ben-houssine