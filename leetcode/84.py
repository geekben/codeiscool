class Solution(object):
    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        a = heights[0]
        h = heights[0]
        maxa = a
        st = [[h, a]]

        for r in heights[1:]:
            ls = len(st)
            stt = st[:]
            for i,s in enumerate(stt):
                k = s[0]
                if r == k:
                    s[1] += k
                elif r > k:
                    s[1] += k
                    if i+1 >= ls:
                        st.append([r, r])
                else:
                    for t in st[i:]:
                        if t[1] > maxa:
                            maxa = t[1]
                    st = st[:i]
                    st.append([r, r+s[1]/k*r])
                    break

        for s in st:
            if s[1] > maxa:
                maxa = s[1]
        return maxa
