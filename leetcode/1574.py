class Solution(object):
    def findLengthOfShortestSubarray(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        he = 0
        hc = 0
        la = len(arr)
        if la == 1:
            return 0
        mc = la
        tc = la - 1

        for i in xrange(1,la):
            if arr[i] < arr[i-1]:
                he = i - 1
                break
            else:
                tc -= 1
        hc = la - 1
        for i in xrange(la-2,0,-1):
            if arr[i] > arr[i+1]:
                hc = i + 1
                break
        if tc == 0:
            return 0

        i = hc
        tl,tr = 0,he
        while i < la:
            if arr[i] >= arr[he]:
                mc = min(mc, i - he - 1)
                break
            if arr[i] < arr[0]:
                mc = min(mc, i - 0)
                i += 1
                continue
            
            while tl < tr - 1:
                tp = (tl+tr)/2
                if arr[i] < arr[tp]:
                    tr = tp
                else:
                    tl = tp
            # print tl,tr,tp,arr[tp],arr[i]
            if arr[i] >= arr[tr]:
                mc = min(mc, i - tr - 1)
                tl,tr = tr,he
            elif arr[i] >= arr[tl]:
                mc = min(mc, i - tl - 1)
                tl,tr = tl,he
            i += 1
        #print he, hc, mc, tc
        return min(hc,mc,tc)
