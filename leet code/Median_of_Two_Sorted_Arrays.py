class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        mrg = [None]*(len(nums1) + len(nums2))
        i = j = k = 0
        while i < len(nums1) and j < len(nums2):
            if nums1[i] < nums2[j]:
                mrg[k] = nums1[i]
                i += 1
                k += 1
            elif nums2[j] < nums1[i]:
                mrg[k] = nums2[j]
                j += 1
                k += 1
            elif nums1[i] == nums2[j]:
                mrg[k] = nums1[i]
                i += 1
                k += 1
        while i < len(nums1):
            mrg[k] = nums1[i]
            i += 1
            k += 1
        while j < len(nums2):
            mrg[k] = nums2[j]
            j += 1
            k += 1
        
        n = len(mrg)
        if n % 2 == 0:
            a = mrg[(n/2)-1]
            b = mrg[n/2]
            c = (float)(a + b)/2
            return c
        else:
            return ( mrg[n//2])
        
