# Ques No 82 - Remove Duplicates from Sorted List-ii 

# Problem Statement:
# Given the head of a sorted linked list, delete all nodes that have duplicate numbers, leaving only distinct numbers from the original list. 
# Return the linked list sorted as well.

 

# Example 1:

# Input: head = [1,2,3,3,4,4,5]
# Output: [1,2,5]

# Example 2:

# Input: head = [1,1,1,2,3]
# Output: [2,3]






class Listnode:
    def __init__(self,val):
        self.val = val
        self.next = None
    
n1 = Listnode(1)
n2 = Listnode(1)
n3 = Listnode(1)
n4 = Listnode(2)
n5 = Listnode(3)

n1.next = n2 
n2.next = n3
n3.next = n4
n4.next = n5
#Leetcode part starts from here...
class Solution:
    def Palindrome(self,head):
        if not head:
            return None
        dummy = Listnode(0)
        dummy.next = head
        slow = dummy
        fast = head

        while fast:
            if fast.next and fast.val == fast.next.val:
                while fast.next and fast.val == fast.next.val:
                    fast = fast.next
                slow.next = fast.next
            else:
                slow = fast
            fast = fast.next
        return dummy.next
obj = Solution()
print(obj.Palindrome(n1))