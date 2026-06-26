# Ques No 148 - Sort List

# Problem Statement:
# Given the head of a linked list, return the list after sorting it in ascending order.

 

# Example 1:

# Input: head = [4,2,1,3]
# Output: [1,2,3,4]




class Listnode:
    def __init__(self,val):
        self.val = val
        self.next = None
    
n1 = Listnode(12)
n2 = Listnode(2)
n3 = Listnode(0)
n4 = Listnode(9)
n5 = Listnode(7)

n1.next = n2 
n2.next = n3
n3.next = n4
n4.next = n5

class Solution:
    def sortList(self, head):
        if not head or not head.next:
            return head
        slow = head
        fast = head.next
        while fast and fast.next:
            slow=slow.next
            fast = fast.next.next
        second = slow.next
        slow.next = None

        left = self.sortList(head)
        right = self.sortList(second)

        dummy = Listnode(0)
        curr = dummy

        while left and right:
            if left.val <= right.val:
                curr.next = left
                left = left.next
            else:
                curr.next = right
                right = right.next
            curr = curr.next
        curr.next = left if left else right
        return dummy.next
obj = Solution()
print(obj.SortList(n1))


#This part is only for demonstrate
curr = n1
while curr:
    print(curr.val , end = "->")
    curr = curr.next