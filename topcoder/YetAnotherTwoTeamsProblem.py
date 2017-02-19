# http://www.luo666.com/?p=129
# system test failed, but has passed all testcases from
# https://community.topcoder.com/stat?c=problem_solution&cr=23159180&rd=15703&pm=12750
class YetAnotherTwoTeamsProblem:
    def count(self, skill):
        ss = 0
        for i in skill:
            ss += i
        sm = ss/2
        skill.sort(reverse=True)
        stat = {0:1}
        c = 0
        for i in skill:
            for j in range(sm-i+1, sm+1):
                t = i+j
                if (j == 0 or j >= i) and t > ss-t and j < ss-j:
                    c += stat.get(j, 0)
            for j in range(sm+i, i-1, -1):
                stat[j] = stat.get(j, 0) + stat.get(j-i, 0)

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
   

