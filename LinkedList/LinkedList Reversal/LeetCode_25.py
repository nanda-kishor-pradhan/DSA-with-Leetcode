# Ques No 25 - Reverse Nodes in K Group 

# Problem statement:
# Given the head of a linked list, reverse the nodes of the list k at a time, and return the modified list.

# k is a positive integer and is less than or equal to the length of the linked list. If the number of nodes is not a multiple of k then left-out nodes, in the end, should remain as it is.

# You may not alter the values in the list's nodes, only nodes themselves may be changed.

 

# Example 1:

# Input: head = [1,2,3,4,5], k = 2
# Output: [2,1,4,3,5]

# Example 2:

# Input: head = [1,2,3,4,5], k = 3
# Output: [3,2,1,4,5]



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
    def reverseKGroup(self ,head , k):
        if not head:
            return None
        curr = head
        count = 0
        while curr and count < k:
            curr =curr.next 
            count+=1
        if count < k:
            return head
        curr = head
        prev = None
        for _ in range(k):
            temp = curr.next 
            curr.next = prev
            prev = curr
            curr= temp
        head.next = self.reverseKGroup(curr,k)

        return prev
obj = Solution()
print(obj.reverseKGroup(n1,2))