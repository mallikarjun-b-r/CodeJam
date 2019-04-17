def Solve(str1,str2):
    str1=str(str1)
    str2=str(str2)
    matrix = [[0 for i in range (len(str1)+1)] for j in range(len(str2)+1)]
    i=len(str1)-1

    while(i >=0):
        j=len(str2)-1
        while(j>=0):
            print(i,j)
            if(str1[j]==str2[i]):
                matrix[i][j]=1+matrix[i+1][j+1]
            else:
                matrix[i][j]=0
            j-=1
        i-=1
    return matrix
print(Solve('secret','bisect'))
s='secret'
print(s[0]==s[0])




