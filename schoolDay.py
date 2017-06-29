# FUNCTION
def yourName():
    name = input()

# RUNNING PROGRAM
story = True
while story == True:
    print("Hey, let me tell you a story. First, tell me your name.")
    name = input()
    print("Ok %s this is a story about your school, in my version." %(name))
    print("MONDAY, 6:00 AM")
    print("Today is school, but you are too lazy to go.")
    print("Will you go to school?")
    ans = input()
    if (ans == "No" or ans == "no"):
        print("Well, you miss school and got scolded harshly by your mom. She demands you to do all the chores in the house for a whole year.")
        print("RIP",name)
        exit()
    elif (ans == "Yes" or ans == "yes"):
        print("You decide to go to school.")
    else:
        print("Since you didn't say no, I'll assume yes.")
        
    print("You do daily morning routine, eat breakfast, then get on the bus. There are two spots left. One at the front with the talkative bus driver and one at the back with the bullies. Where will you sit?")
    print("Choices:")
    print("A. Bus driver")
    print("B. Bullies")
    ans = input()
    if (ans == 'a'):
        print("When you sit at the bus, the driver notices you and starts to talk to you about a bunch of things you don't care about. Moments later, you realize you fell asleep and you miss your stop. ")
        print("You go home and your mom scolds you, also grounding you for life.")
        print("Have fun staying at home, %s!" %(name))
        exit()
    elif (ans == "b"):
        print("You sit in the back, and bullies pick on you but all they did was give you small insults. You ignored them and the bus stops at your school. As you get of you see a poor kid sleeping in the front of the bus. then you continue with your day.")
    else:
        print("That's not one of the choices. Guess you gotta start over.")
        exit()
    print("As you go to your first class you completely forgot to do your homework. It's for the class you hate the most, and the teacher also hates you back!")
    print("What will you do?")
    print("Choices:")
    print("A. Tell the teacher the truth")
    print("B. B.S. your homework")
    print("C. Ask to copy off your friend")
    ans = input()
    if (ans == "a"):
        print("You tell the teacher you didn't do your homeowork and he lets you finish your assignment tommorow, but you get no credit.")
        print("When you got home, you mom gives you a four hour lecture, and finished her lecture saying you are grounded for life.")
        print("Shouldn't have forgot to do your homework, %s" %(name))
        exit()
    elif (ans == "b"):
        print("You finish your homework in under five minutes without the teacher noticing and you get a passin grade. Great job!")
        print("Three hours later, lunch comes around. Today's menu is the nasty dried chicken teriyaki with rice that taste like dog food.")
        print("What will you do?")
        print("Choices:")
        print("A. Buy lunch")
        print("B. Skip lunch")
        ans = input()
        if (ans == 'a'):
            print("You buy the disgusting lunch. For some logical reason, you trip and your food goes flying and lands on ths bus bully.")
            print("He treatens to break your bone for ruining his favorite shirt and you look around for help.")
            print("You see your friend, your friend notices your situation and calls a teacher for help. A teacher then came and sent the bully to detention. Looks like you're safe for now.")
            print("After school ends, you go home and your mom seems to be in a happy mood. Seems like you survived school today and your mom's wrath. Let's see if you survive tommorow, %s" %(name))
            exit()
        elif (ans == 'b'):
            print("You go hungry for the rest of the school hour.")
            print("After you get home from school you told your mom you were really hungry. She asked why and you told her the reason. Then she says she won't feed you for the rest of your life. Hope your don't starve, %s" %(name))
            exit()
        else:
            print("That's not one of the choices. Guess you gotta start over.")
            exit()
    elif (ans == "c"):
        print("After you copied off your friend's homework and turned it in, the teacher then calls both of you to see him and he gives you both a ZERO and detention for plagerizing.")
        print("Your friend glares with disgust, and ignores you after class.")
        print("Three hours later, lunch comes around. Today's menu is the nasty dried chicken teriyaki with rice that taste like dog food.")
        print("What will you do?")
        print("Choices:")
        print("A. Buy lunch")
        print("B. Skip lunch")
        ans = input()

        if (ans == 'a'):
            print("You buy the disgusting lunch. For some logical reason, you trip and your food goes flying and lands on ths bus bully.")
            print("He treatens to break your bone for ruining his favorite shirt and you look around for help.")
            print("You see your friend, but your friend ignores you and leaves the cafeteria. Welp looks like someones going to the hospital.")
            print("Definetly RIP you, %s." %(name)) 
            exit()
        elif (ans == 'b'):
            print("You go hungry for the rest of the school hour.")
            print("After you get home from school you told your mom you were really hungry. She asked why and you told her the reason. Then she says she won't feed you for the rest of your life. Hope your don't starve, %s" %(name))
            exit()
        else:
            print("That's not one of the choices. Guess you gotta start over.")
            exit()
    else:
        print("That's not one of the choices. Guess you gotta start over.")
        exit()
