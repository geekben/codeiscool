class Solution(object):
    def isScramble(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        import copy

        def dist(d1, d2):
            d = copy.deepcopy(d2)
            for k in d.keys():
                if k in d1.keys():
                    d[k] -= d1[k]
                    if d[k] == 0:
                        del d[k]
            return d

        l = len(s1)
        if l == 1:
            if s1 == s2:
                return True
            else:
                return False

        #bk1 = [[0 for _ in xrange(26)] for _ in xrange(len(s1))]
        bk1 = [{} for _ in xrange(l)]
        for i in xrange(l):
            if i > 0:
                bk1[i] = copy.deepcopy(bk1[i-1])

            c = s1[i]
            if c not in bk1[i].keys():
                bk1[i][c] = 1
            else:
                bk1[i][c] += 1

        bk2 = [{} for _ in xrange(l)]
        for i in xrange(l):
            if i > 0:
                bk2[i] = copy.deepcopy(bk2[i-1])

            c = s2[i]
            if c not in bk2[i].keys():
                bk2[i][c] = 1
            else:
                bk2[i][c] += 1

        if bk1[l-1] != bk2[l-1]:
            return False

        for i in xrange((l-1)/2+1):
            l1 = bk1[i]
            r1 = dist(l1, bk1[l-1])
            l2 = bk2[i]
            r2 = dist(l2, bk2[l-1])

            if l1 == l2 and r1 == r2:
                return self.isScramble(s1[:i+1],s2[:i+1]) and \
                    self.isScramble(s1[i+1:],s2[i+1:])
            if l1 != l2:
                #l2 = bk2[(l-1)-(i+1)]
                l2 = bk2[-i-2]
                r2 = dist(l2, bk2[l-1])
                if l1 == r2 and r1 == l2:
                    return self.isScramble(s1[:i+1],s2[-i-1:]) and \
                        self.isScramble(s1[i+1:],s2[:-i-1])
        return False
