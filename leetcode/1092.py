class Solution(object):
    dp = {}
    str1 = ""
    str2 = ""

    def superseq(self, i, j):
        if (i,j) in self.dp:
            return self.dp[(i,j)]
        str1 = self.str1[i:]
        str2 = self.str2[j:]
        l1 = len(str1)
        l2 = len(str2)
        ret = ""
        if l1 == 0:
            self.dp[(i,j)] = str2
            return str2
        if l2 == 0:
            self.dp[(i,j)] = str1
            return str1

        if str1[0] == str2[0]:
            ret = str1[0] + \
                self.superseq(i+1, j+1)
        else:
            t1 = str1[0] + \
                self.superseq(i+1, j)
            t2 = str2[0] + \
                self.superseq(i, j+1)
            if len(t1) <= len(t2):
                ret = t1
            else:
                ret = t2
        self.dp[(i,j)] = ret
        return ret

    def shortestCommonSupersequence(self, str1, str2):
        """
        :type str1: str
        :type str2: str
        :rtype: str
        """
        self.dp = {}
        self.str1 = str1
        self.str2 = str2
        ret = self.superseq(0,0)
        return ret
