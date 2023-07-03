#User function Template for python3

class Solution:
	def singleNumber(self, nums):
		# Code here
		x_xor_y = 0

        for num in nums:
            x_xor_y = x_xor_y ^ num

        rmsbm = x_xor_y & -x_xor_y

        x = 0
        y = 0

        for num in nums:
            if rmsbm & num == 0:
                x = x ^ num
            else:
                y = y ^ num

        return sorted([x, y])



#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		n = int(input())
		v = list(map(int,input().split()))
		ob = Solution();
		ans = ob.singleNumber(v)
		for i in ans:
			print(i, end = " ")
		print()

# } Driver Code Ends