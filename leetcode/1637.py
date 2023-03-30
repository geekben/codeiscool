class Solution(object):
    def maxWidthOfVerticalArea(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        points = sorted(points, key=lambda point: point[0])
        width = 0

        for i in xrange(1, len(points)):
            width = max(width, points[i][0]-points[i-1][0])
        return width
