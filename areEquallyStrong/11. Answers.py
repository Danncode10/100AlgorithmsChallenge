class Solution:
    def areEquallyStrong(self, yourLeft, yourRight, friendsLeft, friendsRight):
        # Check if the strongest arm of both is equal and the weakest arm is also equal
        return (max(yourLeft, yourRight) == max(friendsLeft, friendsRight)) and (min(yourLeft, yourRight) == min(friendsLeft, friendsRight))


# ------ TEST ------#
ans = Solution()
print(ans.areEquallyStrong(10, 15, 15, 10))  # Output: True
print(ans.areEquallyStrong(15, 10, 15, 10))  # Output: True
print(ans.areEquallyStrong(15, 10, 15, 9))   # Output: False
