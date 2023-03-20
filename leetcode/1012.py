class Solution(object):
    def perm(self, n, k):
            ret = 1
            for i in range(k):
                    ret *= n - i
            return ret

    def numDupDigitsAtMostN(self, n):
        """
        :type n: int
        :rtype: int
        """
        limit = map(int, str(n+1))
        ln = len(limit)
        mask = 0
        # for 1234 , numbers < 1000 can safely calc the non-dup as follow
        count = sum(9*self.perm(9,i) for i in xrange(ln-1))
        s = set()

        for i in xrange(ln):
            start = 1 if i == 0 else 0
            for j in xrange(start, limit[i]):
                if j not in s:
                    count += self.perm(9-i, ln-i-1)
            if limit[i] in s:
                break
            s.add(limit[i])
        return n - count

