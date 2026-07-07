class Solution:
    def evalRPN(self, tokens: List[str]) -> int:

        if not tokens:
            return 0

        n = len(tokens)

        opr = {'+','-','*','/'}
        rpn = []
        for i in range(0, n):

            if tokens[i] in opr:
                b = rpn.pop()
                a = rpn.pop()
                rpn.append(str(int(eval(a+tokens[i]+b))))
            else:
                rpn.append(tokens[i])

            print(rpn)

        return int(rpn[0])
        