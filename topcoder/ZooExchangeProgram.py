# https://community.topcoder.com/stat?c=problem_solution&cr=10574855&rd=16187&pm=13268

class ZooExchangeProgram:
    def getNumber(self, label, lower, upper):
        l = list(label)
        r = range(lower, upper+1)
        for i in r:
            if i not in l:
                return -1

        groups = []
        start = 0
        for i,x in enumerate(l):
            if x not in r:
                if start < i:
                    groups.append(set(l[start:i]))
                start = i + 1
            elif i == len(l) - 1:
                groups.append(set(l[start:i+1]))

        # deduplicate groups
        ng = []
        for i in groups:
            if i not in ng:
                ng.append(i)

        # tricky part:
        count = [0] * 50
        state = {0:0}
        mode = []
        musk = 0
        ret = 0

        for i in ng:
            for j in i:
                count[j] += 1
        for i in ng:
            temp = 0
            only = False
            for j in i:
                if count[j] == 1:
                    only = True
                temp += 1<<(j-1)
            if not only:
                mode.append(temp)
                state[temp] = 1
            else:
                musk |= temp
                ret += 1

        if musk == (1<<upper)-(1<<(lower-1)):
            return ret

        best = 50
        for m in mode:
            for i in state.keys():
                state[i|m] = min(state.get(i|m,50), state.get(i,50)+1)
                if musk|i|m  == (1<<upper)-(1<<(lower-1)):
                   best = min(best, ret+state[i|m])

        return best

if __name__ == "__main__":
    label = [12, 38, 13, 38, 14, 1, 15, 37, 16, 6, 17, 8, 18, 5, 19, 8, 20, 11, 21, 35, 22, 8, 23, 1, 24, 9, 25, 37, 26, 6, 27, 2, 28, 36, 29, 46, 30, 38, 31, 35, 32, 43, 33, 34]
    print ZooExchangeProgram().getNumber(label, 12, 34)
    label = [10, 44, 46, 9, 42, 32, 47, 7, 43, 41, 6, 33, 2, 41, 24, 15, 10, 23, 40, 16, 7, 40, 21, 47, 47, 47, 42, 27, 44, 37, 1, 8, 47, 29, 46, 46, 34, 44, 40, 45, 37, 47, 46, 4]
    print ZooExchangeProgram().getNumber(label, 40, 47)

    import re

    with open('testcases') as f:
        for line in f:
            info = re.findall(r"[0-9\-]+", line)
            para = [int(x) for x in info]
            exp = para[-1]
            ret = ZooExchangeProgram().getNumber(para[:-3], para[-3], para[-2])
            if exp == ret:
                print para,"SUCCESS"
            else:
                print para,"FAIL",ret
