# -*- coding: utf-8 -*-
"""
Created on Fri Jan 26 15:25:34 2018

@author: Alexander Simonov
"""

from PIL import Image
img = Image.open('ship.jpg')
img.show()
box = (542,619,664,653)
img2 = img.crop(box)
img2 = img2.rotate(45)
img2.show()
