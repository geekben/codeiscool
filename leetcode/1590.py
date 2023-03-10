class Solution(object):
    def minSubarray(self, nums, p):
        """
        :type nums: List[int]
        :type p: int
        :rtype: int
        """
        ln = len(nums)
        st = {0: -1}
        s = 0
        ret = ln

        d = sum(nums) % p
        if d == 0:
            return 0
        for i,n in enumerate(nums):
            s += n
            sd = s % p
            td = (s - d) % p
            if td in st:
                ret = min(ret, i - st[td])
            st[sd] = i
        return ret if ret < ln else -1
