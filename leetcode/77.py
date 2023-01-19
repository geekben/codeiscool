class Solution(object):
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        ret = []
        ret.append(range(1, k+1))

        if n == k:
            return ret

        for i in range(k+1, n+1):
            for j in ret:
                tr = []
                for l in range(1, i):
                    if l in j:
                        t = j[:]
                        t.remove(l)
                        t.append(i)
                        tr.append(t)
                ret = ret + tr
        return ret
