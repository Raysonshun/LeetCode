class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:

        s = re.split(r'[\"!?\',;.\s]', paragraph)


        # p = ''
        # for i in paragraph:
        #     if not i.isalpha():
        #         p += ','
        #     else:
        #         p += i

        #s = p.split(',')

        d = {}

        for i in range(len(s)):
            s[i] = s[i].lower()

        for i in s:

            if i not in d:
                d[i] = 1
            else:
                d[i] += 1

        maxx = 0
        res = ''

        for i in d:

            if d[i] > maxx and i not in banned and i.isalpha():
                maxx = d[i]
                res = i

        return res
