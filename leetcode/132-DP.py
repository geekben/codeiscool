'''
"aab"
"abbbbaa"
"ab"
"a"
"aaaaaaaba"
"aaaaa"
"ababababababababababababababababababa"
"ababababababababababababababababababab"
"abbbbaabcdefghijklmnopqrstuvwxyzzzzzzyyyyxxxxxabcd"
'''
class Solution(object):
    st = {}
    def isPalindrome(self, s):
        if s in self.st:
            return self.st[s]
        ls = len(s)
        if s[0] == s[-1]:
            if ls <= 2:
                self.st[s] = True
                return True
            elif self.isPalindrome(s[1:-1]):
                self.st[s] = True
                return True
            else:
                self.st[s] = False
                return False
        else:
            self.st[s] = False
            return False

    def minCut(self, s):
        """
        :type s: str
        :rtype: int
        """
        if self.isPalindrome(s):
            return 0
        ls = len(s)
        ret = 2001
        for i in xrange(ls):
            if self.isPalindrome(s[i:]):
                ret = min(ret, self.minCut(s[:i]))
        return ret + 1
