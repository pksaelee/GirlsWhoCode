from PIL import Image

#import image
myImage = Image.open("poster.jpeg")#image name and file type in ()
imageData = myImage.getdata()
pixelList = list(imageData)

newPixelList = []

#pixel manipulation
for pixel in pixelList:
    red = pixel[0]
    green = pixel[1]
    blue = pixel[2]

    newRed = red*2
    if newRed > 255:
        newRed = 255

    p = (newRed,green,blue)
    
#add pixel to new pixel list
    newPixelList.append(p)

#open image
newImage = Image.new("RGB",myImage.size)
newImage.putdata(newPixelList)
newImage.show()
newImage.save("newPhoto.jpeg","jpeg")#file type in ()