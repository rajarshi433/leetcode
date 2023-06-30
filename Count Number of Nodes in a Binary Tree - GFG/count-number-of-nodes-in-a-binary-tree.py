#{ 
 # Driver Code Starts
#Initial Template for Python 3

# } Driver Code Ends
#User function Template for python3

'''
# Node Class:
class Node:
    def init(self, val):
        self.data = val
        self.left = None
        self.right = None
'''
class Solution:
    def countNodes(self, root):
        #code here
        if root == None:
            return 0
            
        left = 1 + self.countLeft(root.left)
        right = self.countLeft(root.right)
    
        if left == right:
            return 2**left - 1
    
        else:
            return 1 + self.countNodes(root.left) + self.countNodes(root.right)


    def countRight(self, root):
        count = 0

        while root:
            count += 1
            root = root.right

        return count

    def countLeft(self, root):
        count = 0

        while root:
            count += 1
            root = root.left

        return count

#{ 
 # Driver Code Starts.
from collections import deque

class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None
        
def constructTree(idx, arr):
    if idx >= len(arr):
        return None
    root = Node(arr[idx])
    root.left = constructTree(2 * idx + 1, arr)
    root.right = constructTree(2 * idx + 2, arr)
    return root
        
if __name__ == '__main__': 
    t = int(input ())
    for _ in range (t):
        n = int(input())
        v = list(map(int, input().split()))
        root = constructTree(0, v)
        obj = Solution()
        print(obj.countNodes(root))
# } Driver Code Ends