#{ 
 # Driver Code Starts
#Initial Template for Python 3

# } Driver Code Ends
#User function Template for python3

class Solution:
    def count_NGEs(self, N, nums, queries, indices):
        # Code here
        ''' Similar to Count Inversions problem '''

        def merge(enum, low, mid, high, count):
            
            start = low
            end = mid + 1
    
            temp = []
    
            while start <= mid and end <= high:
                if enum[start][1] < enum[end][1]:
                    count[enum[start][0]] += (high - end + 1)
                    temp.append(enum[start])
                    start += 1
    
                else:
                    temp.append(enum[end])
                    end += 1
    
            while start <= mid:
                temp.append(enum[start])
                start += 1
    
            while end <= high:
                temp.append(enum[end])
                end += 1
    
    
            for i in range(low, high + 1):
                enum[i] = temp[i - low]
    
            return count
    
    
        def divide(enum, low, high, count):
            if low == high:
                return 
    
            mid = (low + high) // 2
    
            divide(enum, low, mid, count)
            divide(enum, mid + 1, high, count)
    
            merge(enum, low, mid, high, count)
    
    
        n = len(nums)
        enum = list(enumerate(nums))
        count = [0] * n
    
        divide(enum, 0, n - 1, count)
    
        res = []
    
        for i in indices:
            res.append(count[i])
    
        return res
        
        

#{ 
 # Driver Code Starts.
if __name__ == '__main__': 
    t = int(input ())
    for _ in range (t):
        N = int(input())
        arr = list(map(int, input().split()))
        queries = int(input())
        indices = list(map(int, input().split()))
        ob = Solution()
        NGEs = ob.count_NGEs(N, arr, queries, indices)
        for val in NGEs:
            print(val, end = ' ')
        print()
# } Driver Code Ends