#User function Template for python3

'''
class Node:
            def __init__(self, data):
                self.data = data
                self.left = self.right = None
'''

#Function to return a tree created from postorder and inoreder traversals.
def buildTree(inorder, postorder, n):
    # your code here
    map = {}

    for idx, item in enumerate(inorder):
        map[item] = idx

    root = f(postorder, 0, len(postorder) - 1, inorder, 0, len(inorder) - 1, map)

    return root


def f(postorder, postStart, postEnd, inorder, inStart, inEnd, map):

    if postStart > postEnd or inStart > inEnd:
        return None


    root = Node(postorder[postEnd])

    inRoot = map[root.data]
    numsLeft = inRoot - inStart

    root.left = f(postorder, postStart, postStart + numsLeft - 1, inorder, inStart, inRoot - 1, map)
    root.right = f(postorder, postStart + numsLeft, postEnd - 1, inorder, inRoot + 1, inEnd, map)

    return root



#{ 
 # Driver Code Starts
#Initial Template for Python 3
import atexit
import io
import sys
from collections import  defaultdict

#Contributed by : PranchalK


_INPUT_LINES = sys.stdin.read().splitlines()
input = iter(_INPUT_LINES).__next__
_OUTPUT_BUFFER = io.StringIO()
sys.stdout = _OUTPUT_BUFFER

@atexit.register

def write():
    sys.__stdout__.write(_OUTPUT_BUFFER.getvalue())



# Helper function that allocates  
# a new node  
class Node:
    def __init__(self, data):
        self.data = data
        self.left = self.right = None

# This funtcion is here just to test  
def preOrder(node):
    if node == None:
        return
    print(node.data, end=" ")
    preOrder(node.left)
    preOrder(node.right)
    
if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases):
        n = int(input())  # number of nodes in tree
        in_order = list(map(int, input().strip().split()))  # parent child info in list
        post_order = list(map(int, input().strip().split()))  # parent child info in list
        preOrder(buildTree(in_order,post_order,n))
        print()


# } Driver Code Ends