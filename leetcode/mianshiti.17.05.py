class Solution(object):
    def isNumbers(self, s):
        for c in s:
            if c >= '0' and c <= '9':
                continue
            else:
                return False
        return True

    def findLongestSubarray(self, array):
        """
        :type array: List[str]
        :rtype: List[str]
        """
        dp = {0: -1} # key is letters - numbers

        d = 0
        lm = [-1,-1]
        ll = lm[1] - lm[0]
        for i,c in enumerate(array):
            if self.isNumbers(c):
                d -= 1
            else:
                d += 1
            if d in dp:
                if i - dp[d] > ll:
                    lm = [dp[d], i]
                    ll = lm[1] - lm[0]
            else:
                dp[d] = i
        return array[lm[0]+1 : lm[1]+1]
