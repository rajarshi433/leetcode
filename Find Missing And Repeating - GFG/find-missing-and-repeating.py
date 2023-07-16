#User function Template for python3

class Solution:
    def findTwoElement( self, arr, n): 
        # code here
        n = len(arr)

        SumN = (n * (n + 1)) // 2 
        Sum2N = (n * (n + 1) * ((2 * n) + 1)) // 6
        
        S, S2 = 0, 0
        
        for i in arr:
            S += i
            S2 += i**2
        
        val1 = S - SumN
        val2 = S2 - Sum2N
        
        val3 = val2 // val1
        
        repeating = (val1 + val3) // 2
        missing = repeating - val1
        
        return [repeating, missing]


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 

    tc=int(input())
    while tc > 0:
        n=int(input())
        arr=list(map(int, input().strip().split()))
        ob = Solution()
        ans=ob.findTwoElement(arr, n)
        print(str(ans[0])+" "+str(ans[1]))
        tc=tc-1
# } Driver Code Ends