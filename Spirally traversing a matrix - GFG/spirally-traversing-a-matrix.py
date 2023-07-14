#User function Template for python3

class Solution:
    
    #Function to return a list of integers denoting spiral traversal of matrix.
    def spirallyTraverse(self,matrix, r, c): 
        # code here 
        row = len(matrix)
        col = len(matrix[0])

        left = 0
        right = col - 1
        top = 0
        bottom = row - 1

        ans = []

        while left <= right and top <= bottom:

            for i in range(left, right + 1):
                ans.append(matrix[top][i])

            top += 1

            for i in range(top, bottom + 1):
                ans.append(matrix[i][right])

            right -= 1

            if top <= bottom: # if there is only a single row
                for i in range(right, left - 1, -1):
                    ans.append(matrix[bottom][i])

            bottom -= 1

            if left <= right: # if there is only a single column
                for i in range(bottom, top - 1, -1):
                    ans.append(matrix[i][left])

            left += 1


        return ans



#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        r,c = map(int, input().strip().split())
        values = list(map(int, input().strip().split()))
        k = 0
        matrix =[]
        for i in range(r):
            row=[]
            for j in range(c):
                row.append(values[k])
                k+=1
            matrix.append(row)
        obj = Solution()
        ans = obj.spirallyTraverse(matrix,r,c)
        for i in ans:
            print(i,end=" ")
        print()

# } Driver Code Ends