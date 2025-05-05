class Solution:
    def alternatingSums(self, a):
        team1_sum = 0
        team2_sum = 0
        for i in range(len(a)):
            if i % 2 == 0:  # Even index goes to team 1
                team1_sum += a[i]
            else:  # Odd index goes to team 2
                team2_sum += a[i]
        return [team1_sum, team2_sum]


# ------ TEST ------#
ans = Solution()
print(ans.alternatingSums([50, 60, 60, 45, 70]))  # Output: [180, 105]
print(ans.alternatingSums([45, 50]))              # Output: [45, 50]
print(ans.alternatingSums([100, 100, 100]))       # Output: [200, 100]
