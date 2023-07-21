#User function Template for python3

class Solution:
    def solve(self, n, k, stalls):
        def placeCows(dist):
            count = 1
            last = stalls[0]
    
            for s in stalls:
                if (s - last) >= dist:
                    count += 1
                    last = s
    
                if count == k:
                    return True
    
            return False


        # Binary Search
        stalls.sort()
    
        low = 1
        high = stalls[-1]
    
        ans = -1
    
        while low <= high:
            mid = (low + high) // 2
    
            if placeCows(mid) == True:
                ans = mid
                low = mid + 1
    
            else:
                high = mid - 1
    
        return ans


#{ 
 # Driver Code Starts
#Initial Template for Python 3

def main():

    T = int(input())

    while(T > 0):
        n, k = list(map(int, input().split()))
        stalls = list(map(int, input().split()))
        ob = Solution()
        res = ob.solve(n, k, stalls)
        print(res)

        T -= 1


if __name__ == "__main__":
    main()
# } Driver Code Ends