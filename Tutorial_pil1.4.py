# -*- coding: utf-8 -*-
"""
Created on Fri Jan 26 10:43:00 2018

@author: Alexander Simonov
"""

from PIL import Image
img = Image.new('RGB',(800,600),(0,255,0))
for x in range(800):
       for y in range(600):
              img.putpixel((x,y),(int(x/3),int((x+y)/6),int(y/2)))
img.save('image.png','PNG')
img.show()
