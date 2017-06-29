from PIL import Image
#FUNCTION
def negative(pixel):
    for pixel in pixelList:
        red = pixel[0]
        green = pixel[1]
        blue = pixel[2]

        newRed = 255 - red
        newGreen = 255 - green
        newBlue = 255 - blue
       
        p = (newRed,newGreen,newBlue)
        newPixelList.append(p)

def overExposed(pixel):
    for pixel in pixelList:
        red = pixel[0]
        green = pixel[1]
        blue = pixel[2]

        newRed = red*2
        if newRed > 255:
            newRed = 255
        
        newGreen = green*2
        if newGreen > 255:
            newGreen = 255

        newBlue = blue*2
        if newBlue > 255:
            newBlue = 255 

        p = (newRed,newGreen,newBlue)
        newPixelList.append(p)


#import image
myImage = Image.open("ele2.jpg")#image name and file type in ()
imageData = myImage.getdata()
pixelList = list(imageData)

newPixelList = []
length = len(pixelList)
halfway = length//2
counter = 0
#pixel manipulation
for pixel in pixelList:
    if (counter<halfway):#top half
        overExposed(pixel)
    else:#bottom half
        negative(pixel)
    counter += 1

#add pixel to new pixel list

#open image
newImage = Image.new("RGB",myImage.size)
newImage.putdata(newPixelList)
newImage.show()
newImage.save("newPhoto.jpg","jpg")#file type in ()
