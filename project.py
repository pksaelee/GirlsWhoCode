from PIL import Image


myImage = Image.open("flowers.jpg")
imageData = myImage.getdata()
pixelList = list(imageData)

newPixelList = []

length = len(pixelList)

counter = 0

def intensityFunction(pixel):
    red = pixel[0]
    green = pixel[1]
    blue = pixel[2]
    intensity = red + green + blue
    darkBlue = (0,51,76)
    darkRed = (217,26,33)
    lightBlue = (112,150,158)
    yellow =(252,227,166)
    if (intensity <= 182):
        newPixelList.append(darkBlue)
    elif (intensity>=182 and intensity<=364):
        newPixelList.append(darkRed)
    elif (intensity>=364 and intensity<=546):
        newPixelList.append(lightBlue)
    elif (intensity>=546):
        newPixelList.append(yellow)
    

    
for pixel in pixelList:
    intensityFunction(pixel)
    


newImage = Image.new("RGB",myImage.size)
newImage.putdata(newPixelList)
newImage.show()
