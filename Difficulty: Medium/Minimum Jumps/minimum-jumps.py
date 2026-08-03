class Solution:
    def minJumps(self, arr):
        n = len(arr)

        # If array has only one element
        if n == 1:
            return 0

        # If first element is 0, we cannot move
        if arr[0] == 0:
            return -1

        jumps = 1
        maxReach = arr[0]
        steps = arr[0]

        for i in range(1, n):

            # Reached the last index
            if i == n - 1:
                return jumps

            # Update the farthest reachable index
            maxReach = max(maxReach, i + arr[i])

            # Use one step to move to the current index
            steps -= 1

            # No more steps left, so take another jump
            if steps == 0:
                jumps += 1

                # Cannot move further
                if i >= maxReach:
                    return -1

                # Reset steps based on the new maximum reach
                steps = maxReach - i

        return -1