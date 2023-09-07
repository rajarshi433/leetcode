#User function Template for python3

#User function Template for python3
class Solution:
    def armstrongNumber (self, n):
        # code here 
        
        num = n
        Sum = 0
        
        while num != 0:
            Sum = Sum + (num % 10) ** 3
            num = num // 10
            
        if Sum == n:
            return 'Yes'
            
        return 'No'


#{ 
 # Driver Code Starts
#Initial Template for Python 3
if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        n = input()
        n=int(n)
        ob = Solution()
        print(ob.armstrongNumber(n))
# } Driver Code Ends