# https://leetcode.com/problems/find-k-pairs-with-smallest-sums/description/?envType=problem-list-v2&envId=xo2bgr0r
def kSmallestPairs(nums1, nums2, k):
    if not nums1 or not nums2 or k == 0:
        return []

    heap = []
    result = []

    # Only push the first k elements in nums2 combined with nums1[0]
    for j in range(min(k, len(nums2))):
        heapq.heappush(heap, (nums1[0] + nums2[j], 0, j))

    while heap and len(result) < k:
        total, i, j = heapq.heappop(heap)
        result.append((nums1[i], nums2[j]))

        # Move to the next element in nums1 with the same nums2[j]
        if i + 1 < len(nums1):
            heapq.heappush(heap, (nums1[i+1] + nums2[j], i + 1, j))

    return result

