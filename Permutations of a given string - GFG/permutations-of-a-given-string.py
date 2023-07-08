#User function Template for python3

class Solution:
    def find_permutation(self, S):
        
        def f(arr, idx, res):
            
            if idx >= len(arr):
                tempStr = ''.join(arr[::])
                res.add(tempStr)
            
            for i in range(idx, len(arr)):
                
                arr[idx], arr[i] = arr[i], arr[idx] # swap
                f(arr, idx + 1, res)
                arr[i], arr[idx] = arr[idx], arr[i] # re swap
                
        
        arr = list(S)
        arr.sort()
        
        res = set()
        
        f(arr, 0, res)
        
        return list(res)
                
        



#{ 
 # Driver Code Starts
#Initial Template for Python 3


if __name__ == '__main__':
	t=int(input())
	for i in range(t):
		S=input()
		ob = Solution()
		ans = ob.find_permutation(S)
		ans.sort()
		for i in ans:
			print(i,end=" ")
		print()
# } Driver Code Ends