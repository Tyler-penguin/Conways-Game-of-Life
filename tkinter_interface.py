# imports the defs
from tkinter import *
from defs import *
import time
import random

# sets the parameters for the code
scale = 15
do_wrap = True
filename = 'initial_population.csv'

# creates the the initial matrix from the csv
my_dir = os.path.dirname(os.path.realpath(__file__))
filename = my_dir + '/' + filename
matrix = csv_to_matrix(filename)

# defines the wrapping function
def do_something_wrapping(matrix, scale):
    # erases the canvas
    w.delete("all")
    rowlen = len(matrix)
    collen = len(matrix[0])

    # creates an identical matrix
    new_matrix = []
    for row in range(rowlen):
        new_matrix.append([])
        for num in matrix[row]:
            new_matrix[row].append(num)

    color = my_entry4.get()
    # generates random colors
    if color == 'random':
        red = (random.randint(0x22, 0x88))*65536
        green = (random.randint(0x22, 0x88))*256
        blue = (random.randint(0x22, 0x88))
        color_code = red + green + blue
        color = "%06x" % color_code
        color = ('#' + color)

    # iterates through the board
    for row in range(rowlen):
        for col in range(collen):
            sum = 0
            # adds the numbers in a 3*3 grid centered on the current position
            for rowcounter in range(-1, 2):
                for colcounter in range(-1, 2):
                    sum += new_matrix[(rowcounter+row)%(rowlen)][(colcounter+col)%(collen)]
            # determines what to do if the cell was not alive
            if matrix[row][col] == 0:
                if sum == 3:
                    matrix[row][col] = 1
                    w.create_rectangle(col*scale, row*scale, col*scale+scale, row*scale+scale, fill=color)
            # determines what to do if the cell was alive
            else:
                if sum != 3:
                    if sum != 4:
                        matrix[row][col] = 0
                    else:
                        w.create_rectangle(col*scale, row*scale, col*scale+scale, row*scale+scale, fill=color)
                else:
                    w.create_rectangle(col*scale, row*scale, col*scale+scale, row*scale+scale, fill=color)

# defines a function that automatically repeats the wrapping function
def continue_doing_something_wrapping(matrix, scale):
    time_between = float(my_entry.get())
    number_of_iterations = int(my_entry2.get())
    do_stop = str(my_entry3.get())
    iterations_remaining = number_of_iterations
    for iteration in range(number_of_iterations):

        do_something_wrapping(matrix, scale)
        # displays the number of iterations until the loop is completed
        iterations_remaining -=1
        my_text.delete(1.0, END)
        my_text.insert(END, iterations_remaining)

        # allows the loop to be stopped before it finishes
        do_stop = str(my_entry3.get())
        if do_stop == 'X':
            break

        # allows you to space out the time between updates
        time.sleep(time_between)
        root.update()

    my_text.delete(1.0, END)
    my_text.insert(END, 'DONE')

def do_something_nonwrapping(matrix, scale):
    # erases the canvas
    w.delete("all")
    rowlen = len(matrix)
    collen = len(matrix[0])

    # copies the matrix and surrounds it with zeros
    padded_matrix = []
    padded_matrix.append([0 for i in range(collen+2)])
    for row in range(rowlen):
        padded_matrix.append([0])
        for num in matrix[row]:
            padded_matrix[row+1].append(num)
        padded_matrix[row+1].append(0)
    padded_matrix.append([0 for i in range(collen+2)])

    # sets the color of living squares
    color = my_entry4.get()
    if color == 'random':
        red = (random.randint(0, 0xff))*65536
        green = (random.randint(0, 0xff))*256
        blue = (random.randint(0, 0xff))
        color_code = red + green + blue
        color = "%06x" % color_code
        color = ('#' + color)

    # iterates through the matrix to determine if the cell willl be alive or not
    for row in range(rowlen):
        for col in range(collen):
            sum = 0

            # adds the numbers in a 3*3 grid centered on the current position
            for rowcounter in range(3):
                for colcounter in range(3):
                    sum += padded_matrix[rowcounter+row][colcounter+col]
            # determines what to do if the cell was not alive
            if matrix[row][col] == 0:
                if sum == 3:
                    matrix[row][col] = 1
                    w.create_rectangle(col*scale, row*scale, col*scale+scale, row*scale+scale, fill=color)
            # determines what to do if the cell was alive
            else:
                if sum != 3:
                    if sum != 4:
                        matrix[row][col] = 0
                    else:
                        w.create_rectangle(col*scale, row*scale, col*scale+scale, row*scale+scale, fill=color)
                else:
                    w.create_rectangle(col*scale, row*scale, col*scale+scale, row*scale+scale, fill=color)

# defines a function that automatically repeats the nonwrapping function
def continue_doing_something_nonwrapping(matrix, scale):
    time_between = float(my_entry.get())
    number_of_iterations = int(my_entry2.get())
    iterations_remaining = number_of_iterations

    for iteration in range(number_of_iterations):

        do_something_nonwrapping(matrix, scale)
        # displays the number of iterations until the loop is completed
        iterations_remaining -=1
        my_text.delete(1.0, END)
        my_text.insert(END, iterations_remaining)
        # allows the loop to be stopped before it finishes
        do_stop = str(my_entry3.get())
        if do_stop == 'X':
            break

        # allows you to space out the time between updates
        time.sleep(time_between)
        root.update()

    my_text.delete(1.0, END)
    my_text.insert(END, 'DONE')

# initializes the tkinter loop
root = Tk()
# makes the tkinter window fullscreen
root.state('zoomed')

# allows for nice object placement
top = Frame(root)
bottom = Frame(root)
top.pack(side=TOP)
bottom.pack(side=BOTTOM, fill=BOTH, expand=True)

# creates a button that iterates once
if do_wrap == True:
    my_button = Button(root, bg='#808080', width=20, command= lambda: do_something_wrapping(matrix, scale), height=1, text='ITERATE ONCE')
else:
    my_button = Button(root, bg='#808080', width=20, command= lambda: do_something_nonwrapping(matrix, scale), height=1, text='ITERATE ONCE')

my_label = Label(root, text='TIME BETWEEN UPDATES')
my_entry = Entry(root, width=10)

my_label2 = Label(root, text='NUMBER OF ITERATIONS')
my_entry2 = Entry(root, width=10)

# creates the buton that willstart the continuous loop
if do_wrap == True:
    widget = Button(root, bg='#808080', width=20, height=1, command= lambda: continue_doing_something_wrapping(matrix, scale), text='ITERATE OVER TIME')
else:
    widget = Button(root, bg='#808080', width=20, height=1, command= lambda: continue_doing_something_nonwrapping(matrix, scale), text='ITERATE OVER TIME')

my_text = Text(root, width=10, height=1)
my_entry3 = Entry(root, width=10)

# puts the objects on the window
my_button.pack(in_=top, side=LEFT)
my_label.pack(in_=top, side=LEFT)
my_entry.pack(in_=top, side=LEFT)
my_label2.pack(in_=top, side=LEFT)
my_entry2.pack(in_=top, side=LEFT)
widget.pack(in_=top, side=LEFT)
my_text.pack(in_=top, side=LEFT)
my_entry3.pack(in_=top, side=LEFT)

# creates the black box on which the board is displayed
w = Canvas(root, width=len(matrix[0])*scale, height=len(matrix)*scale, bg='#000000')
w.pack()

# puts the initial formation on the board
for new_row in range(len(matrix)):
    for new_col in range(len(matrix[0])):
        if matrix[new_row][new_col] == 1:
            w.create_rectangle(new_col*scale, new_row*scale, new_col*scale+scale, new_row*scale+scale, fill="#ffffff")

# creates the box for changing the color
my_label3 = Label(root, text='COLOR')
my_entry4 = Entry(root, width=10)
my_entry4.insert(10, '#ffffff')
my_label3.pack(in_=bottom, side=LEFT)
my_entry4.pack(in_=bottom, side=LEFT)

root.mainloop()
