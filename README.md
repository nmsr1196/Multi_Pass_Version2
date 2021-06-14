# Multi_Pass_Version2
MultiPass_VERSION 2

![Image of MultiPassV2] (https://github.com/nmsr1196/Multi_Pass_Version2/blob/main/MultipassV2_Demo.mov) (https://github.com/nmsr1196/Multi_Pass_Version2/blob/main/MultipassV2_TopView_.png)


### DEMO VIDEO OF MULTIPASS VERSION 2 https://youtu.be/BCjvFPc9UcI

This document contains all aspects to completing this project. Please read before implementing. I will also supply the links and
refer to VERSION 1 because there are some things that are similar. All files needed to create this project are included.

### BELOW ARE THE NOTES FOR HOW EVERYTHING WAS USED AND METHODS TO CREATE THE MULTIPASS V2.


#### NEW FEATURES: 

- LEDs for the stem/rod

- Night light LED

- LiPo charging

- Switchable Lens (acrylic, 3D printed)

- Can use the movie card or vaccine card

- Sound (voice of Leeloo)


#### CODE: 

THIS PROJECT USES CIRCUITPYTHON.

The code file ‘Multipass_V2.py’ has to be changed to ‘code.py’ for the QT Py 2040. Also in the code ignore the two lines 'button'. Its not being used in the code

#### WIRING: 

To try and keep a thin profile, I used wire-wrap. To insure connectivity, I also soldered the connections of the wire-wrap.


#### GLUE USED: 

I used hot glue to secure the parts. And just a small bead on the bottom of the QT Py 2040. But, be careful not to let it bleed into
the bottom part as this could prevent the card from sliding in all the way to the back.

#### 3D PRINTING MODIFICATION FROM VERSION 1: 

As mentioned before, version 1 is a re-mix of the Ruiz brothers from a remix from a user ‘Level2three’. So, this one ‘version 2’ is a remix 

of version 1. Remix of a remix of a remix of a remix and on  and on.

- The geometry around the on/off button was slightly widen. (This depends on the type of switch you use)

- The power led was  to the left to allow the pass card to not be notched.

- Extra holes were added in the bottom part for wiring.

- Cavities were added for the three sequin leds 


#### ACRYLIC: 

- Acylic does not have to be used. A light diffusion 3D material can be used. For this version 2. I used  1/8” and 1/4” pieces.

- The parts are small so the cuts are fast and simple.

- In this version 2, I made the  stem/rod slightly longer due to the slight change in the button geometry.


#### POWER:

- You can use any size lips battery you like. Unlike version 1, I did not make a battery holder for this version. I put a dab of hot glue for the 

battery since it will be recharged by the power boost.

- 420 mAh LiPo (https://www.adafruit.com/product/4236) You can use a smaller size, Its just what I had at the time.

- Powerboost (https://www.adafruit.com/product/2465)  or if you have a different type of LiPo charger, you can use that.

- Diode - Used a diode to connect to 5 volt pin of the QT Py 2040. Cathode side to 5V pin of QT Py (https://learn.adafruit.com/adafruit-qt-py-2040/pinouts) Cathode


#### BELOW ARE THE PARTS USED:

- QT Py 2040 (https://www.adafruit.com/product/4900 )

- Stemma Speaker (https://www.adafruit.com/product/3885)

- 7 Jewel Neopixel (https://www.adafruit.com/product/2859 )  This goes into the lens disc hole

- Adafruit LED Sequins - Emerald Green, Pack of 5 (these are 3 of the lights I used for the rod and the night light) https://www.adafruit.com/product/1756

- Mini On/Off button (https://www.adafruit.com/product/3870) Power button. If you choose to use a different button, hot glue is your friend, or 3D print some to 
  compensate the size.

- Metal Ball Tactile Button (https://www.adafruit.com/product/3347) This is the pushbutton for the night light. 

- 3mm LED (https://www.adafruit.com/product/4202) You can use any type/color of 3mm LED

- Diode  Used to connect between powerboats 5V and 5V pin of QT Py 2040 (see above)

- 2.2K Resistor You can use your own value of resistor. I chose a higher value to try and reduce brightness

- Wire Wrap (https://www.amazon.com/gp/product/B01CK9GZV6/ref=ppx_yo_dt_b_search_asin_title?ie=UTF8&psc=1 ) I used multiple colors to keep my wiring sanity.

you can use a solid color option (https://www.adafruit.com/product/1446) the choice is yours.

- OLED SSD1306 I2C Display (https://www.amazon.com/Pieces-Display-Module-SSD1306-Screen/dp/B08N6N8L5Q/ref=sr_1_8?dchild=1&keywords=oled+i2c&qid=1622717100&sr=8-8) You can use any version of the ssd1306. I chose this one because of its small footprint and low profile and its wiring connections

on one end.

- 3D Material  I had some Prusa Silver PLA. You can use any color/material. I used silver because I did not want the cosplay police coming after me

- Acrylic I used clear green 1/8” for the stem/rod and lense. Also for the lens, I used 1/4” green. As long as its diffusible, the choose is yours. 

- Light Cardstock or black paper or regular paper. The color and choice is up to you. I used a cricut to cut the shape.


#### MULTIPASS CARD:

Movie Card

- I used a replica of the movie card I created in Photoshop. The Photoshop file is included. This file is in version 1.

You will have to change the following because in order to get to ‘Fhloston Paradise’ duplicate IDs are highly unacceptable:

- name

- pictures 

- numbers below pictures

- The size of the pictures can be done in Photoshop (PS) menu: ‘Image’, ‘Image Size’. Or another program of your choosing.

- For the X-ray picture, Copy your original picture and use PS to ‘invert’ the image under ‘Image, ‘Adjustments’ the ‘Invert’ menu.


#### FILES

- MultipassV2_Demo.mov - This shows some of the features of the multipass version 2

- MultiPass_Version2.fzz - Parts drawing and connectivity

- multipass3.wav - Wav file for Leeloo's voice

- Multipass_TOP_V2.stl - 3D model for multipass top

- Multipass_BOTTOM_V2.stl - 3D model for multipass bottom

- Multipass_V2.py - This is the CircuitPython code. You will need to rename this file to 'code.py' and load libraries listed in code.

- Multipass_V2_Rod.stl - This is the acrylic rod for laser cutting. This measures 3.99mm x 40.9mm. You may have to adjust for 3D printing dependant on material.

- Multpass_V2_lense.svg - This is the acrylic rod for laser cutting. This measures 25.8mm. You may have to adjust for 3D printing dependant on material.





