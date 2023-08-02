#User function Template for python3

'''
    :param head: head of unsorted linked list 
    :return: head of sorted linkd list
    
    # Node Class
    class Node:
        def __init__(self, data):  # data -> value stored in node
            self.data = data
            self.next = None
'''
class Solution:
    #Function to sort the given linked list using Merge Sort.
    def mergeSort(self, head):
        
        def merge(list1, list2):
            dummy = Node(0)
            temp = dummy
            
            while list1 and list2:
                if list1.data <= list2.data:
                    temp.next = list1
                    temp = temp.next
                    list1 = list1.next

                else:
                    temp.next = list2
                    temp = temp.next
                    list2 = list2.next

            if list1:
                temp.next = list1

            if list2:
                temp.next = list2

            return dummy.next


        def getMid(head):
            slow = head
            fast = head.next.next

            while fast and fast.next:
                slow = slow.next
                fast = fast.next.next

            return slow


        def sort(head):
            if not head or not head.next:
                return head

            mid = getMid(head)

            left = head
            right = mid.next
            mid.next = None

            left_list = sort(left)
            right_list = sort(right)

            return merge(left_list, right_list)


        return sort(head)
        


#{ 
 # Driver Code Starts
#Initial Template for Python 3
import atexit
import io
import sys

# Contributed by : Nagendra Jha

# Node Class
class Node:
    def __init__(self, data):  # data -> value stored in node
        self.data = data
        self.next = None


# Linked List Class
class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    # creates a new node with given value and appends it at the end of the linked list
    def append(self, new_value):
        new_node = Node(new_value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node    
            return
        self.tail.next = new_node
        self.tail = new_node

# prints the elements of linked list starting with head
def printList(head):
    if head is None:
        print(' ')
        return
    curr_node = head
    while curr_node:
        print(curr_node.data,end=" ")
        curr_node=curr_node.next
    print(' ')


if __name__ == '__main__':
    t=int(input())
    for cases in range(t):
        n = int(input())
        p = LinkedList() # create a new linked list 'a'.
        nodes_p = list(map(int, input().strip().split()))
        for x in nodes_p:
            p.append(x)  # add to the end of the list

        printList(Solution().mergeSort(p.head))

# } Driver Code Ends