class Solution(object):
    def bSearch(self, a, l, r, v):
        """
        binary search
        to find the posion for v in a
        between l and r
        """
        if l == r:
            if a[l] > v:
                return l+1
            else:
                return l
        if l == r - 1:
            if a[l] < v:
                return l
            elif a[l] > v and v > a[r]:
                return r
            else:
                return r+1

        mid = (l+r)/2
        if a[mid] > v:
            return self.bSearch(a,mid+1, r, v)
        else:
            return self.bSearch(a, l, mid-1, v)

s = Solution()
k = 3
a = [12,11,10,9,3, 3,2,2,1]
print k,a
i = s.bSearch(a,0,len(a)-1, k)
a.insert(i, k)
print a
