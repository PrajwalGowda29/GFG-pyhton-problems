class Solution:
  def isPossible(self, arr, s, x):
    nums = [s]
    total = s

    for a in arr:
        new_num = total + a
        nums.append(new_num)
        total += new_num

        if total > x and new_num > x:
            break

    # Greedily choose from largest to smallest
    for i in range(len(nums) - 1, -1, -1):
        if nums[i] <= x:
            x -= nums[i]

        if x == 0:
            return 1

    return 0