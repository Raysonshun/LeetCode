class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:

        n = 0

        head2 = head

        while (head != None):
            n += 1
            head = head.next

        if n == 1:
            return True

        stack = []

        for i in range(0, n//2):
            stack.append(head2.val)
            head2 = head2. next
            #print(head2.val)

        if n%2 == 0:
            start = int(n/2)
            #head2 = head2.next

        else:
            start = int(n//2 + 1)
            head2 = head2.next

        for i in range(start, n):
            if head2.val != stack.pop():
                return False
            head2 = head2.next

        return True