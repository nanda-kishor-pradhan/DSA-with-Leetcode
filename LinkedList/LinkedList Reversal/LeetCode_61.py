# Ques No 61 - Rotate List 

# Problem Statement:
# Given the head of a linked list, rotate the list to the right by k places.

 

# Example 1:

# Input: head = [1,2,3,4,5], k = 2
# Output: [4,5,1,2,3]

# Example 2:

# Input: head = [0,1,2], k = 4
# Output: [2,0,1]


class Listnode:
    def __init__(self,val):
        self.val = val
        self.next = None
    
n1 = Listnode(1)
n2 = Listnode(2)
n3 = Listnode(3)
n4 = Listnode(4)
n5 = Listnode(5)

n1.next = n2 
n2.next = n3
n3.next = n4
n4.next = n5

class Solution:
    def rotateRight(self,head,k):
        if not head or not head.next or k == 0:
            return head 
        tail = head
        length = 1
        while tail.next:
            tail = tail.next
            length += 1
        
        k = k % length
        if k == 0:
            return head
        
        curr = head
        for _ in range(length - k - 1):
            curr = curr.next
        new_head = curr.next
        curr.next = None
        tail.next = head
        
        return new_head
obj = Solution()
print(obj.rotateRight(n1,2))