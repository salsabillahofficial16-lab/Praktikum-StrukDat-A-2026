x = "Hello dunia!"
print(len(x))

mytuple = ("green", "yellow", "blue")
print(len(mytuple))

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1999
}

print(len(thisdict))

class animals:
    def __init__(self, name):
        self.name = name
    def sound(self):
        print("sound")

class cat(animals):
    def sound(self):
        print("Meeouww")

class dog(animals):
    def sound(self):
        print("Woof")

cat1 = cat("lyly")
dog1 = dog("bobby")

for x in (cat1, dog1):
 print(x.name)
 x.sound()


