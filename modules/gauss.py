import numpy as np

def get_next_identity_number(matrix, rows, columns):
    for row in range(rows['current'], rows['total']):
        if matrix[row, columns['current']] == 0:
            continue
        else:
            aux = matrix[rows['current']]
            matrix[rows['current']] = matrix[row]
            matrix[row] = aux
            if matrix[rows['current'], columns['current']] != 1:
                matrix[rows['current']] = matrix[rows['current']]/matrix[rows['current'], columns['current']]
                break
    return matrix

def organize(matrix, rows, columns):
    for row in range(rows['current']+1, rows['total']):
        if np.all(matrix[row] == 0):
            aux = matrix[row]
            matrix = np.delete(matrix, row, axis = 0)
            matrix = np.vstack((matrix, aux))
            rows['total'] -=1
            return organize(matrix, rows, columns)
    return matrix
            

def escalonate(matrix, rows, columns):
    for row in range(rows['current']+1, rows['total']):

        #Gets the multiplier scalar and multiplied identity row for elimination
        operator = -matrix[row, columns['current']]
        op_row = matrix[rows['current']]*operator

        matrix[row] = matrix[row]+op_row
    return organize(matrix, rows, columns)


def gauss_elimination(mtx):
    matrix = np.array(mtx, dtype= np.float64)
    
    #Stores the row we are currently operating and the row size
    rows = {
        'current': 0,
        'total': matrix.shape[0]
    }
    #Stores the column we are currently operating de the column size (of possible identities)
    columns = {
        'current': 0,
        'total': matrix.shape[1]-1
    }
    while rows['current'] < rows['total']:
        matrix = get_next_identity_number(matrix, rows, columns)
        matrix = escalonate(matrix, rows, columns)
        rows['current'] += 1
        columns['current'] += 1

    return matrix