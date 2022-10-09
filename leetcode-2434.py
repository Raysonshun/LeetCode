class Solution:

    def robotWithString(self, s: str) -> str:

        dic, t, ans = Counter(s), [], []

        for char in s:

            t.append(char)

            if dic[char] == 1:
                del dic[char]
            else:
                dic[char] -= 1
            while dic and t and min(dic) >= t[-1]:
                ans += t.pop()

        ans += t[::-1]
        return ''.join(ans)


    #source: https://leetcode.com/problems/using-a-robot-to-print-the-lexicographically-smallest-string/discuss/2678792/Python3-Stack-%2B-Hashmap-O(26-*-N)-Clean-and-Concise
