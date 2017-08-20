class ConsecutivePalindromes:
    def isPalindrome(self, s):
        l = len(s)
        if l <= 1:
            return False
        for i,c in enumerate(s):
            if i < l/2:
                if c == s[l-1-i]:
                    continue
                else:
                    return False
            else:
                break

        return True

    def findPalindromes(self, s):
        l = len(s)
        r = []
        for i,c in enumerate(s):
            for j in range(i+1,l):
                if self.isPalindrome(s[i:j+1]):
                    r.append((i,j))

        return r

    def findDifPalindromes(self, s):
        l = len(s)
        r = []
        for i,c in enumerate(s):
            for j in range(i+1,l):
                if self.isPalindrome(s[i:j+1]):
                    # del anything contains me 
                    for ri,rt in enumerate(r):
                        if i >= rt[0] and j<=rt[1]:
                            r.pop(ri)

                    r.append((i,j))
                    break

        return r


    def countStrings(self, s):
        ps = self.findDifPalindromes(s)

        l = len(s)
        c = 0
        excluded = 0
        last = -1
        for i,p in enumerate(ps):
            if p[0] <= last:
                excluded += p[1]-last
            else:
                excluded += p[1]-p[0]+1

            if excluded != 0 and last != -1:
                c += pow(2,l-(p[1]-p[0]+1))-pow(2,l-excluded)
            else:
                c += pow(2,l-(p[1]-p[0]+1))

            last = p[1]

        return c


if __name__ == "__main__":
    cp = ConsecutivePalindromes()
    ts = ["TOPPAPPOT","ABBCBCBBA","ABCBA","AAA"]
    for t in ts:
        print t,cp.countStrings(t)
    '''
    print cp.findPalindromes("ABCdCBA")
    print cp.findPalindromes("ABCCBA")
    print cp.findPalindromes("ABC")
    print cp.findPalindromes("A")
    print cp.findPalindromes("")
    '''

