class Solution(object):
    def partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """
        ret = [[]]

        for c in s:
            t = []
            for r in ret:
                lr = len(r)
                t.append(r+[c])
                if lr > 0 and r[-1] == c:
                    t.append(r[:-1]+[c+c])
                if lr > 1 and r[-2] == c:
                    t.append(r[:-2]+[c+r[-1]+c])
            ret = t
        return ret
