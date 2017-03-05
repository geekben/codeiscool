#https://community.topcoder.com/stat?c=problem_solution&rm=306081&rd=14285&pm=11014&cr=19849563

class YetAnotherRobotSimulation:
    def getMaximumProbability(self,L,x,y):
        px = tuple(x)
        py = tuple(y)
        tl = len(px)
        tp = []
        for i in range(0, tl):
            tp.append((px[i],py[i]))

        c = [] 
        # quick search table for number of combinations
        for i in range(0, 51):
            c.append([])
            for j in range(0, i+1):
                if j == 0:
                    c[i].append(1)
                else:
                    if j > i-1:
                        c[i].append(c[i-1][j-1])
                    else:
                        c[i].append(c[i-1][j-1]+c[i-1][j])

        m = 0
        u = r = l = d = 0
        for u in range(0, L+1):
            for r in range(0, L-u+1):
                for l in range(0, L-u-r+1):
                    # different order, same result
                    d = L-u-r-l
                    s = 0
                    pu = pr = pl = pd = 0
                    for pu in range(0,u+1):
                        for pr in range(0,r+1):
                            for pl in range(0,l+1):
                                for pd in range(0,d+1):
                                    if (pr-pl, pu-pd) in tp:
                                        s += c[u][pu]*c[r][pr]*c[l][pl]*c[d][pd]
                                        m = max(s, m)

        return float(m)/(1<<L)

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
    print YetAnotherRobotSimulation().getMaximumProbability(l,x,y)
    l = 8
    x = [2,3,3]
    y = [1,1,0]
    print YetAnotherRobotSimulation().getMaximumProbability(l,x,y)
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
   
