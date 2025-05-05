class Solution:
    def arrayChange(self, inputArray):
        moves = 0
        # Iterate through the array starting from the second element
        for i in range(1, len(inputArray)):
            if inputArray[i] <= inputArray[i - 1]:
                # Increase the current element to make it strictly greater than the previous one
                moves += (inputArray[i - 1] - inputArray[i] + 1)
                # Update the current element to be one greater than the previous element
                inputArray[i] = inputArray[i - 1] + 1
        return moves


# ------ TEST ------#
ans = Solution()
inputArray = [1, 1, 1]
print(ans.arrayChange(inputArray))  # Output: 3
