class Solution:
    def nCr(self, n, r):
        if r > n:
            return 0

        fact_n = 1
        fact_r = 1
        fact_nr = 1

        for i in range(1, n + 1):
            fact_n *= i

        for i in range(1, r + 1):
            fact_r *= i

        for i in range(1, n - r + 1):
            fact_nr *= i

        return fact_n // (fact_r * fact_nr)