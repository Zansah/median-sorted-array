def findMedianSortedArrays(nums1, nums2):
    merged = sorted(nums1 + nums2)
    n = len(merged)
    if n % 2 != 0:
        return merged[n // 2]
    else:
        return (merged[n // 2 - 1] + merged[n // 2]) / 2

nums1 = list(map(int, input("Enter the sorted array nums1 separated by spaces: ").split()))
nums2 = list(map(int, input("Enter the sorted array nums2 separated by spaces: ").split()))

print("Median of the two sorted arrays:", findMedianSortedArrays(nums1, nums2))


