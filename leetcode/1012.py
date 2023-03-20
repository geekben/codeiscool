class Solution(object):
    def numDupDigitsAtMostN(self, n):
        """
        :type n: int
        :rtype: int
        """
        A = map(int, str(n))
        N = len(A)

        def f(i, tight, mask, hasDup):
            if i >= N:
                if hasDup:
                    return 1
                return 0
            upperLimit = A[i] if tight else 9
            ans = 0
            for d in range(upperLimit + 1):
                tight2 = tight and d == upperLimit
                if not hasDup:
                    mask2 = mask if mask == 0 and d == 0 else mask | (1 << d)
                    hasDup2 = mask & (1 << d)
                else:
                    mask2 = 0
                    hasDup2 = True
                ans += f(i + 1, tight2, mask2, hasDup2)
            return ans
        return f(0, True, 0, False)
