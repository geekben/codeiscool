class Solution(object):
    def countSubarrays(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        ret = 0
        ln = len(nums)
        lm = min(ln-k, k) * 2 + 1
        for w in xrange(1, lm+1):
            for i in xrange(ln-w+1):
                if k in nums[i:i+w]:
                    left = right = 0
                    for j in xrange(i,i+w):
                        if nums[j] > k:
                            right += 1
                        elif nums[j] < k:
                            left += 1
                    if right == left or left + 1 == right:
                        ret += 1
        return ret
