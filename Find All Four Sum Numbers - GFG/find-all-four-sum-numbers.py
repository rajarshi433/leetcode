#User function Template for python3

# arr[] : int input array of integers
# k : the quadruple sum required
class Solution:
    def fourSum(self, nums, target):
        # code here
        nums.sort()

        res = []
        n = len(nums)

        for i in range(n):

            if i > 0 and nums[i - 1] == nums[i]:
                continue

            for j in range(i + 1, n):

                if j > i + 1 and nums[j - 1] == nums[j]:
                    continue

                l = j + 1
                r = n - 1

                while l < r:
                    Sum = nums[i] + nums[j] + nums[l] + nums[r]

                    if Sum < target:
                        l += 1
                    elif Sum > target:
                        r -= 1
                    else:
                        res.append([nums[i], nums[j], nums[l], nums[r]])
                        
                        l += 1
                        while l < r and nums[l - 1] == nums[l]:
                            l += 1

        return res


#{ 
 # Driver Code Starts
#Initial Template for Python 3


#Main
if __name__=='__main__':
    t = int(input())
    while t:
        t-=1
        n, k=map(int,input().split())
        # print(n, k)
        a=list(map(int,input().strip().split()))[:n]
        # print(a)
        ob=Solution()
        ans=ob.fourSum(a, k)
        # print(ans)
        for v in ans:
            for u in v:
                print(u, end=" ")
            print("$", end="")
        if(len(ans)==0):
            print(-1, end="")
        print()
        
        

# } Driver Code Ends