from PIL import Image

#import image
myImage = Image.open("waterfall.jpg")#image name and file type in ()
imageData = myImage.getdata()
pixelList = list(imageData)

newPixelList = []

#pixel manipulation
for pixel in pixelList:
    red = pixel[0]
    green = pixel[1]
    blue = pixel[2]

    average = (red+green+blue)//3

    newRed = average
    #if newRed > 255:
        #newRed = 255
    
    newGreen = average
    #if newGreen > 255:
        #newGreen = 255

    newBlue = average
    #if newBlue > 255:
        #newBlue = 255

    p = (newRed,newGreen,newBlue)
    
#add pixel to new pixel list
    newPixelList.append(p)

#open image
newImage = Image.new("RGB",myImage.size)
newImage.putdata(newPixelList)
newImage.show()
newImage.save("newPhoto.jpg","jpg")#image name and file type in ()
