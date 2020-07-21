# dict - it maps key value pairs

# d1 = {}
# print(type(d1))

# d2 = {"Harry":"Burger",
#       "Rohan":"Fish",
#       "SkillF":"Roti",
#       "Shubham":{"B":"maggie", "L":"roti", "D":"Chicken"}}

# print(d2)
# print(d2["Rohan"])
# print(d2["Shubham"])
# print(d2["Shubham"]["B"])

# d2["ankit"] = "chiken"
# print(d2)

# d2[402] = "kabab"
# print(d2)

# del d2[420]
# print(d2)

# print(d2.get("Harry"))

# print(d2.update({"sam":"bhindi"}))
# print(d2)

# print(d2.keys())

# print(d2.values())

# print(d2.items())


# Quiz - make dictionary of your bday NOW print it 

d1 = {
"Ankit" : "14-05-1993",
"Sau" : "11.05.1996",
"Dad": "20.05.1962",
"Mum": "25.06.1960"
}
Name = input("Enter your name:\n")

print(d1[Name])