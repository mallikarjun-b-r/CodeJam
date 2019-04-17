#0,0 -> 5,10 (2,4) and (4,4) blocker (1363)
def Solve(matrix):

    for i in range(11):
        for j in range (6):

            if((i==4 and j==2) or (i==4 and j==4)):
                continue
            if(j==0 and i!=0):
                matrix[i][j] = matrix[i-1][0]
            elif(i==0 and j!=0):
                matrix[i][j] = matrix[0][j-1]
            else:
                if(i==2 and j==4):
                    print(matrix[i-1][j] , matrix[i][j-1])
                matrix[i][j] = matrix[i-1][j] + matrix[i][j-1]
                matrix[0][0]=1

    return matrix
def SolveRecursive(a,b):
    if(a==0 or b==0):
        return 1
    if(a==2 or a==4) and b==4:
        return 0
    return SolveRecursive(a-1,b)+SolveRecursive(a,b-1)






matrix = [[0 for i in range(6)] for j in range(11)]
matrix[0][0]=1

for x in matrix:
    print(x)
Solve(matrix)
for x in matrix:
    print(x)

print(matrix[0][1],matrix[1][0],len(matrix))

print("recursive",SolveRecursive(5,10))


