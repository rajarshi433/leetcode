#User function Template for python3
class Solution:
	def perfectSum(self, arr, n, s):
		# code here
		
		dp = [[-1 for i in range(s + 1)] for j in range(n + 1)]
		
		return self.f(arr, len(arr) - 1, s, dp)
		
		
    def f(self, arr, idx, s, dp):
        
        mod = 10**9 + 7

        if idx < 0:
            if s == 0:
                return 1
            return 0
        
        if dp[idx][s] != -1:
            return dp[idx][s]
            
        take = 0
        
        if arr[idx] <= s:
            take = self.f(arr, idx - 1, s - arr[idx], dp) % mod
        
    	not_take = self.f(arr, idx - 1, s, dp) % mod
    	
    	dp[idx][s] = (take + not_take) % mod
    	return dp[idx][s]


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		n,sum = input().split()
		n,sum = int(n),int(sum)
		arr = [int(x) for x in input().split()]
		ob = Solution()
		ans = ob.perfectSum(arr,n,sum)
		print(ans)

# } Driver Code Ends