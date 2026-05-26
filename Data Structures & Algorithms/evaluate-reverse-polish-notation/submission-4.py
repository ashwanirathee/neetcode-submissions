class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        our_stack = []
        for token in tokens:
            try:
                number = int(token)
                our_stack.append(number)
            except:
                b = our_stack.pop()
                a =  our_stack.pop()
                if token == "+":
                    result = a + b
                    our_stack.append(result)
                elif token == "-":
                    result = a - b
                    our_stack.append(result)
                elif token == "*":
                    result = a * b
                    our_stack.append(result)
                elif token == "/":
                    result = int(a / b)
                    our_stack.append(result)
                else:
                    print("unknown case")
        return our_stack[-1]