# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

        if head == None:
            return head
        if head.next == None:
            return None

        dummy = ListNode(0)
        prev = dummy
        prev.next = head

        cur = head
        nxt = head
        for i in range(1,n):
            nxt = nxt.next

        while(nxt.next != None):

            prev = prev.next
            cur = cur.next
            nxt = nxt.next

        if n == 1:
            prev.next = None
        else:
            prev.next = cur.next
            #cur.next = None

        return dummy.next
