LEFT = '({['
RIGHT = ')}]'

class Solution:
    def isValid(self, s: str) -> bool:
        curr = []
        for char in s:
            if char in LEFT:
                curr.append(char)
            else:
                if not curr or curr[-1] != LEFT[RIGHT.index(char)]:
                    return False
                curr.pop()
        return not curr
