#User function Template for python3

class Solution:
    def rearrange(self, nums, n):
        # code here
        pos = []
        neg = []
        
        for i in nums:
            if i < 0:
                neg.append(i)
            else:
                pos.append(i)
        
            
        l = min(len(pos), len(neg))
        
        for i in range(l):
            nums[i*2] = pos[i]
            nums[i*2 + 1] = neg[i]
        
            
        if len(neg) < len(pos):
            for i in range(2*l, len(nums)):
                nums[i] = pos[l]
                l += 1
        else:
            for i in range(2*l, len(nums)):
                nums[i] = neg[l]
                l += 1
                
        # return nums
            
                
        


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
	tc = int(input())
	while tc > 0:
		n = int(input())
		arr = list(map(int, input().strip().split()))
		ob = Solution()
		ob.rearrange(arr, n)
		for x in arr:
			print(x, end=" ")
		print()
		tc -= 1

# } Driver Code Ends