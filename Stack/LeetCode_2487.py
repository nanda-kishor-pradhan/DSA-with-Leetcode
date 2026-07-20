# Ques No 2487 - Remove Nodes From Linked List 

# Problem Statement:
# You are given the head of a linked list.

# Remove every node which has a node with a greater value anywhere to the right side of it.

# Return the head of the modified linked list.

 

# Example 1:

# Input: head = [5,2,13,3,8]
# Output: [13,8]
# Explanation: The nodes that should be removed are 5, 2 and 3.
# - Node 13 is to the right of node 5.
# - Node 13 is to the right of node 2.
# - Node 8 is to the right of node 3.

# Example 2:

# Input: head = [1,1,1,1]
# Output: [1,1,1,1]
# Explanation: Every node has value 1, so no nodes are removed.



class Listnode:
    def __init__(self,val):
        self.val = val
        self.next = None
    
n1 = Listnode(5)
n2 = Listnode(2)
n3 = Listnode(13)
n4 = Listnode(2)
n5 = Listnode(8)

n1.next = n2 
n2.next = n3
n3.next = n4
n4.next = n5



class Solution:
    def removeNodes(self, head):
        stk = []
        curr = head
        while curr:
            while stk and stk[-1].val < curr.val:
                stk.pop()
            stk.append(curr)
            curr = curr.next

        for i in range(len(stk)-1):
            stk[i].next = stk[i+1]
        stk[-1].next = None

        return stk[0]
obj = Solution()
print(obj.removeNodes(n1))