import sys
import numpy as np
from PIL import Image, ImageDraw, ImageFont
import math

def openimage():
    global arg
    arg = sys.argv
    if len(arg) != 4:
        print('Wrong number of parameters')
        sys.exit()

    try:
        img = Image.open(arg[1])
    except FileNotFoundError:
        print('Find not found')
        sys.exit()

    return img

def CharSelector(h):
    chars  = "$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-                          _+~<>i!lI;:,\"^`'. "[::-1]
    charArr = list(chars)
    l = len(charArr)
    mul = l/256
    return charArr[math.floor(h*mul)]

def resizeimg(img):
    img = openimage()
    fac = arg[3]
    charWidth = 10
    charHeight = 18
    w,h = img.size
    img = img.resize((int(fac*w),int(fac*h*(charWidth/charHeight))),Image.NEAREST)
    w,h = img.size
    pixels = img.load()

    font = ImageFont.truetype(f'C:\\Windows\\Fonts\\{arg[4]}.ttf',15)
    outputImage = Image.new('RGB',(charWidth*w,charHeight*h),color=(0,0,0))
    draw = ImageDraw.Draw(outputImage)

    for i in range(h):
        for j in range(w):
            print(i,j)
            r,g,b = pixels[j,i]
            grey = int((r/3+g/3+b/3))
            pixels[j,i] = (grey,grey,grey)
            draw.text((j*charWidth,i*charHeight),CharSelector(grey),
            font=font,fill = (r,g,b))

    outputImage.save(arg[2])