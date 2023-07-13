#User function Template for python3
class Solution:
    
    def rotateMatrix(self,arr, n):
        # code here
        n = len(arr)

        # Transpose the matrix
        for i in range(n - 1):
            for j in range(i + 1, n):
                arr[i][j], arr[j][i] = arr[j][i], arr[i][j]

        
        # Reverse the matrix upside down
        for i in range(n):
            self.reverse(arr, 0, n - 1, i)
  
        return


    def reverse(self, arr, start, end, i):
        while start < end:
            arr[start][i], arr[end][i] = arr[end][i], arr[start][i]
            start += 1
            end -= 1


#{ 
 # Driver Code Starts
#Initial Template for Python 3




if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        n = int(input())
        inputLine = list(map(int, input().strip().split()))
        arr = [[0 for j in range(n)] for i in range(n)]
        for i in range(n):
            for j in range(n):
                arr[i][j] = inputLine[i * n + j]
        ob = Solution()
        ob.rotateMatrix(arr, n)
        for i in range(n):
            for j in range(n):
                print(arr[i][j], end=" ")
        print()
        tc -= 1

# } Driver Code Ends