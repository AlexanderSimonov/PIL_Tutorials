# -*- coding: utf-8 -*-
"""
Created on Fri Jan 26 15:26:39 2018

@author: Alexander Simonov
"""

from PIL import Image
img = Image.open('ship.jpg')
box = (542,619,664,653)
img2 = img.crop(box)
img2 = img2.transpose(Image.FLIP_LEFT_RIGHT)
img.paste(img2,box)
img.show()
