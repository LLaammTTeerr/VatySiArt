import sys
import numpy as np
from PIL import Image, ImageDraw, ImageFont
import math
import random

"""
Program format
python file.py infile.png outfile.png scalefactor word mode

scalefactor: to scale the image bigger or smaller
word: the character set
mode: sequence or random (0 for sequence; 1 for random)

"""

font = 'C:\\Windows\\Fonts\\micross.ttf'
count = 0

def argvinput():
    arg = sys.argv
    """if len(arg) != 6:
        print('Wrong number of parameters')
        sys.exit()"""
    return arg

def selectchar(charset, mode):
    global count
    if len(charset) == 1:
        return charset
    else:
        if mode == 1:
            return random.choice(charset)
        else:
            count += 1
            return charset[(count - 1)%len(charset)]


def main():
    arg = argvinput()
    img = Image.open(arg[1])
    print(img)

if __name__ == '__main__':
    main()