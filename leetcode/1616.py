class Solution(object):
    def checkPalindromeFormation(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: bool
        """
        lw = len(a)
        ap = True
        bp = True
        aq = True
        bq = True
        aqq = True
        bqq = True

        for i in xrange(lw/2):
            if ap and a[i] != b[lw-1-i]:
                ap = False
            if bp and b[i] != a[lw-1-i]:
                bp = False
            if (not ap) and aq:
                aq = (a[i] == a[lw-1-i])
            if (not ap) and aqq:
                aqq = (b[i] == b[lw-1-i])

            if (not bp) and bq:
                bq = (b[i] == b[lw-1-i])
            if (not bp) and bqq:
                bqq = (a[i] == a[lw-1-i])
            if ap or aq or bp or bq or aqq or bqq:
                continue
            return False
            
        return True
