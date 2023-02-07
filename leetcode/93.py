class Solution(object):
    # d = {}
    def valid(self, s):
        l = len(s)
        if l == 1:
            return True
        elif l == 2 and s[0] > '0':
            return True
        elif l == 3 and s[0] > '0':
            a = int(s)
            if a > 0 and a <= 255:
                return True
            else:
                return False
        else:
            return False

    def restoreIpAddresses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        l = len(s)
        if l > 12 or l < 4:
            return []
        r = []
        for i in xrange(1,4):
            if self.valid(s[:i]):
                for j in xrange(i+1,i+4):
                    if self.valid(s[i:j]):
                        for k in xrange(j+1,j+4):
                            if self.valid(s[j:k]) and self.valid(s[k:]):
                                r.append(s[:i]+'.'+s[i:j]+'.'+s[j:k]+'.'+s[k:])
        return r
