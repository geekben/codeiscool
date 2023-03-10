'''
F[i] = sum(nums[:i+1]
theorem1:
if F[j] mod p == F[i] mod p (j < i);then
    (F[i] - F[j]) mod p == 0
fi

theorem2:
if F[i] mod p == x;then
    (F[i] - x) mod p == 0
fi

we should find a subarray (j,i] which meets:
(F[i] - F[j]) mod p == x (x = (sum(nums) mod p))
so that the sum of remaining array mod p equals 0

according to theorem2:
    (F[i] - F[j]) mod p == x
=>  (F[i] - F[j] - x) mod p == 0

according to theorem1:
    (F[i] - F[j] - x) mod p == 0
we need found (i,j) that meets:
    (F[i] - x) mod p == F[j] mod p
'''
class Solution(object):
    def minSubarray(self, nums, p):
        """
        :type nums: List[int]
        :type p: int
        :rtype: int
        """
        ln = len(nums)
        st = {0: -1}
        s = 0
        ret = ln

        d = sum(nums) % p
        if d == 0:
            return 0
        for i,n in enumerate(nums):
            s += n
            sd = s % p
            td = (s - d) % p
            if td in st:
                ret = min(ret, i - st[td])
            st[sd] = i
        return ret if ret < ln else -1
