'''
[1,2,3,0,0,0]
3
[2,5,6]
3
[1]
1
[]
0
[0]
0
[1]
1
[1,2,3,4,0,0,0]
4
[4,5,6]
3
[5,6,7,8,0,0,0]
4
[1,2,3]
3
'''
class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        a = nums1[:m]
        b = nums2
        p = 0
        q = 0

        while p < m and q < n:
            if a[p] <= b[q]:
                nums1[p+q] = a[p]
                p += 1
            else:
                nums1[p+q] = b[q]
                q += 1

        while p < m:
            nums1[p+q] = a[p]
            p += 1
        while q < n:
            nums1[p+q] = b[q]
            q += 1
