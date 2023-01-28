class Solution(object):
    def maximalRectangle(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        row = len(matrix)
        col = len(matrix[0])

        sm = [[0 for _ in xrange(col+2)] for _ in xrange(row+1)]
        
        y = 1
        for r in matrix:
            x = 1
            for c in r:
                if c == "1":
                    sm[y][x] = sm[y-1][x] + int(c)
                else:
                    sm[y][x] = 0
                x += 1
            y += 1

        st = [[0,0] for _ in xrange(col+1)]
        m = 0
        for r in sm[1:]:
            e = 0
            for p,c in enumerate(r):
                if c == st[e][0]:
                    pass
                elif c > st[e][0]:
                    e += 1
                    st[e] = [c, p]
                else:
                    while e >= 0 and st[e][0] > c:
                        a = st[e][0]*(p-st[e][1])
                        if a > m:
                            m = a
                        e -= 1
                    if st[e][0] < c:
                        e += 1
                        st[e] = [c, st[e][1]]
            for s in st[:e+1]:
                a = s[0]*(col+1-s[1])
                if a > m:
                    m = a

        return m
