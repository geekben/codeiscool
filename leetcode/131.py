class Solution(object):
    def partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """
        ret = [[]]

        for c in s:
            t = []
            for r in ret[:]:
                r.append(c)
                lr = len(r)
                if lr > 1 and r[-2] == c:
                    ret.append(r[:-2]+[c+c])
                if lr > 2 and r[-3] == c:
                    ret.append(r[:-3]+[c+r[-2]+c])
        return ret
