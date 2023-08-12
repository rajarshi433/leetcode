# Doubly Linked List
class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.next = None
        self.prev = None


class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.map = {}
        
        self.head = Node(-1, -1)
        self.tail = Node(-1, -1)
        self.head.next = self.tail
        self.tail.prev = self.head


    def get(self, key: int) -> int:
        
        if key in self.map:
            # Get key
            node = self.map[key]
            res = node.val

            # Delete key
            del self.map[key]
            self.deleteNode(node)

            # Insert key
            self.insertNode(key, res)

            return res

        else:
            return -1


    def set(self, key: int, val: int) -> None:

        if key in self.map:
            # Delete key
            node = self.map[key]
            del self.map[key]
            self.deleteNode(node)

            # Insert key
            self.insertNode(key, val)

        elif len(self.map) == self.capacity:
            # Delete key from tail
            node = self.tail.prev
            del self.map[node.key]
            self.deleteNode(node)
            
            # Insert key
            self.insertNode(key, val)

        else:
            # Insert key
            self.insertNode(key, val)
            

    def deleteNode(self, node):
        prevNode = node.prev
        nextNode = node.next
        prevNode.next = nextNode
        nextNode.prev = prevNode


    def insertNode(self, key, val):
        newNode = Node(key, val)
        self.map[key] = newNode

        temp = self.head.next
        self.head.next = newNode
        newNode.prev = self.head
        temp.prev = newNode
        newNode.next = temp




#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases):
        cap = int(input())  # capacity of the cache
        qry=int(input())  #number of queries
        a = list(map(str, input().strip().split()))  # parent child info in list
        
        lru=LRUCache(cap)
        
       
        i=0
        q=1
        while q<=qry:
            qtyp=a[i]
            
            if qtyp=='SET':
                lru.set(int(a[i+1]),int(a[i+2]))
                i+=3
            elif qtyp=='GET':
                print(lru.get(int(a[i+1])),end=' ')
                i+=2
            q+=1
        print()
# } Driver Code Ends