from PIL import Image

im = Image.open('pxArtMB.bmp') # Can be many different formats.
pix = im.load()
print (im.size)  # Get the width and hight of the image for iterating over
z = 0
x = 0
y = 0 
for x in range(0, im.size[0]):

    if x % 2 == 0:
    
        for y in range(0, im.size[1]) :
            
            print ("leds[" +str(z) + "] = CRGB" + str(pix[x,y]) + ";")  # Get the RGBA Value of the a pixel of an image
            z += 1 
    else:
        for y in range(im.size[1]-1, -1, -1):
        
            print ("leds[" +str(z) + "] = CRGB" + str(pix[x,y]) + ";")  # Get the RGBA Value of the a pixel of an image
            z += 1 
                        
        
