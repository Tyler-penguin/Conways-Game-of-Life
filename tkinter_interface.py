from tkinter import *
from defs import *


matrix = csv_to_matrix('initial_population.csv')
def do_something(matrix):
    matrix = iteration_nonwrapping(matrix)
#    display_game(matrix, 'O', '.')


    for new_row in range(len(matrix)):
        for new_col in range(len(matrix[0])):
            if matrix[new_row][new_col] == 0:
                w.create_rectangle(new_col*10, new_row*10, new_col*10+10, new_row*10+10, fill="#000000")
            else:
                w.create_rectangle(new_col*10, new_row*10, new_col*10+10, new_row*10+10, fill="#ffffff")

root = Tk()
root.state('zoomed')

my_button = Button(root, bg='#808080', width=10, command= lambda: do_something(matrix), height=1, text='ITERATE')
my_button.pack()
w = Canvas(root, width=len(matrix[0])*10, height=len(matrix)*10)
w.pack()
for new_row in range(len(matrix)):
    for new_col in range(len(matrix[0])):
        if matrix[new_row][new_col] == 0:
            w.create_rectangle(new_col*10, new_row*10, new_col*10+10, new_row*10+10, fill="#000000")
        else:
            w.create_rectangle(new_col*10, new_row*10, new_col*10+10, new_row*10+10, fill="#ffffff")

root.mainloop()
