class Solution(object):
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        sn = sorted(nums)

        ret = [[]]
        last = -11
        llen = 0
        for n in sn:
            l = len(ret)
            if n != last:
                for i in xrange(l):
                    ret.append(ret[i][:]+[n])
                last = n
                llen = l
            else:
                for i in xrange(llen):
                    ret.append(ret[l-llen+i][:]+[n])
        return ret
