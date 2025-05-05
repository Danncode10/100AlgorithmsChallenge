class Solution:
    def arrayConversion(self, inputArray):
        iteration = 1
        while len(inputArray) > 1:
            temp = []
            for i in range(0, len(inputArray), 2):
                if iteration % 2 == 1:  # Odd iteration: Sum
                    temp.append(inputArray[i] + inputArray[i + 1])
                else:  # Even iteration: Product
                    temp.append(inputArray[i] * inputArray[i + 1])
            inputArray = temp
            iteration += 1
        return inputArray[0]


# ------ TEST ------#
ans = Solution()
inputArray = [1, 2, 3, 4, 5, 6, 7, 8]
print(ans.arrayConversion(inputArray))  # Output: 186

