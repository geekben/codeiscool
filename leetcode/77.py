class Solution(object):
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        ret = []

        if n == k:
            ret.append(range(1, k+1))
            return ret

        # count = n!/(n-k)!/k!
        for t in range(0, k):
            if t == 0:
                for i in range(1, n-k+2):
                    ret.append([i])
                continue
            tr = []
            for r in ret:
                if r[-1] == n:
                    continue
                for j in range(r[-1]+1, n+1):
                    tr.append(r+[j])
            ret = tr
        return ret
