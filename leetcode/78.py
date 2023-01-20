class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        ret = []
        ret.append([])

        for i in nums:
            tr = ret[:]
            for r in ret:
                tr.append(r + [i])
            ret = tr

        return ret
