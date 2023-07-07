class Solution:

    def sorted(self, s):
        
        if len(s) == 0:
            return
        
        num = s.pop()
        self.sorted(s)
        
        self.sortedInsert(s, num)
        

    def sortedInsert(self, s, num):
        
        if len(s) == 0 or s[-1] < num:
            s.append(num)
            return
            
        temp = s.pop()
        self.sortedInsert(s, num)
        
        s.append(temp)
        
        
    
        
        
        



#{ 
 # Driver Code Starts
if __name__=='__main__':
    t = int(input())
    for i in range(t):
        n = int(input())
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        ob.sorted(arr)
        for e in range(len(arr)):
            print(arr.pop(), end=" ")
        print()


# } Driver Code Ends