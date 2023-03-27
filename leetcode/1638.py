class Solution(object):
    def countSubstrings(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: int
        """
        ls = len(s)
        lt = len(t)
        eq = [[] for _ in xrange(ls)]
        oq = [[] for _ in xrange(ls)]
        ret = 0

        for i,c in enumerate(s):
            for j,d in enumerate(t):
                if c != d:
                    oq[i].append(j)
                else:
                    eq[i].append(j)
            if i == 0:
                ret += len(oq[0])
                continue
            #print eq,oq
            for k in xrange(i):
                te = []
                to = []
                for ei in eq[k]:
                    if ei+1 >= lt:
                        break
                    if c == t[ei+1]:
                        te.append(ei+1)
                    else:
                        to.append(ei+1)
                for oi in oq[k]:
                    if oi+1 >= lt:
                        continue
                    if c == t[oi+1]:
                        to.append(oi+1)
                eq[k] = te
                oq[k] = to
            # print eq,oq
            for o in oq:
                ret += len(o)

        return ret
