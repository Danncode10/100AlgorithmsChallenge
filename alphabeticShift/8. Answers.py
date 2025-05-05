class Solution:
    def alphabeticShift(self, inputString):
        result = ''
        for char in inputString:
            # Shift 'z' to 'a', otherwise shift to next character
            if char == 'z':
                result += 'a'
            else:
                result += chr(ord(char) + 1)
        return result


# ------ TEST ------#
ans = Solution()
print(ans.alphabeticShift("crazy"))
