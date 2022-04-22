class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:



        seen = {}

        start, res = 0, 0

        for i, c in enumerate(s):

            if c in seen and seen[c] >= start:

                start = seen[c]+1

            else:
                res = max(res, i-start+1)

            seen[c] = i

        return res


        '''
        p1, p2 = 0,0

        n = len(s)

        cur = []

        maxl = 0

        while (p2 <= n-1):

            if s[p2] not in cur:

                cur.append(s[p2])

                maxl = max(maxl, len(cur))

                p2 += 1

            else:

                cur.append(s[p2])

                cur = cur[cur.index(s[p2])+1:]

                maxl = max(maxl, len(cur))

                p2 += 1

            print(cur)

        return maxl
        '''