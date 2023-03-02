class Solution(object):
    def printBin(self, num):
        """
        :type num: float
        :rtype: str
        """
        i = 0.5
        c = 2
        d = "0."
        while num > 0 and c <= 32:
            if num == i:
                num -= i
                d = d + "1"
                break
            elif num > i:
                num -= i
                d = d + "1"
            else:
                d = d + "0"
            c += 1
            i /= 2.0
        if num == 0.0:
            return d
        else:
            return "ERROR"
