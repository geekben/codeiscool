class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: bool
        """
        def target_between(t,l,r):
            if t >= l and t <= r:
                return True
            else:
                return False

        l = 1
        ln = len(nums)
        r = ln - 1

        if r == 0:
            if nums[0] == target:
                return True
            else:
                return False

        p = 0
        while l <= r:
            p = (l+r)/2
            if nums[p-1] >= nums[0]:
                if nums[p] <= nums[ln-1]:
                    if target_between(target, nums[p], nums[ln-1]):
                        l = p
                        r = ln-1
                    elif target_between(target, nums[0], nums[p-1]):
                        l = 0
                        r = p-1
                    else:
                        return False
                    break
                else:
                    if target_between(target, nums[0], nums[p-1]):
                        l = 0
                        r = p-1
                        break
                    l = p
            else:
                if target_between(target, nums[p], nums[ln-1]):
                    l = p
                    r = ln-1
                    break
                r = p - 1

        while l <= r:
            p = (l+r)/2
            if nums[p] == target:
                return True
            elif nums[p] > target:
                r = p - 1
            else:
                l = p + 1
        return False

