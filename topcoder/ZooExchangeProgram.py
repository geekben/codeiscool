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
        state = {0:0}
        mode = []

        for i in ng:
            temp = 0
            for j in i:
                temp += 1<<(j-1)
            mode.append(temp)
            state[temp] = 1

        for m in mode:
            for i in state.keys():
                state[i|m] = min(state.get(i|m,50), state.get(i,50)+1)
        return state[(1<<upper)-(1<<(lower-1))]

if __name__ == "__main__":
    '''
    label = [7, 12, 2, 12, 10, 13, 6, 5, 3, 3, 4, 11, 12, 4, 3, 1, 8, 11, 4, 7, 6, 5, 47]
    print ZooExchangeProgram().getNumber(label, 2, 7)
    label2 = [7, 12, 2, 12, 10, 13, 6, 5, 3, 3, 4, 11, 12, 4, 3, 1, 8, 11, 4, 7, 6, 5, 47, 7, 22, 4, 3, 1, 8, 22, 2, 6, 22, 3, 4, 8, 1]
    print ZooExchangeProgram().getNumber(label2, 2, 7)
    label3 = [3, 4, 3, 1, 6, 2, 5, 7, 5, 2]
    print ZooExchangeProgram().getNumber(label3, 2, 6)
    label4 = [2, 1, 3]
    print ZooExchangeProgram().getNumber(label4, 1, 3)
    label5 = [3, 4, 1, 3, 4, 2]
    print ZooExchangeProgram().getNumber(label5, 1, 3)
    label6 = [2, 1, 3, 1, 4]
    print ZooExchangeProgram().getNumber(label6, 1, 4)
    label7 = [3, 1, 4]
    print ZooExchangeProgram().getNumber(label7, 2, 4)
    '''
    label8 = [15, 4, 16, 11, 17, 1, 18, 11, 19, 6, 20, 4, 21, 6, 22, 11, 23, 9, 24, 4, 25, 46, 26, 1, 27, 14, 28, 1, 29, 6, 30, 13, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42]
    print ZooExchangeProgram().getNumber(label8, 15, 42)

    '''
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
    '''



