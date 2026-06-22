matrix=[[1,3,4],[34,5,6],[7,8,9]]
print(matrix[0])
print(matrix[1][2])
print(matrix[2][-1])

#traverse matrix
for row in matrix:
    for val in row:
        print(val,end="")