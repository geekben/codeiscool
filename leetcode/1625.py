class Solution(object):
    def findLexSmallestString(self, s, a, b):
        """
        :type s: str
        :type a: int
        :type b: int
        :rtype: str
        """
        ls = len(s)
        #sn = [int(s[i]) for i in xrange(ls)]
        #mi = -1
        #mn = -1
        ms = "9"*ls

        i = 0
        st = []
        if a == 5:
            j_limit = 1
        elif a % 2 == 0:
            j_limit = 4
        else:
            j_limit = 9

        while i not in st:
            st.append(i)
            for j in xrange(0,j_limit+1):
                j2_limit = (b % 2)*j_limit
                for j2 in xrange(0,j2_limit+1):
                    sv = ""
                    for k in xrange(i,i+ls):
                        if k % 2 == 0:
                            t = (int(s[k%ls]) + a * j2) % 10
                        else:
                            t = (int(s[k%ls]) + a * j) % 10
                        sv += str(t)
                    ms = min(sv, ms)
            i = (i+b)%ls

        return ms
