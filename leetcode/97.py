class Solution(object):
    d = {}
    def isInterleave(self, s1, s2, s3):
        """
        :type s1: str
        :type s2: str
        :type s3: str
        :rtype: bool
        """
        d = self.d
        if (s1,s2,s3) in d:
            return d[(s1,s2,s3)]
        l1 = len(s1)
        l2 = len(s2)
        l3 = len(s3)
        if l1 + l2 != l3:
            d[(s1,s2,s3)] = False
            return False

        hs = s1
        ts = s2
        if l1 > l2:
            hs = s2
            ts = s1

        if l1 == 0 or l2 == 0:
            if ts == s3:
                d[(s1,s2,s3)] = True
                return True
            else:
                d[(s1,s2,s3)] = False
                return False
        h = hs[0]
        for i,c in enumerate(s3):
            if c == h and ts[:i] == s3[:i] and \
                self.isInterleave(hs[1:], ts[i:], s3[i+1:]):
                d[(s1,s2,s3)] = True
                return True
        d[(s1,s2,s3)] = False
        return False
