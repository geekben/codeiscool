class Solution(object):
    def maximalNetworkRank(self, n, roads):
        """
        :type n: int
        :type roads: List[List[int]]
        :rtype: int
        """
        link = [[False]*n for _ in xrange(n)]
        city = []
        m = 0

        for x,y in roads:
            link[x][y] = True
            link[y][x] = True
        for i in xrange(n):
            #city.append((i,sum(link[i])))
            city.append(sum(link[i]))
        #city_s = sorted(city, key=lambda c:c[1])
        for i in xrange(n-1):
            for j in xrange(i+1,n):
                s = city[i] + city[j]
                if link[i][j]:
                    s -= 1
                m = max(m, s)

        return m
