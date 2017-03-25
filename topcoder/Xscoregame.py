class Xscoregame:
    def getscore(self, a):
        r = []
        s = {}

        def dfs(x,a):
            t = []
            for y in a:
                tx = x
                ta = a[:]
                ta.remove(y)
                tx = tx + (tx^y)
                if ta == []:
                    return tx
                t.append(dfs(tx, ta))
            return max(t)

        ret = dfs(0, a)
        return ret

if __name__ == "__main__":
    print Xscoregame().getscore([1,2,3])
    print Xscoregame().getscore([10,0,0,0])
    print Xscoregame().getscore([1,1,1,1,1,1])
    print Xscoregame().getscore([1,0,1,0,1,0,1,0])
    print Xscoregame().getscore([50,0,1,0,1,0,1,0,1,0,1,0,1,0,1])
