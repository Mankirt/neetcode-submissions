class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if num1=='0' or num2=='0':
            return '0'
        d = {"1":1,"2":2, "3":3,"4":4,"5":5,"6":6,"7":7,"8":8,"9":9,"0":0}
        d2 = {1:'1',2:'2', 3:'3',4:'4',5:'5',6:'6',7:'7',8:'8',9:'9',0:'0'}

        num1_int = 0
        for ch in num1:
            num1_int = num1_int*10 + d[ch]
        
        num2_int = 0
        for ch in num2:
            num2_int = num2_int*10 + d[ch]
        
        num1_int *= num2_int
        ans = []
        while num1_int>0:
                ans.append(d2[num1_int%10])
                num1_int= num1_int//10
        return "".join(ans[::-1])