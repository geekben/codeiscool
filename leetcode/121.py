class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        ret = 0
        ip = prices[0]
        op = prices[0]
        for p in prices[1:]:
            if p > op:
                op = p
            elif p < ip:
                if op > ip:
                    ret = max(ret, (op-ip))
                op = p
                ip = p

        return max(ret, op-ip)
