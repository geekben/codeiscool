'''
[1,2,3,10,4,2,3,5]
[1]
[5,4,3,2,1]
[5,6,7,8,1,1,1,1,1,2,3,4,5]
[5,6,7,8,1,1,1,1,1,2,3,4]
[5,6,7,8,0,1,1,1,1,2,3,4,5]
[5,6,7,8,0,1,1,1,1,2,3,4]
[5,6,7,8,0,1,1,1,1,0,1,0,2,3,4]
[5,6,7,8,0,1,1,1,1,2,3,4,5,6]
[1,2,3,10,11,4,12,2,3,5]
[22,37,59,16,42,32,29,53,9,55,29,3,4,1,49,17,37,31,27,45,33,24,54,51,32,51,54,31,36,53]
'''
class Solution(object):
    def findLengthOfShortestSubarray(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        he = 0
        la = len(arr)
        if la == 1:
            return 0
        hc = la - 1
        mc = la
        tc = la - 1

        for i in xrange(1,la):
            if arr[i] < arr[i-1]:
                he = i - 1
                break
            else:
                tc -= 1
        if tc == 0:
            return 0

        i = la - 1
        tl,tr = 0,he
        while i >= 0:
            if i < la - 1 and arr[i] > arr[i+1]:
                hc = i + 1
                break
            if arr[i] >= arr[he]:
                mc = min(mc, i - he - 1)
                i -= 1
                continue
            if arr[i] < arr[0]:
                mc = min(mc, i - 0)
                i -= 1
                continue
            
            while tl < tr - 1:
                tp = (tl+tr)/2
                if arr[i] < arr[tp]:
                    tr = tp
                else:
                    tl = tp
            #print tl,tr,tp,arr[tp],arr[i]
            if arr[i] >= arr[tr]:
                mc = min(mc, i - tr - 1)
                tl,tr = 0,tr
            elif arr[i] >= arr[tl]:
                mc = min(mc, i - tl - 1)
                tl,tr = 0,tl
            i -= 1
        #print he, hc, mc, tc
        return min(hc,mc,tc)
