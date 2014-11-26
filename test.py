def genMatrix(rows,cols):
    matrix = [[0 for col in range(cols)] for row in range(rows)]
    for i in range(rows):
        for j in range(cols):
            print matrix[i][j],
        print '\n'

genMatrix(5,5)
