from tkinter import *
from defs import *


matrix = csv_to_matrix('initial_population.csv')
def do_something(matrix):
    matrix = iteration(matrix)
#    display_game(matrix, 'O', '.')

    for new_row in range(len(matrix)):
        for new_col in range(len(matrix[0])):
            if matrix[new_row][new_col] == 0:
                my_button = Button(root, bg='#000000', width=1, command= lambda: do_something(matrix), height=1, bd=1)
                my_button.grid(row=new_row, column=new_col)
            else:
                my_button = Button(root, bg='#ffffff', width=1, command= lambda: do_something(matrix), height=1, bd=1)
                my_button.grid(row=new_row, column=new_col)



root = Tk()
root.state('zoomed')

for new_row in range(len(matrix)):
    for new_col in range(len(matrix[0])):
        if matrix[new_row][new_col] == 0:
            my_button = Button(root, bg='#000000', width=1, command= lambda: do_something(matrix), height=1, bd=0)
            my_button.grid(row=new_row, column=new_col)
        else:
            my_button = Button(root, bg='#ffffff', width=1, command= lambda: do_something(matrix), height=1, bd=0)
            my_button.grid(row=new_row, column=new_col)


root.mainloop()
