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
    def isScramble(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
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

        #print bk1,bk2
        if bk1[l-1] != bk2[l-1]:
            return False

        def bkcmp(bk1,bk2,h1,e1,h2,e2):
            #print h1,e1,h2,e2
            if h1 == 0:
                t1 = {}
            else:
                t1 = bk1[h1-1]
            if h2 == 0:
                t2 = {}
            else:
                t2 = bk2[h2-1]

            if h1 == e1:
                if dist(t1, bk1[e1]) == dist(t2, bk2[e2]):
                    return True
                else:
                    return False

            for i in xrange(h1,e1):
                d = i - h1
                l1 = dist(t1, bk1[i])
                r1 = dist(bk1[i], bk1[e1])

                l2 = dist(t2, bk2[h2+d])
                r2 = dist(bk2[h2+d], bk2[e2])
                if l1 == l2:
                    if bkcmp(bk1, bk2, h1, i, h2, h2+d) and \
                        bkcmp(bk1, bk2, i+1, e1, h2+d+1, e2):
                        return True

                l2 = dist(t2, bk2[e2-d-1])
                r2 = dist(bk2[e2-d-1], bk2[e2])
                if l1 == r2:
                    if bkcmp(bk1, bk2, h1, i, e2-d, e2) and \
                        bkcmp(bk1, bk2, i+1, e1, h2, e2-d-1):
                        return True

            return False

        return bkcmp(bk1, bk2, 0, l-1, 0, l-1)
