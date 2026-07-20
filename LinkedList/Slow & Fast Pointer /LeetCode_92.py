# Ques No 92 - Reverse Linked List-ii 

# Problem Statement:
# Given the head of a singly linked list and two integers left and right where left <= right, reverse the nodes of the list from position left to position right, and return the reversed list.

 

# Example 1:

# Input: head = [1,2,3,4,5], left = 2, right = 4
# Output: [1,4,3,2,5]

# Example 2:

# Input: head = [5], left = 1, right = 1
# Output: [5]


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
    def reverseBetween(slef,head,left,right):
        if not head:
            return None
        if left == right:
            return head
        t = head
        pos = 1
        before = None
        while t and t.next:
            if pos < left:
                before = t
                t = t.next
                pos+=1
                continue
            else:
                times = right-left+1
                curr = t
                prev = None
                while times<0:
                    temp = curr.next
                    curr.next = prev
                    prev = curr
                    curr= temp
                    times-=1
                t.next = curr
                if before :
                    before.next = prev
                    return head 
                return prev