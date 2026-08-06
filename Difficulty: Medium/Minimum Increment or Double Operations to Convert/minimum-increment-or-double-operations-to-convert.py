class Solution:
    def countMinOperations(self, arr):
        ans = 0

        while True:
            zero = 0
            even = True

            for i in range(len(arr)):
                if arr[i] == 0:
                    zero += 1
                elif arr[i] % 2 == 1:
                    even = False

            if zero == len(arr):
                break

            if even:
                for i in range(len(arr)):
                    arr[i] //= 2
                ans += 1
            else:
                for i in range(len(arr)):
                    if arr[i] % 2 == 1:
                        arr[i] -= 1
                        ans += 1

        return ans