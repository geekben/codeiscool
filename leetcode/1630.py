class Solution(object):
    def checkArithmeticSubarrays(self, nums, l, r):
        """
        :type nums: List[int]
        :type l: List[int]
        :type r: List[int]
        :rtype: List[bool]
        """
        st = {}
        # sn = sorted(nums)
        m = len(l)
        ret = []

        for i in xrange(m):
            ln = l[i]
            rn = r[i]
            if ln == rn or ln + 1 == rn:
                ret.append(True)
                continue
            sn = sorted(nums[ln:rn+1])
            d = sn[1] - sn[0]
            # print m,ln,rn
            for j in xrange(2, rn-ln+1):
                if sn[j] - sn[j-1] != d:
                    ret.append(False)
                    j -= 1
                    break
            if j == rn - ln:
                ret.append(True)
        return ret
