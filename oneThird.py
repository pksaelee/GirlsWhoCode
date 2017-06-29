from PIL import Image




def doubleRed(pixel):

    red=pixel[0]
    green=pixel[1]
    blue=pixel[2]

    newRed = red*2
    if newRed>255:
        newRed=255

    p=(newRed,green,blue)

    newPixelList.append(p)

def grayScale(pixel):
    red=pixel[0]
    green=pixel[1]
    blue=pixel[2]
    avg = (red+green+blue)//3
    
    newRed = avg

    newGreen = avg

    newBlue = avg
        
    p=(newRed,newGreen,newBlue)

    newPixelList.append(p)

def doubleBlue(pixel):
    red=pixel[0]
    green=pixel[1]
    blue=pixel[2]

    newBlue = blue*2
    if newBlue>255:
        newBlue=255

    p=(red,green,newBlue)

    newPixelList.append(p)


myImage = Image.open("waterfall.jpg")
imageData = myImage.getdata()
pixelList = list(imageData)

newPixelList = []

length = len(pixelList)
oneThird = length//3
twoThird = oneThird*2

counter = 0


for pixel in pixelList:
    if(counter<oneThird):
        doubleRed(pixel)
    elif(counter>oneThird and counter<twoThird):
        doubleBlue(pixel)
    else:
        grayScale(pixel)
    counter+=1

newImage = Image.new("RGB",myImage.size)
newImage.putdata(newPixelList)
newImage.show()
