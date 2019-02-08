from tkinter import *
from defs import *
import time
import random

scale = 10
do_wrap = False

filename = 'initial_population.csv'
my_dir = os.path.dirname(os.path.realpath(__file__))
filename = my_dir + '/' + filename
matrix = csv_to_matrix(filename)

def do_something_wrapping(matrix, scale):
    w.delete("all")
    rowlen = len(matrix)
    collen = len(matrix[0])

    new_matrix = []
    for row in range(rowlen):
        new_matrix.append([])
        for num in matrix[row]:
            new_matrix[row].append(num)
    color = my_entry4.get()
    if color == 'random':
        red = (random.randint(0, 0xff))*65536
        green = (random.randint(0, 0xff))*256
        blue = (random.randint(0, 0xff))
        color_code = red + green + blue
        color = "%06x" % color_code
        color = ('#' + color)

    for row in range(rowlen):
        for col in range(collen):
            sum = 0
            for rowcounter in range(-1, 2):
                for colcounter in range(-1, 2):
                    sum += new_matrix[(rowcounter+row)%(rowlen)][(colcounter+col)%(collen)]
            if matrix[row][col] == 0:
                if sum == 3:
                    matrix[row][col] = 1
                    w.create_rectangle(col*scale, row*scale, col*scale+scale, row*scale+scale, fill=color)
            else:
                if sum != 3:
                    if sum != 4:
                        matrix[row][col] = 0
                    else:
                        w.create_rectangle(col*scale, row*scale, col*scale+scale, row*scale+scale, fill=color)
                else:
                    w.create_rectangle(col*scale, row*scale, col*scale+scale, row*scale+scale, fill=color)

def continue_doing_something_wrapping(matrix, scale):
    time_between = float(my_entry.get())
    number_of_iterations = int(my_entry2.get())
    do_stop = str(my_entry3.get())

    iterations_remaining = number_of_iterations

    for iteration in range(number_of_iterations):

        do_something_wrapping(matrix, scale)
        iterations_remaining -=1
        my_text.delete(1.0, END)
        my_text.insert(END, iterations_remaining)
        do_stop = str(my_entry3.get())
        if do_stop == 'X':
            break

        time.sleep(time_between)
        root.update()

    my_text.delete(1.0, END)
    my_text.insert(END, 'DONE')

def do_something_nonwrapping(matrix, scale):
    w.delete("all")
    rowlen = len(matrix)
    collen = len(matrix[0])

    padded_matrix = []
    padded_matrix.append([0 for i in range(collen+2)])

    for row in range(rowlen):
        padded_matrix.append([0])
        for num in matrix[row]:
            padded_matrix[row+1].append(num)
        padded_matrix[row+1].append(0)
    padded_matrix.append([0 for i in range(collen+2)])

    color = my_entry4.get()
    if color == 'random':
        red = (random.randint(0, 0xff))*65536
        green = (random.randint(0, 0xff))*256
        blue = (random.randint(0, 0xff))
        color_code = red + green + blue
        color = "%06x" % color_code
        color = ('#' + color)

    for row in range(rowlen):
        for col in range(collen):
            sum = 0
            for rowcounter in range(3):
                for colcounter in range(3):
                    sum += padded_matrix[rowcounter+row][colcounter+col]
            if matrix[row][col] == 0:
                if sum == 3:
                    matrix[row][col] = 1
                    w.create_rectangle(col*scale, row*scale, col*scale+scale, row*scale+scale, fill=color)
            else:
                if sum != 3:
                    if sum != 4:
                        matrix[row][col] = 0
                    else:
                        w.create_rectangle(col*scale, row*scale, col*scale+scale, row*scale+scale, fill=color)
                else:
                    w.create_rectangle(col*scale, row*scale, col*scale+scale, row*scale+scale, fill=color)

def continue_doing_something_nonwrapping(matrix, scale):
    time_between = float(my_entry.get())
    number_of_iterations = int(my_entry2.get())
    iterations_remaining = number_of_iterations

    for iteration in range(number_of_iterations):

        do_something_nonwrapping(matrix, scale)
        iterations_remaining -=1
        my_text.delete(1.0, END)
        my_text.insert(END, iterations_remaining)

        time.sleep(time_between)
        root.update()

    my_text.delete(1.0, END)
    my_text.insert(END, 'DONE')


root = Tk()
root.state('zoomed')

top = Frame(root)
bottom = Frame(root)
top.pack(side=TOP)
bottom.pack(side=BOTTOM, fill=BOTH, expand=True)

if do_wrap == True:
    my_button = Button(root, bg='#808080', width=20, command= lambda: do_something_wrapping(matrix, scale), height=1, text='ITERATE ONCE')
else:
    my_button = Button(root, bg='#808080', width=20, command= lambda: do_something_nonwrapping(matrix, scale), height=1, text='ITERATE ONCE')

my_label = Label(root, text='TIME BETWEEN UPDATES')
my_entry = Entry(root, width=10)

my_label2 = Label(root, text='NUMBER OF ITERATIONS')
my_entry2 = Entry(root, width=10)

if do_wrap == True:
    widget = Button(root, bg='#808080', width=20, height=1, command= lambda: continue_doing_something_wrapping(matrix, scale), text='ITERATE OVER TIME')
else:
    widget = Button(root, bg='#808080', width=20, height=1, command= lambda: continue_doing_something_nonwrapping(matrix, scale), text='ITERATE OVER TIME')

my_text = Text(root, width=10, height=1)

my_entry3 = Entry(root, width=10)

my_button.pack(in_=top, side=LEFT)
my_label.pack(in_=top, side=LEFT)
my_entry.pack(in_=top, side=LEFT)
my_label2.pack(in_=top, side=LEFT)
my_entry2.pack(in_=top, side=LEFT)
widget.pack(in_=top, side=LEFT)
my_text.pack(in_=top, side=LEFT)
my_entry3.pack(in_=top, side=LEFT)

w = Canvas(root, width=len(matrix[0])*scale, height=len(matrix)*scale, bg='#000000')
w.pack()
for new_row in range(len(matrix)):
    for new_col in range(len(matrix[0])):
        if matrix[new_row][new_col] == 1:
            w.create_rectangle(new_col*scale, new_row*scale, new_col*scale+scale, new_row*scale+scale, fill="#ffffff")

my_label3 = Label(root, text='COLOR')
my_entry4 = Entry(root, width=10)
my_entry4.insert(10, '#ffffff')
my_label3.pack(in_=bottom, side=LEFT)
my_entry4.pack(in_=bottom, side=LEFT)

root.mainloop()
