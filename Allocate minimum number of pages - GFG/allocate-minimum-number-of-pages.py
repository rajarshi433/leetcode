class Solution:
    
    #Function to find minimum number of pages.
    def findPages(self, arr, N, M):
        #code here
        def countStudents(pages):
            student = 1
            holding = 0
    
            for i in arr:
                if holding + i <= pages:
                    holding += i
                
                else:
                    student += 1
                    holding = i
    
            return student
    
    
    
        # Binary Search
        if M > N:
            return - 1
            
        low = max(arr)
        high = sum(arr)
    
        ans = float('inf')
    
        while low <= high:
            mid = (low + high) // 2
    
            students = countStudents(mid)

            if students > M:
                low = mid + 1
    
            else:
                ans = mid
                high = mid - 1
    
        
        return ans




#{ 
 # Driver Code Starts
#Initial Template for Python 3

#contributed by RavinderSinghPB
if __name__=='__main__':
    t=int(input())
    for _ in range(t):
        
        n=int(input())
        
        arr=[int(x) for x in input().strip().split()]
        m=int(input())
        
        ob=Solution()
        
        print(ob.findPages(arr,n,m))
# } Driver Code Ends