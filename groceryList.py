groceryList = []
another = True

while True:
    print("Do you want to add an item to your grocery list? (y/n)")
    ans = input()
    if ans == "y":
        print("What would you like to add?")
        groceryList.append(input())
        
    if ans == "n":
        print("Ok, here's your list.")
        for x in groceryList:
            print(x)
        break
