# -*- coding: utf-8 -*-
"""
Created on Fri Jan 26 15:10:37 2018

@author: Alexander Simonov
"""
from PIL import Image
from PIL import ImageFilter
img = Image.open('ship.jpg')
imout = img.filter(ImageFilter.CONTOUR)
img.show()
imout.show()

