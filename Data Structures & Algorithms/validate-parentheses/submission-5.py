class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        hp = {
            "(":")",
            "{":"}",
            "[":"]"
        }

        for char in s:
            if char in hp:
                stack.append(char)
            elif stack:
                if hp[stack[-1]] != char:
                    return False
                stack.pop()
            else:
                return False

        if stack:
            return False
        return True
        