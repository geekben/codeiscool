class YetAnotherCardGame:
    def maxCards(self, p, s):
        p = list(p)
        s = list(s)
        p.sort()
        s.sort()
        sp = list(set(p))

        ss = []
        ret = []
        ii = 0

        for i in sp:
            p.remove(i)
        p = sp + p
        sp.append(101)
        print p

        for i in p:
            if i == 101:
                break
            if ret == [] or i > ret[-1]:
                ret.append(i)
                ii += 1
            eat = True

            st = s[:]
            for j in st:
                #print "==",ret[-1],sp[ii],j, s, ss
                if j > ret[-1] and j < sp[ii]:
                    ret.append(j)
                    eat = False
                    del s[0]
                elif j <= sp[ii]:
                    ss.append(j)
                    del s[0]
            if eat:
                if len(ss) > 0:
                    del ss[0]
                elif len(s) > 0:
                    s.pop()

        return len(ret)

if __name__ == "__main__":
    print YetAnotherCardGame().maxCards([2,5],[3,1])
    print YetAnotherCardGame().maxCards({1, 4, 6, 7, 3},{1,7,1,5,7})
    print YetAnotherCardGame().maxCards([1]*5,[1]*5)
    print YetAnotherCardGame().maxCards([19, 99, 86, 30, 98, 68, 73, 92, 37, 69, 93, 28, 58, 36, 86, 32, 46, 34, 71, 29],
            [28, 29, 22, 75, 78, 75, 39, 41, 5, 14, 100, 28, 51, 42, 9, 25, 12, 59, 98, 83])
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
