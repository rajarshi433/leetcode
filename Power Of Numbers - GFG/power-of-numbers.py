#User function Template for python3

class Solution:
    #Complete this function
    def power(self,x,n):
        #Your code here
        
        mod = 1000000007
        
        def helper(x, n):
            if x == 0: return 0
            if n == 0: return 1

            res = helper(x, n // 2) %  mod
            res = (res * res) % mod

            return (x * res) % mod if n % 2 != 0 else res
            
            
        res = helper(x, n)

        return res % mod 


#{ 
 # Driver Code Starts
#Initial Template for Python 3

import math

def main():
    
    T=int(input())
    
    while(T>0):
        
        N=input()
        R=N[::-1]
        
        ob=Solution();
        ans=ob.power(int(N),int(R))
        print(ans)
        
        T-=1

if __name__=="__main__":
    main()
# } Driver Code Ends