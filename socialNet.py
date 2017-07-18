#CLASSES
class User:
    def __init__(self,name,ID,connections):
        self.name = name
        self.ID = ID
        self.connections = connections
    def getName(self):
        return self.name
    def getID(self):
        return self.ID
    def getConnection(self):
        return self.connections
    def setName(self,newName):
        self.name = newName

class Network:
    def __init__(User):
        listUsers = []
            
        
#def main(self):
    #u = User()
    #n = Network()
    #n.addUser(u)
    #n.printUsers()
    
    
#FUNCTION
u1 = User("Dana Baltazar","danabaltazar","Jessica")
u2 = User("Precious Saelee","pksaelee","Jessica")

users = [u1,u2]

print("Enter ID:")
name = input()
print("Welcome, %s. Would you like to see your connections? y/n" %name)
yn = input()
while True:
    if yn =="y":
        for each in users:
            print("Name: " + each.getName())
            print("ID: " + each.getID())
            print("Connections: " + each.getConnection())
            print()
        break
    elif (yn == 'n'):
        break
    else:
        print("Please enter y or n.")
while True:
    print("Do you want to add connections? y/n")
    ans = input()
    if ans == "y":
        print("Enter name:")
        users.append("Name: ")
        n = input()
        users.append(n)
        print("Enter ID:")
        users.append("ID: ")
        u = input()
        users.append(u)
        print("Enter connection:")
        users.append("Connections: ")
        c = input()
        users.append(c)
        print("Connections saved.")
        break  
    elif ans == "n":
        break
    else:
        print("Please enter y or n.")
#while True:
   # print("Do you want to remove a connection? y/n")
    #ans2 = input()
    #if ans2 == 'y':
    
