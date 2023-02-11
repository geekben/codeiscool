class Solution(object):
    def isInterleave(self, s1, s2, s3):
        """
        :type s1: str
        :type s2: str
        :type s3: str
        :rtype: bool
        """
        l1 = len(s1)
        l2 = len(s2)
        hs = s1
        ts = s2
        if l1 > l2:
            hs = s2
            ts = s1

        if l1 == 0 or l2 == 0:
            if ts == s3:
                return True
            else:
                return False
        h = hs[0]
        for i,c in enumerate(s3):
            if c == h and self.isInterleave(hs[1:], ts, s3[:i]+s3[i+1:])
                return True
        return False
