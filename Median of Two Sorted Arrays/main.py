# Time Limit Exceeded

def findMedianSortedArrays(nums1, nums2):
    if len(nums1) > len(nums2):
        nums1, nums2 = nums2, nums1

    m, n = len(nums1), len(nums2)
    low, high = 0, m

    while low <= high:
        partition1 = (low + high) // 2
        partition2 = (m + n + 1) // 2 - partition1

        max_left_1 = float('-inf') if partition1 == 0 else nums1[partition1 - 1]
        max_left_2 = float('-inf') if partition2 == 0 else nums2[partition2 - 1]
        min_right_1 = float('inf') if partition1 == m else nums1[partition1]
        min_right_2 = float('inf') if partition2 == n else nums2[partition2]

        if max_left_1 <= min_right_2 and max_left_2 <= min_right_1:
            if (m + n) % 2 == 0:
                return (max(max_left_1, max_left_2) + min(min_right_1, min_right_2)) / 2.0
            else:
                return max(max_left_1, max_left_2)
        elif max_left_1 > min_right_2:
            high = partition1 - 1
        else:
            low = partition1 + 1

 
#Tester code
 print(findMedianSortedArrays([1,2,7], [6,7,10]))
