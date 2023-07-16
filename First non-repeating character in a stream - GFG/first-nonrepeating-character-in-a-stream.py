#User function Template for python3
from collections import deque

class Solution:
	def FirstNonRepeating(self, A):
		# Code here
        appeared_count = [0] * 26
        appeared_queue = deque()
        ans = []
        
        for s in A:
            i = ord(s) - ord("a")
            appeared_count[i] += 1
            
            if appeared_count[i] == 1:
                appeared_queue.append(i)
                
            while appeared_queue and appeared_count[appeared_queue[0]] > 1:
                appeared_queue.popleft()
                
            if appeared_queue:
                ans.append(chr(appeared_queue[0] + ord("a")))
            else:
                ans.append("#")
                
        return "".join(ans)


#{ 
 # Driver Code Starts

#Initial Template for Python 3

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		A = input()
		ob = Solution()
		ans = ob.FirstNonRepeating(A)
		print(ans)

# } Driver Code Ends