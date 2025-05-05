class Solution:
    # Function to return the sum of two numbers
    def add(self, param1, param2):
        return param1 + param2

    # Function to return the sum of any number of parameters
    def addAll(self, *args):
        total = 0
        for num in args:
            total += num
        return total


# ------ TEST ------#
ans = Solution()
print(ans.add(1, 2))             # Output: 3
print(ans.addAll(1, 2, 3, 4))    # Output: 10
print(ans.addAll(-5, 15, 20))    # Output: 30
