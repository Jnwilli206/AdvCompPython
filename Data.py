tuple1 = ("Dog", "Cat", "Lizard", "Hamster", "Parrot", "Spider", "Snake", "Mouse", "Fish", "Turtle")
list1 = ["Turtle", "Fish", "Mouse", "Snake", "Spider", "Parrot", "Hamster", "Lizard", "Cat", "Dog"]
print("The third element is", tuple1[2])
print("The third element it", list1[2])

set1 = {"a", "b"}
for x in tuple1:
    set1.add(x)
set1.remove("a")
set1.remove("b")
print("The tuple randomized is", set1)

set2 = {"a", "b"}
for x in list1:
    set2.add(x)
set2.remove("a")
set2.remove("b")
print("The list randomized is", set2)

list1.append("Fox")
print("Look I added a fox", list1)

list2 = []
for x in tuple1:
    list2.append(x)
list2.append("Squirrel")
print("And for this one I added a squirrel", list2)

list1.remove("Cat")
list2.remove("Cat")
print("And now I've remove cat from both", list1)
print("Because I'm allergic", list2)