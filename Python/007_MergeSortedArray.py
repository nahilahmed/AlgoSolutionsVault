def solution(nums1, nums2, m, n):

    if n == 0:
        return
    len1 = len(nums1)
    end_idx = len1 - 1
    while n > 0 and m > 0:
        if nums2[n - 1] >= nums1[m - 1]:
            nums1[end_idx] = nums2[n - 1]
            n -= 1
        else:
            nums1[end_idx] = nums1[m - 1]
            m -= 1
        end_idx -= 1
        print(nums1)
    while n > 0:
        nums1[end_idx] = nums2[n - 1]
        n -= 1
        end_idx -= 1
        print(nums1)


nums1 = [1, 2, 3, 0, 0, 0]
m = 3
nums2 = [2, 5, 6]
n = 3
solution(nums1, nums2, m, n)
print(nums1)

"""
https://leetcode.com/problems/merge-sorted-array/solutions/4722196/simple-beginner-friendly-dry-run-two-pointer-loops-time-o-m-n-space-o-1-gits/?envType=study-plan-v2&envId=top-interview-150

Code Explanation 👈
Early return if nums2 is empty: The condition if(n == 0)return; checks if nums2 is empty (n == 0). If it is, there's nothing to merge, so the function returns immediately.

Setup for merging: It initializes end_idx to the last index of nums1 (len1 - 1), which is where the highest element of the merged array will be placed.

Merging from the end: The code uses a while loop to compare elements from the end of nums1 and nums2, placing the larger of the two in the current end_idx position of nums1. This process continues until either all elements from nums1 (m elements) have been processed or all elements from nums2 (n elements) have been placed into nums1. This ensures that if nums1 has larger elements at the end, they are moved to their correct position in the merged array, making space for nums2's elements.

If nums2[n-1] >= nums1[m-1], it places nums2[n-1] at nums1[end_idx], and decrements n and end_idx.
Otherwise, it moves nums1[m-1] to nums1[end_idx], and decrements m and end_idx.
Handling remaining elements in nums2: After the first loop, if there are still elements left in nums2 (n > 0), it means all elements in nums1 that were part of the original array (m elements) have been merged, and the remaining elements in nums2 should be copied over. This is handled by the second while loop, which continues placing elements from nums2 into nums1 until nums2 is empty.

Result: At the end of the process, nums1 contains the merged sorted elements of both nums1 and nums2. The algorithm efficiently utilizes the empty space at the end of nums1 and merges the arrays from the end, which allows it to work in-place without needing additional space for the result.

"""
