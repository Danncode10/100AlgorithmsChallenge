class Solution:
    def arrayMaxConsecutiveSum(self, inputArray, k):
        # Calculate the sum of the first 'k' elements
        max_sum = sum(inputArray[:k])
        current_sum = max_sum

        # Slide the window across the array
        for i in range(k, len(inputArray)):
            current_sum += inputArray[i] - inputArray[i - k]  # Add the next element, subtract the leftmost element
            max_sum = max(max_sum, current_sum)  # Update the max sum if needed

        return max_sum


# ------ TEST ------#
ans = Solution()
inputArray = [2, 3, 5, 1, 6]
k = 2
print(ans.arrayMaxConsecutiveSum(inputArray, k))  # Output: 8
