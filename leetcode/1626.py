class Solution(object):
    def bestTeamScore(self, scores, ages):
        """
        :type scores: List[int]
        :type ages: List[int]
        :rtype: int
        """
        ll = len(scores)
        tp = [[scores[i],ages[i]] for i in xrange(ll)]
        dp = [0] * ll
        sp = sorted(tp, key=lambda p:(p[0],p[1]))
        ret = 0

        for i in xrange(ll):
            for j in xrange(i):
                if sp[i][1] >= sp[j][1]:
                    dp[i] = max(dp[i], dp[j])
            dp[i] += sp[i][0]
            ret = max(ret, dp[i])
        return ret
