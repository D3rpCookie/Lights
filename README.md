# Lights Guide/README
**There is two parts to this code, a python script for turning 32x32 pixel bitmap into arduino code that is able to be imported into arduino to display any image you prefer using 3 8x32 strips of led. **
##Pyton Script:
Here is what the example 32x32 bitmap will look like: ![image](https://user-images.githubusercontent.com/70545101/167725314-f9c7ea42-35b0-4348-b25a-5ae143b5a863.png)

Due to arduino being too small, we aren't able to convert the whole 32x32 pixel bitmap into a single arduino and run it so we spilt it into two arduinos. the first arduino will handle The top 8x32 bit ![image](https://user-images.githubusercontent.com/70545101/167725351-16b1cbe4-f45b-40fc-801b-bf7fb68796ff.png)

While the second arduino will handle the bottom 16x32 bit of the bit map, this means you will have to cut the 32x32 bit map into 3 pieces, the combine the bottom two piece together with the middle one being upside down. ![image](https://user-images.githubusercontent.com/70545101/167725282-29fdaf6c-8386-4451-9dc7-191e99462323.png)

To use the python script to convert the bitmap into arduino code, import the image to whatever code studio you are using and change the name in main.py ![image](https://user-images.githubusercontent.com/70545101/167724555-02bded51-873a-43cf-bc23-9f0218139381.png) 
where it says pxArtT.bmp to your bitmap's name, this will direct the python script to take in your bitmap. Then run the python script and 
