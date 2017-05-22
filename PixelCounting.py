from PIL import Image
import math

im=Image.open("FILE_PATH_HERE")

WaferDiam = 50.8 #mm, wafer diameter

black=0
white=0
other=0

#count the pixels of each colour
for pixel in im.getdata():
    if pixel == (0,0,0, 255):
        black+=1
    elif pixel == (255,255,255, 255):
        white+=1
    else:
        other+=1

#assume black is dead image space, white is unplated wafer and 'other' is plated wafer area
#calculate the fractional area of the different colors       
total = black + white + other
OtherFrac = other/(white + other)

#assuming the image has been padded in the region of the flat with white pixels
Atot = math.pi*(WaferDiam/2)**2
APlated = Atot*OtherFrac

#output the result
print ('total number of pixels = ' + str(total))
print ('black = ' + str(black)+', white = '+str(white)+', other = '+str(other))

print ('Fraction of circular wafer plated = ' + str(OtherFrac)) #neglects the flat
print ('Area of circular wafer = ' + str(round(Atot)) + ' mm^2') #neglects the flat

print ('Plated area = ' + str(round(APlated)) + ' mm^2')
