#{ 
 # Driver Code Starts
#Initial Template for Python 3

# } Driver Code Ends
#User function Template for python3

class Solution:
    def solve(self, m, k, bloomDay):
        # Code here
        def isPossible(day):
            count = 0
            bouquets = 0

            for i in bloomDay:
                if i <= day:
                    count += 1
                
                else:
                    bouquets += count // k
                    count = 0

            bouquets += count // k

            if bouquets >= m:
                return True
            
            return False


        # Binary search
        if (m * k) > len(bloomDay):
            return -1 

        low = min(bloomDay)
        high = max(bloomDay)

        minDays = -1

        while low <= high:
            mid = (low + high) // 2

            if isPossible(mid) == True:
                minDays = mid
                high = mid - 1

            else:
                low = mid + 1

        return minDays

#{ 
 # Driver Code Starts.
if __name__ == '__main__': 
    t = int(input ())
    for _ in range (t):
        M, K = list(map(int, input().split()))
        bloomDay = list(map(int, input().split()))
        ob = Solution()
        res = ob.solve(M, K, bloomDay)
        print(res)
# } Driver Code Ends