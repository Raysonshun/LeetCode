class Solution(object):
    def lengthLongestPath(self, input):
        """
        :type input: str
        :rtype: int
        """
        stack, out = [], 0

        inputs = input.split('\n')

        for seq in inputs:

            seqs = seq.split('\t')

            if len(seqs) > len(stack):
                stack.append(seqs[-1])

            else:
                stack[len(seqs)-1] = seqs[-1]

            if seqs[-1].find('.') > -1:
                out = max(out, len('\\'.join(stack[:len(seqs)])))

        return out