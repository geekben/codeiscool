class YetAnotherTwoTeamsProblem:
    def count(self, skill):
        ss = 0
        for i in skill:
            ss += i
        #skill.sort()
        mask = (1 << len(skill)) - 1
        stat = {0:0}
        sm = {0:100000}
        su = {}
        c = 0
        for idx,s in enumerate(skill):
            i = 1<<(idx+1)
            for j in stat.keys():
                n = i|j
                if i == j or stat[j] < 0 or stat.get(n, 1) < 0:
                    continue

                temp = s + stat[j]
                sm[n] = min(sm[j], s)
                h = su.get(temp, {}).get(sm[n], 0)
                stat[n] = temp
                if h != 0:
                    if h == -2:
                        c += 1
                        stat[mask^n] = -1
                    elif h == -1:
                        stat[mask^n] = -1
                    continue

                d = ss - temp
                if temp < d:
                    stat[n] = temp
                elif temp == d:
                    stat[n] = -1
                    stat[mask^n] = -1
                else:
                    if temp - d < sm[n]*2:
                        stat[n] = -2
                        stat[mask^n] = -1
                        c += 1
                    else:
                        stat[n] = -1
                ht = su.get(temp, {})
                if ht == {}:
                    su[temp] = {sm[n]:stat[n]}
                else:
                    ht[sm[n]] = stat[n]

        return c

if __name__ == "__main__":
    import re
    with open("testcases") as f:
        for line in f:
            info = re.findall(r"[0-9\-]+", line)
            para = [int(x) for x in info]
            seq = para[:-1]
            exp = para[-1]
            ret = YetAnotherTwoTeamsProblem().count(seq)
            print seq, exp
            if ret == exp:
                print "SUCCESS"
            else:
                print "FAIL", ret
   

