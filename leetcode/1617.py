class Solution(object):
    def countSubgraphsForEachDiameter(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: List[int]
        """

        subs = [[] for _ in xrange(n-1)]

        for i in xrange(1, n+1):
            for e in edges[:]:
                se = sorted(e)
                if se[0] != i:
                    continue
                edges.remove(e)
                for j in xrange(n-2,-1,-1):
                    for ne in subs[j]:
                        if se[0] == ne[0]:
                            subs[j+1].append(se[1] + ne[:])
                        elif se[0] == ne[-1]:
                            subs[j+1].append(ne[:] + se[1])
                        elif se[0] < ne[1] and se[0] > ne[0]:
                            subs[j].append([ne[0], ne[1]])
                subs[0].append(se)

        ret = []
        for sub in subs:
            ret.append(len(sub))
        return ret
