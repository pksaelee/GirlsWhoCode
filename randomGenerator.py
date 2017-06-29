from random import randint
def level1():
    countFive = 0

    numList = []
    for num in range(100):
        num = randint(10,99)
        numList.append(num)
    print(numList)

    for number in numList:
        if number % 5 == 0:
            countFive += 1
            #print("MULTIPLE")
    print('There are %d multiples of five in this list.' %countFive)

def level2(numlist):
    numSum = 0
    
    for num in numlist:
        if num%3 == 0 or num%5 == 0:
            print(num)
            numSum += num
    print('Final sum:')
    print(numSum)

def level3(numList):
    primeSum = 0

    for num in numList:
        prime = True
        for x in range(2,num):
            if num%x==0:
                prime = False
        if prime == True:
            print(num)
            primeSum += num

    print(primeSum)
            


randomlist = []
for x in range(100):
    randnumber = randint(10,99)
    randomlist.append(randnumber)
#level1(randomlist)
#level2(randomlist)
level3(randomlist)



