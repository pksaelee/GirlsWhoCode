print("Time for lunch!")

breadslices = 10
peanutbutter = 100
jelly = 100
sandwich = 0

while breadslices > 0:
    print("It's peanut butter jelly time!")
    breadslices = breadslices - 2
    peanutbutter = peanutbutter - 5
    jelly -= 5
    sandwich+= 1

print("I made %s sandwiches." %(sandwich))
print("I have %dg of peanut butter and %dg of jelly left over." %(peanutbutter, jelly))
print("Delicious.")
