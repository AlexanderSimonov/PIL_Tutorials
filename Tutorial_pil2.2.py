# -*- coding: utf-8 -*-
"""
Created on Fri Jan 26 10:48:54 2018

@author: Alexander Simonov
"""

from PIL import  Image
img = Image.open('image.png')
for x in range(img.size[0]):
      for y in range(img.size[1]):
            r,g,b = img.getpixel((x,y))
            img.putpixel((x,y),(b,r,g))
img.save('image2.png','PNG')
img.show()
