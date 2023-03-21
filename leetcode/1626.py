class Solution(object):
    def bestTeamScore(self, scores, ages):
        """
        :type scores: List[int]
        :type ages: List[int]
        :rtype: int
        """
        ll = len(scores)
        #conf = [[True] * ll for _ in xrange(ll)]
        conf = []

        for i in xrange(ll):
            for j in xrange(i+1, ll):
                if (scores[i] > scores[j] and ages[i] < ages[j]) or \
                    (scores[i] < scores[j] and ages[i] > ages[j]):
                    #conf[i][j] = False
                    conf.append((1 << i) | (1 << j))
        # print conf

        m = 0
        for i in xrange(1,1<<ll):
            if i in conf:
                continue
            isConf = False
            for c in conf:
                if (i & c) == c:
                    isConf = True
                    break
            if not isConf:
                s = 0
                for j in xrange(ll):
                    if ((1 << j) & i) > 0:
                        s += scores[j]
                m = max(m, s)
        return m
