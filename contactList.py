contactList = {"Emergency": "911"}

addContacts = True
while addContacts == True:
    print("Do you want to add a contact in you your list?(y/n)")
    ans = input().lower()
    if (ans == "y"):
        print("What is the name of your contact?")
        name = input()
        print("Do you want to add a  phone number?(y/n)")
        answer = input().lower()
        if (answer == "y"):
            print("Input phone number:")
            number = input()
            contactList[name] = number
            print("Phone number added.")
            print("Do you want to add an email address of %s?(y/n)" %name)
            answ = input().lower()
            if (answ == "y"):
                print("Input address:")
                address = input().lower()
                contactList[name] = address
                print("Address added.")
            elif (answ == "n"):
                break
            else:
                print("Please type 'y' or 'n'.")
        elif (ans == "n"):
            print("Do you want to add an address of %s?(y/n)" %name)
            answ = input().lower()
            if (answ == "y"):
                print("Input address:")
                address = input().lower()
                contactList[name] = address
                print("Address added.") 
            elif (answ == "n"):
                break
            else:
                print("Please type 'y' or 'n'.")
        else:
            print("Please type 'y' or 'n'.")
    elif(ans == "n"):
        break
    else:
        print("Please type 'y' or 'n'.")

print("Contacts saved")
print()
print("MY CONTACTS:")
print()
for contact in contactList:
    print("Name: " + contact)
    number = contactList[contact]
    address = contactList[contact]
    defineType = type(number)
    if (defineType == str):
        print("Number:" + contactList[contact])
        print("Address:" + contactList[contact])
    elif (defineType == list):
        for x in number:
            print("Numbers:")
            print("- " + x)
        for y in address:
            print("Address:")
            print("- " + y)
    print()
        
