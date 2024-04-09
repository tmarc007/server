name="Tom"
print(name)


def say_hello():
    print("Hello")
    print("I'm inside")

# call the fn
say_hello

# date structures --> 114
# There are 4
# array js --> list in py
prices = [2, 3, 5 ,7] # The numbers are elements in the list
# add to a list. In js it's push; in py we use append
prices.append(9)

# sum all the prices
total = 0
for number in prices:
    total += number

print(total)

# Dictionaries
# Rules: 
me = {
    "name": "Tom",
    "age": 109,
    "hobbie": [],
    "address": {
        "Street": "evergreen",
        "city": "Springfield"
    }
}

print(me)

# read
print(me["name"])

# warning: reading a key that does not exist will break our code
# if(me.index)
if "last" in me:
    print(me["last"])

# modify - to modify age to 99
me["age"] = 99

# add keys - if the key does exist is will be added
me["last"] = "Marcello"


print("The End!!!")






