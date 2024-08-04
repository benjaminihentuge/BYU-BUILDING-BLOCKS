people = [
    "Stephanie 36",
    "John 29",
    "Emily 24",
    "Gretchen 54",
    "Noah 12",
    "Penelope 32",
    "Michael 2",
    "Jacob 10"
]

highest_age = 0
lowest_age = 100

for items in people:

    items = items.strip()
    items = items.split(' ')

    name = items[0]
    age = items[1]

    print(name,age)
    age = int(age)

    if age > highest_age:

        highest_age = age
        highest_name = name

    elif age < lowest_age:
        lowest_age = age
        lowest_name = name
        

print(highest_name,highest_age)
print(lowest_name,lowest_age)


    

    