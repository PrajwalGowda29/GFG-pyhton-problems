class Solution:
    def maxSubarraySum(self, arr):
        # Initialize with the first element
        current_sum = arr[0]
        max_sum = arr[0]

        # Traverse the array
        for i in range(1, len(arr)):
            current_sum = max(arr[i], current_sum + arr[i])
            max_sum = max(max_sum, current_sum)

        return max_sum