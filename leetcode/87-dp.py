class Solution(object):
    def isScramble(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        l = len(s1)
        if l == 1:
            if s1 == s2:
                return True
            else:
                return False
        ss = [[[None for _ in xrange(l+1)] for _ in xrange(l)] for _ in xrange(l)]

        for i in xrange(l):
            for j in xrange(l):
                if s1[i] == s2[j]:
                    ss[i][j][1] = True
                else:
                    ss[i][j][1] = False

        # f for floor, f#1 for 1 char strings, f#2 for 2 char strings
        for f in xrange(2,l+1):
            for i in xrange(l-f+1):
                for j in xrange(l-f+1):
                    # postion k divide strings as [inclusive]:
                    # [i, i+k],[i+k+1, i+f-1]
                    # [j, j+k],[j+k+1, j+f-1] non-swap
                    # [j+f-k-1,j+f-1],[j, j+f-k-2] swap
                    for k in xrange(f-1):
                        if (ss[i][j][k+1] and ss[i+k+1][j+k+1][f-k-1]) \
                            or (ss[i][j+f-k-1][k+1] and ss[i+k+1][j][f-k-1]):
                            ss[i][j][f] = True
                            break
                    if ss[i][j][f] is None:
                        ss[i][j][f] = False
        return ss[0][0][l]
