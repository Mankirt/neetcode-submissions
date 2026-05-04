class Solution:
    def addBinary(self, a: str, b: str) -> str:
        carry = '0'
        i = 0
        l = []
        a = a[::-1]
        b = b[::-1]
        while i < len(a) or i < len(b):
            x1 = a[i] if i < len(a) else '0'
            y2 = b[i] if i < len(b) else '0'

            if x1 == '0' and y2 == '0':
                if carry == '1':
                    l.append('1')
                    carry = '0'
                else:
                    l.append('0')
            elif x1 == '1' and y2 == '1':
                if carry == '1':
                    l.append("1")
                    #carry = '1'  # ✅ fix: must keep carry = '1'
                else:
                    l.append('0')
                    carry = '1'
            else:
                if carry == '1':
                    l.append('0')
                    #carry = '1'  # ✅ fix: must keep carry = '1'
                else:
                    l.append('1')
                    carry = '0'
            i += 1
        if carry == '1':
            l.append("1")
        return "".join(l[::-1])
