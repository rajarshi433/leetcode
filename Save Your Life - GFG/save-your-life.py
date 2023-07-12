#User function Template for python3


class Solution:
    def maxSum (self, w, x, b, n):
        #code here
        sum_ = 0
        maxSum = float('-inf')
        st = 0
        end = 0
        start = 0
        
        for idx, val in enumerate(w):
            
            if sum_ == 0:
                st = idx
            
            if val in x:
                index = x.index(val)
                sum_ += b[index]
            else:
                sum_ += ord(val)
                
            if sum_ > maxSum:
                maxSum = sum_
                start = st
                end = idx
            
            if sum_ < 0:
                sum_ = 0
                
        return w[start: end+1]


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        w = input()
        n = int(input())
        x = input().split(' ')
        b = input().split(' ')
        for itr in range(n):
            b[itr] = int(b[itr])
       

        ob = Solution()
        print(ob.maxSum(w,x,b,n))
# } Driver Code Ends