class Solution(object):
    st = {}
    def isPalindrome(self, s,i,j):
        if (i,j) in self.st:
            return self.st[(i,j)]
        if s[i] == s[j]:
            if j - i <= 1:
                self.st[(i,j)] = True
                return True
            elif self.isPalindrome(s,i+1,j-1):
                self.st[(i,j)] = True
                return True
            else:
                self.st[(i,j)] = False
                return False
        else:
            self.st[(i,j)] = False
            return False

    def minCut(self, s):
        """
        :type s: str
        :rtype: int
        """
        self.st = {}
        ls = len(s)
        q = [[0,(0,ls-1)]]

        while q:
            tl = q.pop(0)
            cut = tl[0]

            for idx,t in enumerate(tl[1:]):
                b,e = t
                if self.isPalindrome(s,b,e):
                    continue
                cut += 1
                for i in xrange(b,e):
                    q.append([cut, (b,i), (i+1,e)] + tl[idx+2:])
                break
            if cut == tl[0]:
                return cut

