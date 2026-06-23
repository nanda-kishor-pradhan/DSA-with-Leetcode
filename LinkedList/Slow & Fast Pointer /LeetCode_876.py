# QUES NO 876 - Middle of Linked list

# Problem Statement:
# Given the head of a singly linked list, return the middle node of the linked list.

# If there are two middle nodes, return the second middle node.

 

# Example 1:

# Input: head = [1,2,3,4,5]
# Output: [3,4,5]
# Explanation: The middle node of the list is node 3.


class ListNode:
    def __init__(self,val):
        self.val = val
        self.next = None


node1 = ListNode(1)
node2 = ListNode(2)
node3 = ListNode(3)
node4 = ListNode(4)
node5 = ListNode(5)

node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5


#This is code part for Leetcode

class Solution:
    def middleNode(self,head):
        slow , fast = head , head 
        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next
        return slow
obj = Solution()
print(obj.middleNode(node1))
