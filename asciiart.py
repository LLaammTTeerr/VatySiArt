import sys
import numpy as np
from PIL import Image, ImageDraw, ImageFont
import math
import random

"""
Program format
python file.py infile.png outfile.png scalefactor fontsize word mode

scalefactor: to scale the image bigger or smaller
word: the character set
mode: sequence or random (0 for sequence; 1 for random)

"""

count = 0

def argvinput():
    arg = sys.argv
    if len(arg) != 7:
        print('Wrong number of parameters')
        sys.exit()
    return arg

def selectchar(charset, mode):
    global count
    if len(charset) == 1:
        return charset
    else:
        if mode == 1:
            return random.choice(charset)
        else:
            count = count % len(charset)
            count += 1
            return charset[count - 1]


def main():
    arg = argvinput()
    img = Image.open(arg[1])
    scale = float(arg[3])
    W, H = 10, 18
    w,h = img.size
    img = img.resize((int(scale*w),int(scale*h*(W/H))),Image.NEAREST)
    w,h = img.size
    pixels = img.load()

    ouputimg = Image.new('RGB', (W*w,H*h),color=(0,0,0))
    draw = ImageDraw.Draw(ouputimg)

    font = ImageFont.truetype('C:\\Windows\\Fonts\\micross.ttf', int(arg[4]))

    print(w,h)

    input('Procceed?')

    for i in range(h):
        for j in range(w):

            print(i,j)

            r,g,b = pixels[j,i]

            draw.text((j*W,i*H),selectchar(arg[5], int(arg[6])),font=font,fill = (r,g,b))

    ouputimg.save(arg[2])


if __name__ == '__main__':
    main()