import os
import csv

def iteration(matrix):
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

    for row in range(rowlen):
        for col in range(collen):
            sum = 0
            for rowcounter in range(3):
                for colcounter in range(3):
                    sum += padded_matrix[rowcounter+row][colcounter+col]
            if matrix[row][col] == 0:
                if sum == 3:
                    matrix[row][col] = 1
            else:
                if sum != 3:
                    if sum != 4:
                        matrix[row][col] = 0
    return matrix

def csv_to_matrix(filename):
    counter = -1
    matrix = []
    my_dir = os.path.dirname(os.path.realpath(__file__))
    filename = my_dir + '/' + filename
    tuple_list=[]
    with open(filename, 'r')  as f:
        read_csv= csv.reader(f)
        for row in read_csv:
            counter += 1
            matrix.append([])
            for item in row:
                matrix[counter].append(int(item))
    return matrix

def display_game(matrix, live_symbol, dead_symbol):
    for row in matrix:
        for col in row:
            if col == 1:
                print(live_symbol, end=' ')
            else:
                print(dead_symbol, end=' ')
        print('')
    print('')

matrix = csv_to_matrix('initial_population.csv')

for i in range(10000):
     matrix = iteration(matrix)
     display_game(matrix, 'O', '.')
