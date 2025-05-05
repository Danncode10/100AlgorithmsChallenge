class Solution:
    def almostIncreasingSequence(self, sequence):
        def isIncreasing(seq):
            for i in range(1, len(seq)):
                if seq[i] <= seq[i - 1]:
                    return False
            return True

        for i in range(len(sequence)):
            # Create a new sequence without the i-th element
            temp = sequence[:i] + sequence[i+1:]
            if isIncreasing(temp):
                return True

        return False


# ------ TEST ------#
ans = Solution()
print(ans.almostIncreasingSequence([1, 3, 2, 1]))  # Output: False
print(ans.almostIncreasingSequence([1, 3, 2]))     # Output: True
print(ans.almostIncreasingSequence([1, 2, 3, 4]))  # Output: True
print(ans.almostIncreasingSequence([10, 1, 2, 3])) # Output: True
