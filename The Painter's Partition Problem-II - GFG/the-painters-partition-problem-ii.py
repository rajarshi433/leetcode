#User function Template for python3

class Solution:
    def minTime (self, boards, n, k):
        #code here
        def count(capacity):
            painters = 1
            time = 0
    
            for i in boards:
                if time + i <= capacity:
                    time += i
                
                else:
                    painters += 1
                    time = i
    
            return painters
    
    
    
        # Binary Search
        low = max(boards)
        high = sum(boards)
    
        ans = -1
    
        while low <= high:
            mid = (low + high) // 2
    
            painters = count(mid)
            
            if painters > k:
                low = mid + 1
    
            else:
                ans = mid
                high = mid - 1
    
        
        return ans
        


#{ 
 # Driver Code Starts
#Initial Template for Python 3


if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        str = input().split()
        k = int(str[0])
        n = int(str[1])
        arr = input().split()
        for itr in range(n):
            arr[itr] = int(arr[itr])

        ob = Solution()
        print(ob.minTime(arr,n,k))
# } Driver Code Ends