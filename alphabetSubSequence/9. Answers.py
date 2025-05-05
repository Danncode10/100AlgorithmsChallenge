class Solution:
    def alphabetSubsequence(self, s):
        # Check if each character in the string appears in increasing order in the alphabet
        for i in range(1, len(s)):
            if s[i] <= s[i - 1]:  # If the current character is not greater than the previous one
                return False
        return True


# ------ TEST ------#
ans = Solution()
print(ans.alphabetSubsequence("effg"))  # Output: False
print(ans.alphabetSubsequence("cdce"))  # Output: False
print(ans.alphabetSubsequence("ace"))   # Output: True
print(ans.alphabetSubsequence("bxz"))   # Output: True
