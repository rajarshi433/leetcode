#User function Template for python3

class Solution:
	def NthRoot(self, n, m):
		# Code here
		def f(mid, n, m):
            num = 1
    
            while n >= 1:
                num = mid * num
    
                if num > m:
                    return 1
                
                n -= 1
    
            if num < m:
                return -1
    
            if num == m:
                return 0

        

        low = 1
        high = m
    
        while low <= high:
            mid = (low + high) // 2
    
            if f(mid, n, m) == 0:
                return mid
    
            if f(mid, n, m) > 0:
                high = mid - 1
    
            elif f(mid, n, m) < 0:
                low = mid + 1
    
    
        return -1


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		n, m = input().split()
		n = int(n); m = int(m);
		ob = Solution()
		ans = ob.NthRoot(n, m)
		print(ans)
# } Driver Code Ends