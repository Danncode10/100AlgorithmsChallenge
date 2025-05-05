class Solution:
    def addTwoDigits(self, n):
        # Convert number to string, split into digits, convert back to int, and sum
        return sum(int(digit) for digit in str(n))


# ------ TEST ------#
ans = Solution()
print(ans.addTwoDigits(29))  # Output: 11
print(ans.addTwoDigits(47))  # Output: 11
print(ans.addTwoDigits(10))  # Output: 1
