class Solution(object):
    def minSubarray(self, nums, p):
        """
        :type nums: List[int]
        :type p: int
        :rtype: int
        """
        ln = len(nums)
        st = {}
        s = 0
        for n in nums:
            s += n
        d = s % p
        if d == 0:
            return 0

        lp = min(p, ln)
        for i in xrange(1, lp):
            last = 0
            for k in xrange(i):
                last += nums[k]
            if last % p == d: return i
            for j in xrange(i, ln):
                if i == 1:
                    last = nums[j]
                elif i == 2:
                    last = nums[j-1] + nums[j]
                else:
                    last = last - nums[j-i] + nums[j]
                if last % p == d:
                    return i

        return -1
