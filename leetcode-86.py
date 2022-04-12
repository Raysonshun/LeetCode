class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:


        ll,hh= ListNode(0), ListNode(0)
        l = ll
        h = hh

        cur = head

        while(cur):

            store = cur.next

            if cur.val < x:
                ll.next = cur
                ll.next.next = None
                ll = ll.next

            else:

                hh.next = cur
                hh.next.next = None
                hh = hh.next

            cur = store

        ll.next = h.next

        return l.next





# initial solution:

#         if not head:
#             return

#         cur = head

#         l = []

#         while(cur):
#             l.append(cur.val)
#             cur = cur.next

#         i = 0
#         cur_small = 0
#         st = []

#         while(i < len(l)):

#             if l[i] < x:
#                 i += 1
#                 continue
#             else:
#                 st.append(l.pop(i))

#         l = l + st

#         res = [ListNode(i) for i in l]

#         ret = res[0]
#         ans = ret

#         for i in range(1,len(res)):
#             ret.next = res[i]
#             ret = ret.next

#         return ans