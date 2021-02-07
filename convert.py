import sys
import numpy as np
import matplotlib
import matplotlib.pyplot

arg = sys.argv

if len(sys.argv) != 2:
    print('Wrong number of parameters')
    sys.exit()

arg = arg[1]

try:
    image = matplotlib.image.imread(arg)
except FileNotFoundError:
    print('File not found')
    sys.exit()

grey_1 = r"""$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,"^`'. """
grey_2 = r" .:-=+*#%@"
reversed(grey_2)

rgb_weight = [0.2989, 0.5870, 0.1140]

rgb_img = image[...,:3]

gray_rgb = np.dot(rgb_img, rgb_weight)

#H, W = gray_rgb.shape

#average = np.average(gray_rgb)

result = []

print(gray_rgb)

for row in gray_rgb:
    row_temp = []
    for num in row:
        row_temp.append(grey_1[int(num*69/255)])
    result.append(row_temp)

for i in result:
    print(i)