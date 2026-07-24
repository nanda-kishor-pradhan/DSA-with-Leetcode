# Ques No - Reverse Linked list

# Problem Statement:
# Given the head of a singly linked list, reverse the list, and return the reversed list.

# Example 1:

# Input: head = [1,2,3,4,5]
# Output: [5,4,3,2,1]


# ____________________________________
#This part is only for VS code

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
#Leetcode part starts from here....
class Solution:
    def ReverseList(self,head):
        helper = None
        mech = head

        while mech:
            temp = mech.next
            mech.next = helper 
            helper = mech
            mech = temp
        return helper
obj = Solution()
print(obj.ReverseList(n1))
       