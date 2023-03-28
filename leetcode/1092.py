class Solution(object):
    def shortestCommonSupersequence(self, str1, str2):
        """
        :type str1: str
        :type str2: str
        :rtype: str
        """
        l1 = len(str1)
        l2 = len(str2)
        ret = ""
        if l1 == 0:
            return str2
        if l2 == 0:
            return str1
        if str1[0] == str2[0]:
            ret = str1[0] + \
                self.shortestCommonSupersequence(str1[1:], str2[1:])
        else:
            t1 = str1[0] + \
                self.shortestCommonSupersequence(str1[1:], str2)
            t2 = str2[0] + \
                self.shortestCommonSupersequence(str1, str2[1:])
            if len(t1) <= len(t2):
                ret = t1
            else:
                ret = t2
        return ret
