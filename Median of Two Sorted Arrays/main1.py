# in vscode running well but till error

class Solution:
    def findMedianSortedArrays(nums1, nums2) :
        def findMedian(nums1, nums2):
            M, N = len(nums1), len(nums2)
            low, high = 0, M
            while low <= high:
                i1 = (low + high) >> 1
                i2 = ((M + N + 1) >> 1) - i1
                leftMax1 = -float("inf") if i1 == 0 else nums1[i1 - 1]
                rightMin1 = float("inf") if i1 == M else nums1[i1]
                leftMax2 = -float("inf") if i2 == 0 else nums2[i2 - 1]
                rightMin2 = float("inf") if i2 == N else nums2[i2]
                if leftMax1 <= rightMin2 and leftMax2 <= rightMin1:
                    maxLeft = max(leftMax1, leftMax2)
                    if (M + N) % 2 == 1:
                        return maxLeft
                    return (maxLeft + min(rightMin1, rightMin2)) / 2
                elif leftMax1 > rightMin2:
                    high = i1 - 1
                else:
                    low = i1 + 1

        if len(nums1) <= len(nums2):
            return findMedian(nums1, nums2)
        return findMedian(nums2, nums1)

    nums1 = [1, 3]
    nums2 = [2, 4]
    result = findMedianSortedArrays(nums1, nums2)
    print(result)
