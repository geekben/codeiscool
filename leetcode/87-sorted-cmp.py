class Solution(object):
    ss = {}
    def isScramble(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        ss = self.ss
        sk = s1+s2

        if sk in ss:
            return ss[sk]

        if s1 == s2:
            ss[sk] = True
            return True

        if sorted(s1) != sorted(s2):
            ss[sk] = False
            return False

        l = len(s1)
        m = l/2
        for i in xrange(1,l):
            if i >= m and \
                self.isScramble(s1[:i],s2[:i]) and self.isScramble(s1[i:],s2[i:]) \
                or i < m and \
                self.isScramble(s1[i:],s2[i:]) and self.isScramble(s1[:i],s2[:i]):
                ss[sk] = True
                return True

            if i >= m and \
                self.isScramble(s1[:i],s2[-i:]) and self.isScramble(s1[i:],s2[:-i]) \
                or i < m and \
                self.isScramble(s1[i:],s2[:-i]) and self.isScramble(s1[:i],s2[-i:]):
                ss[sk] = True
                return True

        ss[sk] = False
        return False
