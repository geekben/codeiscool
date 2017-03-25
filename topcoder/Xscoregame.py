class Xscoregame:
    def getscore(self, a):
        s = {(0,0):0}
        n = len(a)

        ln = 1<<n
        for i in range(0, ln):
            for j in range(0, 64):
                if s.get((i,j), -1) < 0:
                    continue
                for idx,k in enumerate(a):
                    e = 1 << idx
                    if e & i > 0:
                        continue
                    t = s[(i,j)]
                    t += t ^ k
                    ni = i|e
                    nj = t%64
                    s[(ni, nj)] = max(s.get((ni, nj),-1), t)

        ret = 0
        nn = ln - 1
        for j in range(0, 64):
            ret = max(ret, s.get((nn,j),-1))

        return ret

if __name__ == "__main__":
    print Xscoregame().getscore([1,2,3])
    print Xscoregame().getscore([10,0,0,0])
    print Xscoregame().getscore([1,1,1,1,1,1])
    print Xscoregame().getscore([1,0,1,0,1,0,1,0])
    print Xscoregame().getscore([50,0,1,0,1,0,1,0,1,0,1,0,1,0,1])

