class Solution(object):
    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        h = 0
        e = 1
        maxa = heights[0]
        st = [[heights[0],0]]
        stl = 1 #st length
        ls = len(heights)

        for p,r in enumerate(heights[1:]):
            s = st[e-1]
            k = s[0]
            if r == k:
                continue
            elif r > k:
                if e >= stl:
                    st.append([r, p+1])
                    stl += 1
                else:
                    st[e] = [r, p+1]
                e += 1
            else:
                while e > h and s[0] > r:
                    a = s[0]*(p+1-s[1])
                    if a > maxa:
                        maxa = a
                    e -= 1
                    s = st[e-1]
                if s[0] == r:
                    pass
                else:
                    st[e] = [r, st[e][1]]
                    e += 1
            #print r,st[:e],maxa

        for s in st[h:e]:
            a = s[0]*(ls-s[1])
            if a > maxa:
                maxa = a
        
        return maxa
