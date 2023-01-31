'''
"abcde"
"caebd"
"a"
"a"
"a"
"b"
"abcdeg"
"caebdg"
"abcdeg"
"gcaebd"
"aa"
"aa"
"ab"
"ba"
"abc"
"cba"
"aaaaabbbbb"
"aabbaabbaa"
"abcdegreat"
"tgreacaebd"
"abcdbdacbdac"
"bdacabcdbdac"
"abcdecaebd"
"caebdabcde"
"abcdbdac"
"bdacabcd"
"ccababcaabcb"
"bccbccaaabab"
"ccababcaabc"
"bccbccaaaba"
"ccababcaa"
"cbccaaaba"
"cababca"
"bccaaab"
"ccababcaabc"
"ccbccaaabab"
"caabc"
"bccaa"
"ccababcaabcbbccbccaaabab"
"bccbccaaababccababcaabcb"
"ccababcaabcbbccbccaaababgreat"
"bccbccaaababccababcaabcbrgeat"
"ccababcaabcbbccbccaaabababcdeg"
"caebdgbccbccaaababccababcaabcb"
"eebaacbcbcadaaedceaaacadccd"
"eadcaacabaddaceacbceaabeccd"
'''
class Solution(object):
    import copy
    bk1 = {}
    bk2 = {}
    st1 = []
    st2 = []
    s1 = ""
    s2 = ""
    ss = {}

    def dist(self, n, d1, d2):
        if n == 1:
            st = self.st1
            bk = self.bk1
        else:
            st = self.st2
            bk = self.bk2

        if st[d1][d2]:
            return st[d1][d2]

        d = copy.deepcopy(bk[d2])
        for k in d.keys():
            if k in bk[d1].keys():
                d[k] -= bk[d1][k]
                if d[k] == 0:
                    del d[k]
        st[d1][d2] = d
        return d

    def bkcmp(self, h1, e1, h2, e2):
        #print h1,e1,h2,e2
        ss = self.ss
        if (h1,e1,h2) in ss.keys():
            return ss[(h1,e1,h2)]

        if self.s1[h1:e1+1] == self.s2[h2:e2+1]:
            ss[(h1,e1,h2)] = True
            return True

        m = (h1 + e1)/2
        for i in xrange(h1,e1):
            d = i - h1
            l1 = self.dist(1, h1-1, i)
            r1 = self.dist(1, i, e1)

            l2 = self.dist(2, h2-1, h2+d)
            r2 = self.dist(2, h2+d, e2)
            if l1 == l2:
                if i <= m and self.bkcmp(h1, i, h2, h2+d) and \
                    self.bkcmp(i+1, e1, h2+d+1, e2):
                    ss[(h1,e1,h2)] = True
                    return True
                if i > m and self.bkcmp(i+1, e1, h2+d+1, e2) and \
                    self.bkcmp(h1, i, h2, h2+d):
                    ss[(h1,e1,h2)] = True
                    return True

            l2 = self.dist(2, h2-1, e2-d-1)
            r2 = self.dist(2, e2-d-1, e2)
            if l1 == r2:
                if i <= m and self.bkcmp(h1, i, e2-d, e2) and \
                    self.bkcmp(i+1, e1, h2, e2-d-1):
                    ss[(h1,e1,h2)] = True
                    return True
                if i > m and self.bkcmp(i+1, e1, h2, e2-d-1) and \
                    self.bkcmp(h1, i, e2-d, e2):
                    ss[(h1,e1,h2)] = True
                    return True

        ss[(h1,e1,h2)] = False
        return False

    def isScramble(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        l = len(s1)
        if l == 1:
            if s1 == s2:
                return True
            else:
                return False
        self.s1 = s1
        self.s2 = s2
        self.st1 = [[None for _ in xrange(l+1)] for _ in xrange(l)]
        self.st2 = [[None for _ in xrange(l+1)] for _ in xrange(l)]
        self.bk1 = [{} for _ in xrange(l+1)] # last item for -1
        self.bk2 = [{} for _ in xrange(l+1)]
        self.st1.append(self.bk1)
        self.st2.append(self.bk2)
        self.ss = {}

        for i in xrange(l):
            if i > 0:
                self.bk1[i] = copy.deepcopy(self.bk1[i-1])

            c = s1[i]
            if c not in self.bk1[i].keys():
                self.bk1[i][c] = 1
            else:
                self.bk1[i][c] += 1

        for i in xrange(l):
            if i > 0:
                self.bk2[i] = copy.deepcopy(self.bk2[i-1])

            c = s2[i]
            if c not in self.bk2[i].keys():
                self.bk2[i][c] = 1
            else:
                self.bk2[i][c] += 1

        if self.bk1[l-1] != self.bk2[l-1]:
            return False

        return self.bkcmp(0, l-1, 0, l-1)
