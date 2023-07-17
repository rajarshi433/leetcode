#User function Template for python3
class Solution:

	# Function to find maximum
	# product subarray
	def maxProduct(self, arr, n):
		# code here
		pref, suff = 1, 1

        Max = float('-inf')

        for i in range(n):
            if pref == 0:
                pref = 1
            if suff == 0:
                suff = 1

            pref = pref * arr[i]
            suff = suff * arr[n - i - 1]

            Max = max(Max, pref, suff)

        return Max


#{ 
 # Driver Code Starts
#Initial Template for Python 3



if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        n = int(input())
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        ans = ob.maxProduct(arr, n)
        print(ans)
        tc -= 1

# } Driver Code Ends