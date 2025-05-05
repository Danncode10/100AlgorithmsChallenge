class Solution:
    def allLongestStrings(self, inputArray):
        # Find the maximum string length
        max_len = max(len(s) for s in inputArray)
        # Return only strings with that maximum length
        return [s for s in inputArray if len(s) == max_len]


# ------ TEST ------#
ans = Solution()
inputArray = ["aba", "aa", "ad", "vcd", "aba"]
print(ans.allLongestStrings(inputArray))  # Output: ['aba', 'vcd', 'aba']
