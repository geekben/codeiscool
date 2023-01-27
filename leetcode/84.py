class Solution(object):
    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        h = 0
        e = 1
        maxa = heights[0]
        st = [[heights[0],heights[0]]]
        stl = 1 #st length
        ls = len(heights)

        for p,r in enumerate(heights[1:]):
            for i,s in enumerate(st[h:e]):
                k = s[0]
                if r == k:
                    s[1] += k
                    e = h + i + 1
                    if maxa < s[1]:
                        maxa = s[1]
                    if maxa > (ls-p)*k + s[1]:
                        h += 1
                    break
                elif r > k:
                    s[1] += k
                    if h + i + 1 == e:
                        if e >= stl:
                            st.append([r,r])
                            stl += 1
                        else:
                            st[e] = [r, r]
                        e += 1
                        if r > maxa:
                            maxa = r
                    if maxa < s[1]:
                        maxa = s[1]
                    if maxa > (ls-p)*k + s[1]:
                        h += 1
                else:
                    st[h+i] = [r, r+s[1]/k*r]
                    if st[h+i][1] > maxa:
                        maxa = st[h+i][1]
                    e = h + i + 1
                    if maxa > (ls-p)*k + s[1]:
                        h += 1
                    break
            #print r,st[:e],maxa

        return maxa
