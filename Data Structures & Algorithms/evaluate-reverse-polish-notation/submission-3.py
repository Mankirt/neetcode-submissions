class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack_n=[]
        for token in tokens:
            if token == "*":
                stack_n.append(stack_n.pop() * stack_n.pop())
            elif token == "+":
                stack_n.append(stack_n.pop() + stack_n.pop())
            elif token == "/":
                d=stack_n.pop()
                stack_n.append(int(stack_n.pop() / d))
            elif token == "-":
                d=stack_n.pop()
                stack_n.append(stack_n.pop() - d)
            else:
                stack_n.append(int(token))
            print(stack_n)
        return stack_n[0]
            
