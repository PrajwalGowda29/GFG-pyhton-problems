class Solution:
    def maxTask(self, h: list[int], l: list[int]) -> int:
        # dp0 = maximum tasks if no task is done today
        # dp1 = maximum tasks if a task is done today

        dp0 = 0
        dp1 = h[0]

        for i in range(1, len(h)):
            
            # No task today
            new_dp0 = max(dp0, dp1)

            # Do low-effort task today
            low = max(dp0, dp1) + l[i]

            # Do high-effort task today
            # Previous day must have no task
            high = dp0 + h[i]

            new_dp1 = max(low, high)

            dp0 = new_dp0
            dp1 = new_dp1

        return max(dp0, dp1)