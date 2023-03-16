class Solution(object):
    def answerQueries(self, nums, queries):
        """
        :type nums: List[int]
        :type queries: List[int]
        :rtype: List[int]
        """
        ln = len(nums)
        sn = sorted(nums)
        sums = [0] * (ln + 2)
        ans = []

        for i in xrange(ln):
            sums[i+1] = sn[i] + sums[i]
        sums[-1] = sums[-2] + 1000001
        #print sums
        for q in queries:
            for i in xrange(ln+2):
                if q < sums[i]:
                    ans.append(i-1)
                    break

        return ans
