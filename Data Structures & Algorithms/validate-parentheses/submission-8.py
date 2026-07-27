class Solution:
    def isValid(self, s: str) -> bool:
        para = {")":"(",
        "}":"{",
        "]":"["}

        stack = []
        for c in s:
            if c in para.values():
                stack.append(c)
            else:
                if stack and stack[-1] == para[c]:
                    stack.pop()
                else:
                    return False
        return True if not stack else False