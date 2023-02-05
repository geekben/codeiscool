class Solution(object):
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        l = len(s)
        if l == 0:
            return 1
        if l == 1:
            n = int(s)
            if n > 0 and n < 10:
                return 1
            else:
                return 0
        else:
            n = int(s[-1])
            a = b = 0
            if n > 0 and n < 10:
                a = self.numDecodings(s[:-1])
            if s[-2] != '0':
                n = int(s[-2:])
                if n > 9 and n < 27:
                    b = self.numDecodings(s[:-2])
            return a + b
