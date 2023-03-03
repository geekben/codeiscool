class Solution(object):
    def getFolderNames(self, names):
        """
        :type names: List[str]
        :rtype: List[str]
        """
        st = {}
        ans = []
        for n in names:
            if n in st:
                pn = n[:]
                k = st[n]
                n = n + "("+str(k)+")"
                while n in st:
                    k += 1
                    n = pn + "("+str(k)+")"
                st[pn] = k + 1
            st[n] = 1
            ans.append(n)

        return ans
