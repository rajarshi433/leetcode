#User function Template for python3
class Solution:
	def subsetSums(self, arr, N):
		
		def f(arr, idx, sum_, res):
		    
		    if idx < 0:
		        res.append(sum_)
		        return
		    
		    f(arr, idx - 1, sum_ + arr[idx], res)
		    f(arr, idx - 1, sum_, res)
		    
        
        res = []
        
        f(arr, N - 1, 0, res)
        
        return sorted(res)
		    
		    
		    
		    


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    T=int(input())
    for i in range(T):
        N = int(input())
        arr = [int(x) for x in input().split()]
        ob = Solution()
        ans = ob.subsetSums(arr, N)
        ans.sort()
        for x in ans:
            print(x,end=" ")
        print("")

# } Driver Code Ends