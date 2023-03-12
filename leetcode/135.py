class Solution(object):
    def candy(self, ratings):
        """
        :type ratings: List[int]
        :rtype: int
        """
        h = 0
        l = 0
        ret = 0
        m = 0

        for i,r in enumerate(ratings):
            if i == 0:
                ret += 1
                l = 1
                m = l
                continue
            if r > ratings[i-1]:
                l += 1
                ret += l
                h = i
                m = l
            elif r == ratings[i-1]:
                l = 1
                ret += l
                h = i
                m = l
            else:
                l = 1
                if m > i - h:
                    ret += i - h - 1
                else:
                    ret += i - h
                ret += l

        return ret
