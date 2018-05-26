import os, sys, math
from lxml import etree   
from PIL import Image    
from PIL import ImageDraw 

def integrateImage(imageWidth,imageHeight) :
    pix2[0][0] = pow(pix2[0][0],2)
    for x in range(imageWidth) :
        for y in range(imageHeight) :
            if x == 0 and y != 0 :
                pix[x][y] += pix[x][y-1]
                pix2[x][y] = pix2[x][y-1] + pow(pix2[x][y],2)
            elif y == 0  and x != 0 :
                pix[x][y] += pix[x-1][y]
                pix2[x][y] = pix2[x-1][y] + pow(pix2[x][y],2)
            elif x != 0 and y != 0 :
                pix[x][y] += pix[x-1][y] + pix[x][y-1] - pix[x-1][y-1]
                pix2[x][y]=pix2[x-1][y]+pix2[x][y-1]-pix2[x-1][y-1]+pow(pix2[x][y],2)

im = Image.open(sys.argv[1])
imageWidth, imageHeight = im.size
pixels = im.load()
pix  = [[int((30*pixels[y,x][0]+59*pixels[y,x][1]+11*pixels[y,x][2])/100) \
        for x in range(imageWidth)] for y in range(imageHeight)]
pix2 = [[pix[y][x] for x in range(imageWidth)] for y in range(imageHeight)]
integrateImage(imageWidth,imageHeight)
