class YetAnotherRobotSimulation:
    def __init__(self):
        self.am = [-1, 1, -2, 2]
        self.yes = {}
        self.l = 0 
        self.tp = [] 

    def go(self,m,s):
        if len(m) >= self.l:
            if s in self.tp:
                self.yes[m] = self.yes.get(m, 0) + 1
            return

        for j in self.am:
            if j == -1:
                p = list(s)
                p[0] -= 1
            elif j == 1:
                p = list(s)
                p[0] += 1
            elif j == -2:
                p = list(s)
                p[1] -= 1
            elif j == 2:
                p = list(s)
                p[1] += 1

            nm = tuple(list(m)+[j])
            sn = tuple(p)

            self.go(nm, s)
            self.go(nm, sn)


    def getMaximumProbability(self,l,x,y):
        self.l = l
        px = tuple(x)
        py = tuple(y)
        tl = len(px)
        for i in range(0, tl):
            self.tp.append((px[i],py[i]))

        self.go((),(0,0))
        
        mp = 0
        for i,v in self.yes.items():
            if mp < v:
                mp = v

        #print self.yes
        return float(mp)/(1<<l)

if __name__ == "__main__":
    l = 3
    x = [1,2,2]
    y = [1,1,0]
    print YetAnotherRobotSimulation().getMaximumProbability(l,x,y)
    l = 1
    x = [0]
    y = [0]
    print YetAnotherRobotSimulation().getMaximumProbability(l,x,y)
    l = 36
    x = [6,7,12,-21,5,5,2,4]
    y = [4,5,-2,4,5,12,5,7]
    #print YetAnotherRobotSimulation().getMaximumProbability(l,x,y)
    l = 8
    x = [2,3,3]
    y = [1,1,0]
    #print YetAnotherRobotSimulation().getMaximumProbability(l,x,y)
    l = 5
    x = [0,0,0,0]
    y = [0,1,2,3]
    print YetAnotherRobotSimulation().getMaximumProbability(l,x,y)

    
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
   
