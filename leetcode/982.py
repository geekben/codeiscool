class Solution(object):
    def countTriplets(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ln = len(nums)
        ret = 0
        st = {}

        for i in xrange(ln):
            for j in xrange(i,ln):
                mask = nums[i] & nums[j]
                if mask in st:
                    if i == j: st[mask] += 1
                    else: st[mask] += 2
                else:
                    if i == j: st[mask] = 1
                    else: st[mask] = 2

        for n in nums:
            for m in st.keys():
                if n & m == 0:
                    ret += st[m]
        return ret
