class Solution:
    #Back-end complete function Template for Python 3
    
    #Function to find the leaders in the array.
    def leaders(self, A, N):
        
        maxRight = float('-inf')
        
        leaders = []
        
        for i in range(N - 1, -1, -1):
            if A[i] >= maxRight:
                leaders.append(A[i])
                maxRight = A[i]
                
        # reverse the leaders array for ans
        l = 0
        r = len(leaders) - 1
        
        while(l < r):
            leaders[l], leaders[r] = leaders[r], leaders[l]
            l += 1
            r -= 1
                
        return leaders

#{ 
 # Driver Code Starts
#Initial Template for Python 3

import math


    
def main():
    
    T=int(input())
    
    while(T>0):
        
        
        N=int(input())
        
        A=[int(x) for x in input().strip().split()]
        obj = Solution()
        
        A=obj.leaders(A,N)
        
        for i in A:
            print(i,end=" ")
        print()
        
        T-=1

if __name__=="__main__":
    main()
# } Driver Code Ends