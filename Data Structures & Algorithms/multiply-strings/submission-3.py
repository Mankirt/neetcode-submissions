class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if "0" in [num1, num2]:
            return "0"
        
        out = [0] * (len(num1)+ len(num2))

        num1 = num1[::-1]
        num2 = num2[::-1]

        for i in range(len(num1)):
            for j in range(len(num2)):
                digit = int(num1[i]) * int(num2[j])

                out[i+j] += digit
                out[i+j+1] += (out[i+j]//10)
                out[i+j] = out[i+j] % 10
        
        out = out[::-1]
        beg =0
        while out[beg] == 0:
            beg += 1
        
        return "".join(map(str, out[beg:]))