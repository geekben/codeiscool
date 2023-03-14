class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: List[str]
        """
        if s in wordDict:
            return [s]
        ls = len(s)
        dp = [False] * (ls+1)
        dp[0] = True
        pattern = 0

        for i in xrange(0,ls):
            for j in xrange(0,i+1):
                if dp[j] and s[j:i+1] in wordDict:
                    dp[i+1] = True
                    pattern |= (1 << i)
        #print dp, pattern

        st = 1 << (ls-1)
        ret = []
        for k in xrange(1, st+1):
            if (k | pattern) == pattern:
                tr = ""
                j = 0
                for i in xrange(0,ls):
                    if (1 << i) & k != 0:
                        if s[j:i+1] not in wordDict:
                            tr = ""
                            break
                        else:
                            tr += s[j:i+1] + " "
                            j = i + 1
                if tr != "" and s[j:] in wordDict:
                    ret.append(tr+s[j:])
        return ret
