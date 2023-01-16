# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        node =None
        while(head is not None):
            next =head.next # we have created this empty node
            head.next = node# we want to break the connection with the 1st node
            node = head
            head = next
        return node # since it will point to last node
        