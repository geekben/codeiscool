class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        if len(digits) == 0:
            return []
        
        s = {'2':'abc', '3':'def', '4':'ghi', '5':'jkl', '6':'mno', '7':'pqrs', '8':'tuv', '9':'wxyz'}
        ret = []
        for c in s[digits[0]]:
            ret.append(c)
        lr = len(ret)
        for d in digits[1:]:
            l = len(s[d])
            ret *= l
            lo = lr
            lr = lo * l
            for i in range(0,lr):
                ret[i] += s[d][i/lo]

        return ret

s = Solution()
print s.letterCombinations("234")
