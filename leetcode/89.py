class Solution(object):
    # TODO: use global var to share results among cases
    def grayCode(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        ret = [0] # TODO: pre allocate for time

        for i in xrange(n):
            # l = 1 << i # slower than len()
            l = len(ret)
            for j in xrange(l-1,-1,-1):
                ret.append(ret[j] + (1<<i))

        return ret
