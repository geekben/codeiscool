class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        ip = prices[0]
        op = prices[0]
        ret = 0

        for p in prices[1:]:
            if p > op:
                op = p
            elif p < op:
                if op > ip:
                    ret += op - ip
                ip = p
                op = p
        ret += op - ip
        return ret
