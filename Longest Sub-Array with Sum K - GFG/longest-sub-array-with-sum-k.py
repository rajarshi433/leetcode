#User function Template for python3

class Solution:
    def lenOfLongSubarr (self, arr, n, k) : 
        #Complete the function
        map = {}
        Sum = 0
        length = 0
        
        for i in range(n):
            Sum += arr[i]
            
            if Sum == k:
                length = max(length, i + 1)
                
            elif (Sum - k) in map:
                length = max(length, i - map[Sum - k])
                
            if Sum not in map:
                map[Sum] = i
                
        return length
    



#{ 
 # Driver Code Starts
#Initial Template for Python 3


for _ in range(0,int(input())):
    
    n, k = map(int , input().split())
    arr = list(map(int,input().strip().split()))
    ob = Solution()
    print(ob.lenOfLongSubarr(arr, n, k))




# } Driver Code Ends