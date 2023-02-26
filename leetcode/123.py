class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        p0 = prices[0]
        wo = []
        ip = p0
        op = p0
        tl = []

        for p in prices[1:]+[-1]:
            lw = len(wo)
            if lw < 2:
                if p > op:
                    op = p
                elif p < op:
                    if op > ip:
                        wo.append([ip, op])
                        tl.append(op-ip)
                        if len(wo) == 2:
                            tl.append(wo[1][1] - wo[0][0])
                    op = p
                    ip = p
            else:
                if p > op:
                    op = p
                elif p < op:
                    if op > ip:
                        v1 = tl[0] # only w1
                        v2 = tl[1] # only w2
                        v3 = tl[2] # w1 w2 combined
                        v4 = op - ip # only w3
                        v6 = op - wo[1][0] # w2 w3 combined
                        temp = [v1+v2, v1+v4, v2+v4, v3+v4, v1+v6]
                        mp = max(temp)
                        mi = temp.index(mp)
                        if mi == 0:
                            if p > ip:
                                continue
                        elif mi == 1: # w1 w3
                            wo[1] = [ip, op]
                            tl[1] = v4
                            tl[2] = op - wo[0][0]
                        elif mi == 2: # w2 w3
                            wo.pop(0)
                            wo.append([ip, op])
                            tl.pop(0)
                            tl[1] = v4
                            tl.append(op - wo[0][0])
                        elif mi == 3: # w1+2 w3
                            wo = [[wo[0][0],wo[1][1]], [ip, op]]
                            tl = [v3, v4, op-wo[0][0]]
                        elif mi == 4: # w1 w2+3
                            wo[1] = [wo[1][0], op]
                            tl[1] = v6
                            tl[2] = wo[1][1] - wo[0][0]
                    ip = p
                    op = p

        lw = len(wo)
        if lw == 0:
            return 0
        elif lw == 1:
            return tl[0]
        elif lw == 2:
            return tl[0]+tl[1]
