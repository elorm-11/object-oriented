class parrot:

    species = "poodle"
    species2 = "BULLDOG"
    species3 = "dog"

    def __init__(self, name,age):
      self.name = name
      self.age = age

blu = parrot("blu", 10)
woo = parrot("woo", 15)

print("blu is a {}".format(blu.species3))
print("woo is also a {}".format( woo.species3))

print("{} is {} but".format( blu.name, blu.species))
print("{} is {} ".format( woo.name, woo.species2))

print("{} is {} years old".format( blu.name, blu.age))
print("{} is {} years old".format( woo.name, woo.age))