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

        l = 0
        ln = len(nums)
        r = ln - 1

        if r == 0:
            if nums[0] == target:
                return True
            else:
                return False

        p = 0
        while l <= r:
            # bsearch must take care of pivot position
            s = l + r
            if s%2 == 1:
                p = s/2 + 1
            else:
                p = s/2

            if nums[p] == target or nums[p-1] == target:
                return True

            # absorbs the same values around pivot
            # this is important because it can't tell
            # which direction to take next if the candidate
            # pivot in this try is among the same values
            # and absorbtion could destroy the array rotation
            # assumption so we must judge before going further
            if nums[l] < nums[r]:
                break
            if nums[p-1] == nums[p] and \
                nums[l] == nums[r] and \
                nums[l] == nums[p]:
                l += 1
                r -= 1
                continue

            if nums[p-1] >= nums[l]:
                if nums[p] <= nums[r]:
                    if target_between(target, nums[p], nums[r]):
                        l = p + 1 # if l = p, could be a deadloop
                    elif target_between(target, nums[l], nums[p-1]):
                        r = p - 1
                    else:
                        return False
                    break
                else:
                    if target_between(target, nums[l], nums[p-1]):
                        r = p - 1
                        break
                    l = p + 1
            else:
                if target_between(target, nums[p], nums[r]):
                    l = p + 1
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
