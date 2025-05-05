class Solution:
    def adjacentElementsProduct(self, inputArray):
        max_product = inputArray[0] * inputArray[1]  # Initialize with first adjacent pair
        for i in range(1, len(inputArray) - 1):
            product = inputArray[i] * inputArray[i + 1]
            if product > max_product:
                max_product = product
        return max_product


# ------ TEST ------#
ans = Solution()
inputArray = [3, 6, -2, -5, 7, 3]
print(ans.adjacentElementsProduct(inputArray))  # Output: 21
