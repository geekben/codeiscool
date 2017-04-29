class XorSequence:
    def getmax(self, n, sz, a0, a1, p, q, r):
        a = [a0, a1]
        for i in range(2, sz):
            a.append((a[i-2]*p%n+a[i-1]*q%n+r)%n)

        mr = 0
        for b in range(0,n):
            c = []
            ret = 0
            for j in range(0,sz):
                c.append(a[j]^b)
                for k in range(0,j):
                    if c[k] < c[j]:
                        ret += 1
            if ret > mr:
                mr = ret

        return mr

if __name__ == "__main__":
    print XorSequence().getmax(4,6,3,2,0,1,3)
    print XorSequence().getmax(8,8,2,5,3,1,4)
    print XorSequence().getmax(8,7,3,0,1,2,4)
    print XorSequence().getmax(32,15,7,9,11,2,1)
    print XorSequence().getmax(131072,131072,7,7,1,0,0)
