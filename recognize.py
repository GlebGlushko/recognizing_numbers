from PIL import Image, ImageDraw
import numpy
import random


def convert(image):                 #changes size and color of picture
    image = image.resize((50, 50))
    draw = ImageDraw.Draw(image)
    for i in range(50):
        for j in range(50):
            r, g, b = image.getpixel((j, i))
            if r + g + b > 300:
                r = 255
                g = 255
                b = 255
            else:
                r = 0
                g = 0
                b = 0
            draw.point((j, i), (r, g, b))
    #image.save("kek.jpg", "JPEG")
    return image


def get_num(link):                      #recognizes color of pixel
    image = convert(Image.open(link))
    our_num = numpy.ones((50, 50), dtype=numpy.int)
    for x in range(50):
        for y in range(50):
            r, g, b = image.getpixel((y, x))
            if (r > 225 and g > 225 and b > 225):
                our_num[x][y] = 0
    return our_num


def get_weight():                   #gets the weight, we've got during studying percethrone
    w = numpy.zeros((10, 50, 50))
    for num in range(10):
        weights_link = 'D:\\recognizing_numbers\\venv\\result\\result_' + str(num) + '.txt'
        file = open(weights_link, "r")
        for i in range(50):
            line = file.readline()
            if not line:
                print("exception")
                break
            else:
                line = line[:-2]
                w[num][i] = (line.split(' '))
        file.close()
    return w
