class Solution:
    def addBinary(self, a: str, b: str) -> str:
        res = []
        carry = 0 

        a = a[::-1]
        b = b[::-1]

        for i in range(max(len(a),len(b))):

            digitA = int(a[i]) if i <len(a) else 0
            digitB = int(b[i]) if i <len(b) else 0
            total = digitA + digitB + carry

            res.append(str(total%2))
            carry = total // 2
        
        res = res[::-1]
        if carry:
            res = "".join(["1"]+res)
        else:
            res = "".join(res)
        return res