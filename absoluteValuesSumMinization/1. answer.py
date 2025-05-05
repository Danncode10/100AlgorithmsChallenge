
class Solution:
    def absoluteValuesSumMinimization(self, a):
        n = len(a)
        index = ( n // 2 )

        if n % 2 == 0: # If length is even
            index -= 1

        return a[index]


# ------ TEST ------#
ans = Solution()
a = [2, 4, 7, 6, 6, 8]
print(ans.absoluteValuesSumMinimization(a))

