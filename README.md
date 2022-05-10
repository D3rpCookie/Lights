# Lights Guide/README
**There is two parts to this code, a python script for turning 32x32 pixel bitmap into arduino code that is able to be imported into arduino to display any image you prefer using 3 8x32 strips of led.**
## Pyton Script:
Here is what the example 32x32 bitmap will look like(our example images are all in the repo for you to look at): ![image](https://user-images.githubusercontent.com/70545101/167725314-f9c7ea42-35b0-4348-b25a-5ae143b5a863.png)

Due to arduino being too small, we aren't able to convert the whole 32x32 pixel bitmap into a single arduino and run it so we spilt it into two arduinos. the first arduino will handle The top 8x32 bit ![image](https://user-images.githubusercontent.com/70545101/167725351-16b1cbe4-f45b-40fc-801b-bf7fb68796ff.png)

While the second arduino will handle the bottom 16x32 bit of the bit map, this means you will have to cut the 32x32 bit map into 3 pieces, the combine the bottom two piece together with the bottom one being upside down. ![image](https://user-images.githubusercontent.com/70545101/167725282-29fdaf6c-8386-4451-9dc7-191e99462323.png)

To use the python script to convert the bitmap into arduino code, import the top image and the middle/bottom image to whatever code studio you are using and change the name in main.py to  
![image](https://user-images.githubusercontent.com/70545101/167727406-e5dc6e6e-b249-41cd-a22b-b519a555db75.png)

where it says pxArtT.bmp to your bitmap's name, this will direct the python script to take in your bitmap. Then run the python script and export the result as a txt file(tOutput.txt is our result for the top one if you are following along with our pictures)
Do the same for the middle/bottom image(mbOutput.txt is our result). 

## Arduino Code: 
Next, open up arduino ide, you need to install the library FastLED within the arduino ide libraries. Then open up tArduino.txt and copy and paste the text from your tConverter.py script's output **without the first line** to replace the part where it says "leds[1] = CRGB(0, 255, 0 );", then copy tArduino.txt into your arduino ide and push the code to your 1st arduino.
![image](https://user-images.githubusercontent.com/70545101/167726875-4468b174-61cc-4e6a-baa4-bbccfff29a41.png)

Now repeat the step using the mbCoverter.py and copy it into mbArduino.txt, then push it into your 2nd Arduino. 

## Wiring: 
the arduino power and ground can be plug into the power and ground port on the arduino, soldering is advised as it allows for better longevity of the product. Please only use 4.0 V battery or plug directly into any computer using a usb. The dataIn is done using PIN 4 on the arduino on both arduinos. 
