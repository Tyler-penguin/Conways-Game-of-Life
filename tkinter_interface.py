from tkinter import *
from defs import *
import time

do_wrap = True


matrix = csv_to_matrix('initial_population.csv')
def do_something(matrix, do_wrap):
    if do_wrap == True:
        matrix = iteration_wrapping(matrix)
    else:
        matrix = iteration_nonwrapping(matrix)
#    display_game(matrix, 'O', '.')

    w.delete("all")

    for new_row in range(len(matrix)):
        for new_col in range(len(matrix[0])):
            if matrix[new_row][new_col] == 0:
                w.create_rectangle(new_col*10, new_row*10, new_col*10+10, new_row*10+10, fill="#000000")
            else:
                w.create_rectangle(new_col*10, new_row*10, new_col*10+10, new_row*10+10, fill="#ffffff")

def continue_doing_something(matrix, do_wrap):
    time_between = float(my_entry.get())
    number_of_iterations = int(my_entry2.get())
    iterations_remaining = number_of_iterations

    for iteration in range(number_of_iterations):

        do_something(matrix, do_wrap)
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

my_button = Button(root, bg='#808080', width=20, command= lambda: do_something(matrix, do_wrap), height=1, text='ITERATE ONCE')

my_label = Label(root, text='TIME BETWEEN UPDATES')
my_entry = Entry(root, width=10)

my_label2 = Label(root, text='NUMBER OF ITERATIONS')
my_entry2 = Entry(root, width=10)


widget = Button(root, bg='#808080', width=20, height=1, command= lambda: continue_doing_something(matrix, do_wrap), text='ITERATE OVER TIME')

my_text = Text(root, width=10, height=1)

my_entry3 = Entry(root, width=10)

my_button.pack(in_=top, side=LEFT)
my_label.pack(in_=top, side=LEFT)
my_entry.pack(in_=top, side=LEFT)
my_label2.pack(in_=top, side=LEFT)
my_entry2.pack(in_=top, side=LEFT)
widget.pack(in_=top, side=LEFT)
my_text.pack(in_=top, side=LEFT)

w = Canvas(root, width=len(matrix[0])*10, height=len(matrix)*10)
w.pack()
for new_row in range(len(matrix)):
    for new_col in range(len(matrix[0])):
        if matrix[new_row][new_col] == 0:
            w.create_rectangle(new_col*10, new_row*10, new_col*10+10, new_row*10+10, fill="#000000")
        else:
            w.create_rectangle(new_col*10, new_row*10, new_col*10+10, new_row*10+10, fill="#ffffff")

root.mainloop()
