class YetAnotherORProblem2:
    def countSequences(self, n, r):
        ls = {0:1}
        c = 0
        mc = 1
        while mc < r:
            mc <<= 1
        mc -= 1
        for i in range(0, r+1):
            ls[i] = 1

        for i in range(0, n+1):
            if i == n:
                for k,v in ls.items():
                    c += v
                return c%1000000009
            cs = {0:0}
            for k,v in ls.items():
                mask = mc^k
                j = k & -k
                while j <= r:
                     cs[k+j] =  cs.get(k+j, 0) + v
                     j = ((j | ~k) + 1) & k
                     if j == 0:
                         break
            ls = cs.copy()

if __name__ == "__main__":
    print YetAnotherORProblem2().countSequences(2,2)
    print YetAnotherORProblem2().countSequences(2,3)
    print YetAnotherORProblem2().countSequences(3,3)
    print YetAnotherORProblem2().countSequences(7,1023)
    print YetAnotherORProblem2().countSequences(2,1024)
    print YetAnotherORProblem2().countSequences(10,14336)

    '''
    import re
    with open("testcases") as f:
        for line in f:
            info = re.findall(r"[0-9\-]+", line)
            para = [int(x) for x in info]
            seq = para[:-1]
            exp = para[-1]
            ret = ZigZag().longestZigZag(seq)
            print seq, exp
            if ret == exp:
                print "SUCCESS"
            else:
                print "FAIL", ret
    '''
   
