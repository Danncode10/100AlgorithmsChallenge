class Solution:
    def areSimilar(self, a, b):
        # If arrays are already equal, they are similar
        if a == b:
            return True

        # Find the positions where the arrays differ
        diff = []
        for i in range(len(a)):
            if a[i] != b[i]:
                diff.append(i)

        # If there are exactly two differences, check if swapping makes them equal
        if len(diff) == 2:
            i, j = diff
            return a[i] == b[j] and a[j] == b[i]

        return False


# ------ TEST ------#
ans = Solution()
print(ans.areSimilar([1, 2, 3], [1, 2, 3]))  # Output: True
print(ans.areSimilar([1, 2, 3], [2, 1, 3]))  # Output: True
print(ans.areSimilar([1, 2, 2], [2, 1, 1]))  # Output: False

