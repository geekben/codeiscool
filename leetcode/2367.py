class Solution(object):
    def arithmeticTriplets(self, nums, diff):
        """
        :type nums: List[int]
        :type diff: int
        :rtype: int
        """
        st = {}
        ret = 0

        for n in nums:
            d = n % diff
            if d in st:
                tl = st[d]
                if len(tl) == 2:
                    if n - tl[1] == diff:
                        ret += 1
                        st[d] = [tl[1],n]
                    else:
                        st[d] = [n]
                else:
                    if n - tl[0] == diff:
                        st[d].append(n)
                    else:
                        st[d] = [n]
            else:
                st[d] = [n]
        return ret
