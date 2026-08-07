class Solution:
    def countFriendsPairings(self, n):
        if n <= 2:
            return n

        a = 1   # f(1)
        b = 2   # f(2)

        for i in range(3, n + 1):
            c = b + (i - 1) * a
            a = b
            b = c

        return b