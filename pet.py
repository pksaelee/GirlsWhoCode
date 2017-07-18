#CLASSES
class Pet:
    def __init__(self,name,age,color):
        self.name = name
        self.age = age
        self.color = color
class Dog(Pet):
    def __init__(self,name,age,color,breed,attitude):
        self.breed = breed
        self.attitude = attitude
        Pet.__init__(self,name,age,color)
        self.adopted = False
    def getName(self):
        return self.name
    def speak(self):
        print("Woof!")
    def isAdopted(self):
        return self.adopted
    def setAdopted(self,adopt):
        self.adopted = adopt
    def bio(self):
        print(self.name + " is a " + self.age+ " year old " + self.color + " "
              + self.breed + " who is " + self.attitude + "!")
class SeaAnimal(Pet):
    def __init__(self,name,age,color,breed,talent):
        self.breed = breed
        self.talent = talent
        Pet.__init__(self,name,age,color)
        self.adopted = False
    def getSelf(self):
        return(self.name)
    def isAdopted(self):
        return self.adopted
    def setAdopted(self,adopt):
        self.adopted = adopt
    def bio(self):
        print(self.name + " is a " + self.age+ " year old " + self.color + " "
              + self.breed + " who has a cool talent!")
        print("Do you want to see " + self.name+"'s talent? y/n")
        ans = input()
        if ans == "y":
            print(self.name +" "+ self.talent)
            print("Cool!")
            print()
        if ans == "n":
            print("Ok, next animal then.")
            print()



#RUNNING CODE
spot = Dog("Spot","2","black and white","Terrier","friendly")
fred = Dog("Fred", "1","brown","Boxer","sassy")
clifford = Dog("Clifford","3","red","Bid Red Dog","nice")
storm = Dog("Storm","2","white","Husky","hyper")

dogs = [spot,fred,clifford,storm]

zack = SeaAnimal("Zack","8","purple","Guppy Fish","plays dead!")
gina = SeaAnimal("Gina","50","brown","Tortoise","runs!")
siz = SeaAnimal("Siz","1","pink","Big-belly Seahorse","jumps out of the water!")
buddy = SeaAnimal("Buddy", "3","orange","Goldfish","also plays dead...oh no he's actually dead! Let's make a grave for him before we move on...")

seaanimals = [zack,gina,siz,buddy]

print("Welcome to the Girls Who Code Animal Shelter!")
print("Let me introduce you to our dogs first.")
for each in dogs:
    each.speak()
    print("That's " + each.getName())
    each.bio()
print()
print("Next, let me introduce you to our sea animals.")
for other in seaanimals:
    print("This is " + other.getSelf())
    other.bio()
