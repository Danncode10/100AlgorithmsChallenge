class Solution:
    def addBorder(self, picture):
        # Width of each line plus 2 for the '*' border
        border_length = len(picture[0]) + 2
        border = '*' * border_length

        # Add border to the top and bottom, and '*' to both sides of each line
        framed_picture = [border]
        for line in picture:
            framed_picture.append('*' + line + '*')
        framed_picture.append(border)

        return framed_picture


# ------ TEST ------#
ans = Solution()
picture = ["abc", "ded"]
print(ans.addBorder(picture))
