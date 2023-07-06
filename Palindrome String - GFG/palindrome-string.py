#User function Template for python3
class Solution:
	def isPalindrome(self, S):
		# code here
		
		l = 0
		r = len(S) - 1
		
		while l < r:
		    if S[l] != S[r]:
		        return 0
            else:
                l += 1
                r -= 1
                
        return 1


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		S = input()
		ob = Solution()
		answer = ob.isPalindrome(S)
		print(answer)

# } Driver Code Ends