class Solution(object):
    import copy
    ss = {}

    def bkcmp(self, h1, e1, h2, e2):
        #print h1,e1,h2,e2
        ss = self.ss
        s1 = self.s1
        s2 = self.s2
        if (h1,e1,h2) in ss.keys():
            return ss[(h1,e1,h2)]

        if s1[h1:e1+1] == s2[h2:e2+1]:
            ss[(h1,e1,h2)] = True
            return True

        if sorted(s1[h1:e1+1]) != sorted(s2[h2:e2+1]):
            ss[(h1,e1,h2)] = False
            return False

        m = (h1+e1)/2
        for i in xrange(h1,e1):
            j = i - h1 + h2
            if i <= m and self.bkcmp(h1,i,h2,j) and self.bkcmp(i+1,e1,j+1,e2):
                ss[(h1,e1,h2)] = True
                return True
            if i > m and self.bkcmp(i+1,e1,j+1,e2) and self.bkcmp(h1,i,h2,j):
                ss[(h1,e1,h2)] = True
                return True
            j = e2 - (i - h1)
            if i <= m and self.bkcmp(h1,i,j,e2) and self.bkcmp(i+1,e1,h2,j-1):
                ss[(h1,e1,h2)] = True
                return True
            if i > m and self.bkcmp(i+1,e1,h2,j-1) and self.bkcmp(h1,i,j,e2):
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
        self.s1 = s1
        self.s2 = s2
        self.ss = {}

        return self.bkcmp(0, l-1, 0, l-1)
