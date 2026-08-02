class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        bkts = {
            ")":"(",
            "]":"[",
            "}":"{"
        }

        for c in s:
            if c in bkts and stack:
                if stack.pop() != bkts[c]:
                    return False
            else:
                stack.append(c)

        return stack == []
