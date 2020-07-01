from PIL import Image
import math
import catsnake

def determinePoint(x, y):
    c = catsnake.comp(x, y)
    z = catsnake.comp(0, 0)

    for i in range(255):
        z = (z * z) + c
        if z.real > 2048 or z.imag > 2048 or z.real < -2048 or z.imag < -2048:
            return i
    return 255

img = Image.new("RGB", (256, 256), "black")
px = img.load()

for y in range(img.height):
    for x in range(img.width):
        rx = (x - (img.width / 2)) / (img.width / 4)
        ry = (y - (img.height / 2)) / (img.height / 4)
        v = determinePoint(rx, ry)
        px[x, y] = (255 - v, 0, v)
img.show()