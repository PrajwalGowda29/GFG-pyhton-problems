class Solution:
   def countWithout(self, n: int, d: int) -> int:
    s = str(n)
    memo = {}

    def dp(pos, tight, started):
        if pos == len(s):
            return 1 if started else 0

        key = (pos, tight, started)

        if key in memo:
            return memo[key]

        limit = int(s[pos]) if tight else 9
        ans = 0

        for digit in range(limit + 1):

            # Leading zero is not considered a digit
            if digit == d and (started or d != 0):
                continue

            new_started = started or digit != 0
            new_tight = tight and digit == int(s[pos])

            ans += dp(pos + 1, new_tight, new_started)

        memo[key] = ans
        return ans

    return dp(0, True, False)