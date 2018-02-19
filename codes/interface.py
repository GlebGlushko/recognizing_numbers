import tkinter as tk
import numpy
from tkinter import filedialog
import os
from PIL import Image, ImageTk
import recognize

# tk._test()


root = tk.Tk()
root.minsize(350, 350)
root.maxsize(350, 350)
root.title("Recognizing")
def read(link):                     #reads weights from result's file
    file = open(link, 'r')
    w = numpy.zeros((50, 50))
    for i in range(50):
        line = file.readline()
        line = line[:-2]
        w[i] = (line.split(' '))
    file.close()
    return w


def yes_click(ans_num, number):     #if percepthron returns right number, it increases all outs, which stir up percepthron

    link = 'D:\\recognizing_numbers\\venv\\result\\result_' + str(ans_num) + '.txt'
    weight = read(link)
    f = open(link, 'w')
    for x in range(50):
        for y in range(50):
            f.write(str(int(weight[x][y] + number[x][y])) + ' ')
        f.write('\n')
    f.close()


def no_click(ans_num, number):      #if percepthron returns wrong number, it decreases all outs, which stir up percepthron
    link = 'D:\\recognizing_numbers\\venv\\result\\result_' + str(ans_num) + '.txt'
    # print("TOZHE", ans_num)
    weight = read(link)
    f = open(link, 'w')
    for x in range(50):
        for y in range(50):
            f.write(str(int(weight[x][y] - number[x][y])) + ' ')
        f.write('\n')
    f.close()


def calculate(number):          #decides what number is it
    weight = recognize.get_weight()
    ans_num = -100
    ans = -2500
    for num in range(10):
        net = -2500
        for x in range(50):
            for y in range(50):
                net += number[x][y] * weight[num][x][y]
        if ans < net:
            ans = net
            ans_num = num
    #print (ans)
    return ans_num


def start():            #opens window to communicate with user
    link = filedialog.askopenfilename()
    number = recognize.get_num(link)
    ans_num = calculate(number)
    s = "Is it " + str(ans_num) + "?"
    lable = tk.Label(root, text=s)
    lable.place(x=170, y=100)
    yes = tk.Button(root,
                    text='Yes',
                    command=lambda: yes_click(ans_num, number))
    yes.place(x=145, y=140, width=35, height=15)
    no = tk.Button(root,
                   text='No',
                   command=lambda: no_click(ans_num, number))
    no.place(x=190, y=140, width=35, height=15)


btn = tk.Button(root,
                text='Select file',
                bg='white', fg='black',
                command=start,
                width=15, height=1)
btn.place(x=130, y=50)

root.mainloop()
