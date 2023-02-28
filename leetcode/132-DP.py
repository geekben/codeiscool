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
    def minCut(self, s):
        """
        :type s: str
        :rtype: int
        """
        ls = len(s)
        d = [[False for _ in xrange(ls)] for _ in xrange(ls)]

        for j in xrange(ls):
            for i in xrange(j+1):
                if i == j:
                    d[i][j] = True
                elif j - i == 1 and s[i] == s[j]:
                    d[i][j] = True
                elif s[i] == s[j] and d[i+1][j-1]:
                    d[i][j] = True

        ret = [2001 for _ in xrange(ls)]
        for i in xrange(ls):
            if d[0][i]:
                ret[i] = 0
            else:
                for j in xrange(i):
                    if d[j+1][i]:
                        ret[i] = min(ret[i], ret[j]+1)
        #print ret
        return ret[ls-1] # the string end at ls-1 index
