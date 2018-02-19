import numpy
import random
from PIL import Image

BIAS = 1000

weight = numpy.zeros((10, 50, 50), dtype=numpy.int)

def proceed(data, number):      #retruns yes, if number overcomes our bias
    net = 0
    for x in range(50):
        for y in range(50):
            net += data[x][y] * weight[number][x][y]
    return net >= BIAS


def decrease(data, number):     #if percepthron returns whrong number, it decreases all outs, which stir up percepthron
    for x in range(50):
        for y in range(50):
            if data[x][y]:
                weight[number][x][y] -= 1;


def increase(data, number):     #if percepthron returns right number, it increases all outs, which stir up percepthron
    for x in range(50):
        for y in range(50):
            if data[x][y]:
                weight[number][x][y] += 1;


def get_num(link):              #recognizes color of pixel
    image = Image.open(link)
    our_num = numpy.ones((50, 50), dtype=numpy.int)
    for x in range(50):
        for y in range(50):
            r, g, b = image.getpixel((y, x))
            if (r > 225 and g > 225 and b > 225):
                our_num[x][y] = 0
    return our_num


option = 0
for num in range(10):                   #for each number we teach our percepthrone
    for step in range(2500):            #quantity of lessons for the percepthrone
        link = 'C:\\Users\\Глеб\\Desktop\\50x50\\' + str(option) + '_' + str(random.randint(0, 2)) + '.jpg'
        our_num = get_num(link)
        if option != num:
            if proceed(our_num, num):
                decrease(our_num, num)
        else:
            if not proceed(our_num, num):
                increase(our_num, num)
        option += 1
        if option == 10:
            option = 0

for num in range(10):
    link = 'D:\\recognizing_numbers\\venv\\result\\result_' + str(num) + '.txt'
    f = open(link, 'w')
    for x in range(50):
        for y in range(50):
            f.write(str(weight[num][x][y]) + ' ')           #write weights to file, so we mustn't calculate it every time we use programm
        f.write('\n')                                       # and give an opportunity to learn new pictures with knowledge we already knew
    f.close()
