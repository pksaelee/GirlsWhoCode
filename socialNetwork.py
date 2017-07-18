#GLOBAL VARIABLES
users={"pksaelee":["Precious Saelee", "3@gmail.com"]}

#FUNCTION
def userCheck(username):
    if (len(users) == 0):
        return True
    for each in users:
        if username == each:
            return False
    return True

#CLASSES
class User:
    def __init__(self,name,email,userName):
        self.name = name
        self.email = email
        self.userName = userName

        userData = [name,email]
        users[userName] = userData

        self.connections = []
        
    def addConnections(self,connectionsUser):
        connections = connectionsUser.split()
        for each in connections:
            self.connections.append(each)
            
    def removeConnections(self,connectionsUser):
        self.connections.remove(connectionsUser)

    def makeConnectionList(self):
        connectionList = self.connections
        connectionList.sort()
        print("You have " + str(len(connectionList)) + " people in your connections.")
        print("Here's your list of connections.")
        for each in connectionList:
            print(each)
        print()
        
class Network:
    def __init__(self):
        self.users = users

     

#RUNNING CODE
print("Welcome to the NEW Social Network!")
print("Please enter your full name.")
newName = input ()

print("Please enter your email address.")
newEmail = input()

print("Please enter your desired username.")
print("Please do not have spaces in your username.")
chooseUser = True
while(chooseUser):
    newUser = input()
    result = userCheck(newUser)
    if result == True:
        chooseUser = False
        user1 = User(newName,newEmail,newUser)
    else:
        print("Sorry, this username has already been taken. Please choose another one.")
while True:
    print("Add some connections? y/n")
    ans = input()

    if ans == 'y':
        print("Please enter the name of the new connection.")
        connections = input()
        user1.addConnections(connections)
        print("Please enter the username.")
        u = input()
        print("Please enter email of the user.")
        e = input()
        newCon = User(connections,e,u)
        newCon.makeConnectionList()
        user1.makeConnectionList()

        if len(connections) == 0:
            print("You don't have any connections to remove.")
        else:
            while True:
                print("Remove a connection? y/n")
                ans2 = input()
                
                if ans2 =="y":
                    print("Please type the name you want to remove.")
                    connection = input()
                    user1.removeConnections(connection)
                    user1.makeConnectionList()
                elif ans2=="n":
                    print()
                    break
                else:
                    print("Please type y or n.")
    elif ans=='n':
        break
    else:
        print("Please type y or n.")
print(users)
