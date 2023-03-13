'''
1
1
[1,1,1,1]
[1,1,1,50]
5
3
[1,4,3,2]
[2,6,3,1]
2
4
[1]
[3]
5
3
[1,4,3,2,4,3,2,4,3,2,4,3,2,4,3,2,4,3,2,4,3,2,4,3,2,4,3,2,4,3,2,4,3,2,4,3,2,4,3,2,4,3,2,4,3,2,2,4,3,2,2,4,3,2,2,4,3,2,2,4,3,2,4,3,2,4,3,2,4,3,2,4,3,2,4,3,2,4,3,2,4,3,2,4,3,2,4,3,2,4,3,2,4,3,2,4,3,2,2]
[2,6,3,1,6,3,1,6,3,1,6,3,1,6,3,1,6,3,1,6,3,1,6,3,1,6,3,1,6,3,1,6,3,1,6,3,1,6,3,1,6,3,1,6,3,1,6,3,1,6,3,1,6,3,1,6,3,1,6,3,1,6,3,1,6,3,1,6,3,6,3,1,6,3,1,6,3,1,6,3,1,6,3,1,6,3,1,6,3,6,3,1,6,3,1,6,3,1,6]
'''
class Solution(object):
    def minNumberOfHours(self, initialEnergy, initialExperience, energy, experience):
        """
        :type initialEnergy: int
        :type initialExperience: int
        :type energy: List[int]
        :type experience: List[int]
        :rtype: int
        """
        n = len(energy)
        ey = initialEnergy
        ep = initialExperience
        hours = 0

        for i in xrange(n):
            # print ey,ep,hours
            if ey > energy[i]:
                ey -= energy[i]
            else:
                hours += energy[i] - ey + 1
                ey = 1

            if ep > experience[i]:
                ep += experience[i]
            else:
                hours += experience[i] - ep + 1
                ep = 1 + experience[i] + experience[i]
        return hours
