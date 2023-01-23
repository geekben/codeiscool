class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        em = []
        last = nums[0]
        c = 1
        le = 0

        for i,n in enumerate(nums):
            if i == 0:
                continue
            if n == last:
                c += 1
                if c > 2:
                    em.append(i)
                    le += 1
                elif le > 0:
                    ei = em[0]
                    nums[ei] = n
                    em = em[1:] # could use pointer to avoid copy
                    em.append(i)
            else:
                c = 1
                last = n
                if le > 0:
                    ei = em[0]
                    nums[ei] = n
                    em = em[1:] # could use pointer to avoid copy
                    em.append(i)

        return len(nums) - le
