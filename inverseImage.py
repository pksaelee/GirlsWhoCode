from PIL import Image

#import image
myImage = Image.open("ele2.jpg")#image name and file type in ()
imageData = myImage.getdata()
pixelList = list(imageData)

newPixelList = []

#pixel manipulation
for pixel in pixelList:
    red = pixel[0]
    green = pixel[1]
    blue = pixel[2]

    #average = (red+green+blue)//3

    newRed = 255 - red
    #if newRed > 255:
        #newRed = 255
    
    newGreen = 255 - green
    #if newGreen > 255:
        #newGreen = 255

    newBlue = 255 - blue
    #if newBlue > 255:
        #newBlue = 255

    p = (newRed,newGreen,newBlue)
    
#add pixel to new pixel list
    newPixelList.append(p)

#open image
newImage = Image.new("RGB",myImage.size)
newImage.putdata(newPixelList)
newImage.show()
newImage.save("newPhoto.jpg","jpg")#file type in ()
