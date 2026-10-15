# Week 1.3, Session 1: For loop equivalent to a list comprehension

animals = ['dog','cat','hamster','goldfish']

not_fish = [item for item in animals if item != 'goldfish']

print(not_fish)


# write the equivalent for loop to create the not_fish list from animals
not_fish2 = []
for i in animals:
    if i != 'goldfish':
        not_fish2.append(i)

# print your result to verify it is the same
print(not_fish)
print(not_fish2)