class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        n = len(arr)
        left = 1
        right = n - 2
        while left <= right:
            mid = (left + right) // 2
            if arr[mid-1] < arr[mid] > arr[mid+1]:
                return mid
            if arr[mid-1] < arr[mid]:
                left = mid + 1
            else:
                right = mid - 1