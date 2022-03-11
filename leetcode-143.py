class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        n = 0
        head2 = head
        a = []
        while (head != None):
            n += 1
            a.append(head)
            head = head.next

        i = 0
        #print('n = ', n)

        while i <= (n-1)//2 :
            #print(i)
            if i != 0:
                head2.next = a[i]
                head2 = head2.next

            temp = a.pop()
            head2.next = temp
            head2 = head2.next
            if i == (n-1)//2:
                head2.next = None
            i += 1