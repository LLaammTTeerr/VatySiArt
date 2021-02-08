import sys
from PIL import Image, ImageDraw, ImageFont
import random
import os

m = """
Invalid number of parameters

Run again

GUIDE:

Program run format
python file.py infile.png outfile.png scalefactor fontsize word mode

scalefactor: to scale the image bigger or smaller
word: the character set
mode: sequence or random (0 for sequence; 1 for random)

"""

cu_dir = os.path.dirname(__file__)

#count for sequence mode
count = 0

def update_progress(progress):
    barLength = 10 # Modify this to change the length of the progress bar
    status = ""
    if isinstance(progress, int):
        progress = float(progress)
    if not isinstance(progress, float):
        progress = 0
    if progress >= 1:
        progress = 1
    block = int(round(barLength*progress))
    text = "\rPercent: [{0}] {1}% {2}".format( "#"*block + "-"*(barLength-block), progress*100, status)
    sys.stdout.write(text)
    sys.stdout.flush()

def argvinput():
	#count if the number of parameter is correct
    arg = sys.argv
    if len(arg) != 7:
        print(m)
        sys.exit()
    return arg

def selectchar(charset, mode):
    global count
    if len(charset) == 1:
    	#if the word is only 1 then you know
        return charset
    else:
        if mode == 1:
        	#random mode
            return random.choice(charset)
        else:
        	#sequence mode
            count = count % len(charset)
            count += 1
            return charset[count - 1]


def main():

	#read input
    arg = argvinput()

    #open the image according to the input
    img = Image.open(arg[1])

    #image scale factor
    scale = float(arg[3])

    #font wide and high
    W, H = 10, 18

    #image size
    w,h = img.size

    #resize image
    img = img.resize((int(scale*w),int(scale*h*(W/H))),Image.NEAREST)

    #new image size
    w,h = img.size

    #get the pixels color set
    pixels = img.load()

    #Draw black plain canvas
    ouputimg = Image.new('RGB', (W*w,H*h),color=(0,0,0))
    draw = ImageDraw.Draw(ouputimg)

    #Configure the font
    font = ImageFont.truetype(f'{cu_dir} + \\micross.ttf', int(arg[4]))

    #Check if everything user input is all right

    print(f'')

    cap = {0: 'Sequence', 1: 'Random'}

    print(f'Input file: {arg[1]}')
    print(f'Output file: {arg[2]}')
    print(f'Scale Factor: {arg[3]}')
    print(f'Font size: {arg[4]}')
    print(f'Word: {arg[5]}')
    print(f'Mode: {cap[int(arg[6])]}')
    
    print(f'Loop: {w} x {h}')

    choice = input('Procceed? (Y/N)? ')

    if choice.upper() == "Y":

        for i in range(h):
            for j in range(w):

                r,g,b = pixels[j,i]

                draw.text((j*W,i*H),selectchar(arg[5], int(arg[6])),font=font,fill = (r,g,b))

                update_progress((i*w + j+1)/(w*h))

        ouputimg.save(arg[2])

        print()
        print('Done, check your file')
    
    else:
        print("Proccess cancelled")


if __name__ == '__main__':
    main()