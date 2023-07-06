#User function Template for python3

class Solution:
    def goodNumbers(self,L,R,D):
        #code here
        
        
        def validate(n, D):
            prev = n % 10
            
            if prev == D:
                return False
                
            n = n // 10
            
            while n > 0:
                if n % 10 == D or n % 10 <= prev:
                    return False
                    
                prev = prev + (n % 10)
                n = n // 10
                
            return True
            
        res = []
        for i in range(L, R + 1):
            if validate(i, D):
                res.append(i)
                
        return res
            
                
                



#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__=='__main__':
    t=int(input())
    for _ in range(t):
        L,R,D=map(int,input().strip().split())
        ob=Solution()
        ans=ob.goodNumbers(L,R,D)
        for i in ans:
            print(i,end=" ")
        print()
# } Driver Code Ends