from tkinter import *
from defs import *
import time

matrix = csv_to_matrix('initial_population.csv')
def do_something(matrix):
    matrix = iteration_nonwrapping(matrix)
#    display_game(matrix, 'O', '.')

    w.delete("all")

    for new_row in range(len(matrix)):
        for new_col in range(len(matrix[0])):
            if matrix[new_row][new_col] == 0:
                w.create_rectangle(new_col*10, new_row*10, new_col*10+10, new_row*10+10, fill="#000000")
            else:
                w.create_rectangle(new_col*10, new_row*10, new_col*10+10, new_row*10+10, fill="#ffffff")

def continue_doing_something(matrix):
    frequency = my_entry.get()
    time_for_iterations = my_entry2.get()
    total_iterations = int(float(frequency) * float(time_for_iterations))
    time_between = 1/ float(frequency)
    for iteration in range(total_iterations):

        do_something(matrix)

        time.sleep(time_between)

        root.update()

    print(frequency, time_for_iterations, total_iterations)
    my_text.delete(1.0, END)
    my_text.insert(END, 'DONE')


root = Tk()
root.state('zoomed')

top = Frame(root)
bottom = Frame(root)
top.pack(side=TOP)
bottom.pack(side=BOTTOM, fill=BOTH, expand=True)

my_button = Button(root, bg='#808080', width=20, command= lambda: do_something(matrix), height=1, text='ITERATE ONCE')

my_label = Label(root, text='TIMES PER SECOND')
my_entry = Entry(root, width=10)

my_label2 = Label(root, text='TIME')
my_entry2 = Entry(root, width=10)


widget = Button(root, bg='#808080', width=20, height=1, command= lambda: continue_doing_something(matrix), text='ITERATE OVER TIME')

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
