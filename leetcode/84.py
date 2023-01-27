class Solution(object):
    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        a = heights[0]
        h = heights[0]
        e = 1
        maxa = a
        st = [[h, a]]
        stl = 1 #st length

        for r in heights[1:]:
            for i,s in enumerate(st[:e]):
                k = s[0]
                if r == k:
                    s[1] += k
                    e = i + 1
                    if maxa < s[1]:
                        maxa = s[1]
                    break
                elif r > k:
                    s[1] += k
                    if i + 1 == e:
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
                else:
                    st[i] = [r, r+s[1]/k*r]
                    if st[i][1] > maxa:
                        maxa = st[i][1]
                    e = i + 1
                    break
            #print r,st[:e],maxa

        return maxa
