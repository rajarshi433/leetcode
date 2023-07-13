#User function Template for python3


#Function to modify the matrix such that if a matrix cell matrix[i][j]
#is 1 then all the cells in its ith row and jth column will become 1.
def booleanMatrix(matrix):
    # code here 
    rows = len(matrix)
    cols = len(matrix[0])

    col00 = 0

    for r in range(rows):
        for c in range(cols):
            if matrix[r][c] == 1:

                matrix[r][0] = 1

                if c == 0:
                    col00 = 1
                else:
                    matrix[0][c] = 1


    for r in range(1, rows):
        for c in range(1, cols):
            if matrix[0][c] == 1 or matrix[r][0] == 1:
                matrix[r][c] = 1

    
    if matrix[0][0] == 1:
        for i in range(cols):
            matrix[0][i] = 1

    if col00 == 1:
        for i in range(rows):
            matrix[i][0] = 1



#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        r,c = map(int, input().strip().split())
        matrix = []
        for i in range(r):
            line = [int(x) for x in input().strip().split()]
            matrix.append(line)
        booleanMatrix(matrix)
        for i in range(r):
            for j in range(c):
                print(matrix[i][j], end=' ')
            print()


# } Driver Code Ends