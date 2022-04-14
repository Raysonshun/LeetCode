class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        if (not head) or (not head.next):
            return head

        fast, slow = head.next, head

        while ( fast and fast.next ):

            fast = fast.next.next
            slow = slow.next

        head2 = slow.next
        slow.next = None

        h1 = self.sortList(head)
        h2 = self.sortList(head2)

        return self.merge(h1,h2)




    def merge(self,h1,h2):

        dummy = d = ListNode(0)

        while h1 and h2:

            if h1.val <= h2.val:

                #temp = h1.next
                #h1.next = ListNode(None)
                dummy.next = h1
                dummy = dummy.next
                h1 = h1.next

            else:
                dummy.next = h2
                dummy = dummy.next
                h2 = h2.next

        re = h1 or h2

        dummy.next = re

        return d.next