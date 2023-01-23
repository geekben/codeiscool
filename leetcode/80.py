class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        em = [0 for _ in xrange(len(nums))]
        last = nums[0]
        c = 1
        le = 0
        he = 0 # head of em
        ee = 0 # end of em

        for i,n in enumerate(nums):
            if i == 0:
                continue
            if n == last:
                c += 1
                if c > 2:
                    em[ee] = i
                    ee += 1
                    le += 1
                elif le > 0:
                    ei = em[he]
                    nums[ei] = n
                    he += 1
                    em[ee] = i
                    ee += 1
            else:
                c = 1
                last = n
                if le > 0:
                    ei = em[he]
                    nums[ei] = n
                    he += 1
                    em[ee] = i
                    ee += 1

        return len(nums) - le
