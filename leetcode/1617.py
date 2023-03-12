class Solution(object):
    def countSubgraphsForEachDiameter(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: List[int]
        """

        dist = [[n+1]*n for _ in xrange(n)]
        for i in xrange(n):
            dist[i][i] = 0
        dp = [0]*(1<<n)

        for x,y in edges:
            dp[(1<<(x-1)) + (1<<(y-1))] = 1
            dist[x-1][y-1] = 1
            dist[y-1][x-1] = 1

        for k in xrange(n):
            for i in xrange(n):
                for j in xrange(n):
                    temp = dist[i][k] + dist[k][j]
                    if temp < dist[i][j]:
                        dist[i][j] = temp

        for i in xrange(1<<n):
            if dp[i] == 0:
                continue
            for j in xrange(n):
                bj = 1 << j
                if i & bj != 0 or dp[i | bj] != 0:
                    continue

                for k in xrange(n):
                    bk = 1 << k
                    if i & bk != 0 and dist[k][j] == 1:
                        dp[i|bj] = dp[i]
                        break
                if dp[i|bj] == 0:
                    continue
                for k in xrange(n):
                    bk = 1 << k
                    if i & bk != 0:
                        dp[i|bj] = max(dp[i|bj], dist[k][j])

        ret = [0]*(n-1)
        for i in range(1<<n):
            if dp[i] != 0:
                ret[dp[i]-1] += 1

        return ret
