class Solution(object):
    def minOperationsMaxProfit(self, customers, boardingCost, runningCost):
        """
        :type customers: List[int]
        :type boardingCost: int
        :type runningCost: int
        :rtype: int
        """
        if 4*boardingCost <= runningCost:
            return -1
        ll = len(customers)
        mr = 10000000
        mp = 0
        p = 0
        for i,c in enumerate(customers):
            if c <= 4:
                p += c*boardingCost - runningCost
            else:
                p += 4*boardingCost - runningCost
                if i+1 < ll:
                    customers[i+1] += c - 4
                else:
                    customers.append(c-4)
            if p > 0 and p >= mp:
                if p == mp:
                    if i + 1 < mr:
                        mr = i + 1
                else:
                    mp = p
                    mr = i + 1
                # print p,mp,mr
        if mr == 10000000:
            return -1
        return mr
