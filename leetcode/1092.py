class Solution(object):
    def shortestCommonSupersequence(self, str1, str2):
        """
        :type str1: str
        :type str2: str
        :rtype: str
        """
        l1 = len(str1)
        l2 = len(str2)
        ll = l1 + l2
        ret = ""
        lm = ll+1
        for i in xrange(1<<ll):
            tr = ""
            t1 = str1[:]
            t2 = str2[:]
            lt1 = l1
            lt2 = l2
            for j in xrange(ll):
                if lt1 == 0:
                    tr += t2
                    lt2 = 0
                elif lt2 == 0:
                    tr += t1
                    lt1 = 0
                else:
                    if t1[0] == t2[0]:
                        tr += t1[0]
                        t1 = t1[1:]
                        t2 = t2[1:]
                        lt1 -= 1
                        lt2 -= 1
                    elif (1 << j) & i == 0:
                        tr += t1[0]
                        t1 = t1[1:]
                        lt1 -= 1
                    else:
                        tr += t2[0]
                        t2 = t2[1:]
                        lt2 -= 1
                if lt1 == 0 and lt2 == 0:
                    break
            if len(tr) < lm:
                lm = len(tr)
                ret = tr
        return ret
