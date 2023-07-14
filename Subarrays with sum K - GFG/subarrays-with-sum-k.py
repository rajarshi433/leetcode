#User function Template for python3

class Solution:
    def findSubArraySum(self, nums, N, k):
        # code here
        map = {
            0 : 1
        }
        count = 0
        sum_ = 0

        for i in nums:
            sum_ += i

            if (sum_ - k) in map.keys():
                count += map[sum_ - k]

            map[sum_] = map.get(sum_, 0) + 1

        return count


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range (t):
        N = int(input())
        Arr = input().split()
        for itr in range(N):
            Arr[itr] = int(Arr[itr])
        k = int(input())
        ob = Solution()
        print(ob.findSubArraySum(Arr, N, k))
# } Driver Code Ends