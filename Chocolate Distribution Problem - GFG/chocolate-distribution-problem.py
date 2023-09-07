#User function Template for python3

class Solution:

    def findMinDiff(self, a, n, m):
        a.sort()
        
        low = 0
        high = m - 1
        ans = float('inf')
        
        for i in range(high, n):
            ans = min(ans, a[i] - a[low])
            low += 1
            
        return ans
            
            

        


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':

    t = int(input())

    for _ in range(t):
        N = int(input())
        A = [int(x) for x in input().split()]
        M = int(input())


        solObj = Solution()

        print(solObj.findMinDiff(A,N,M))
# } Driver Code Ends