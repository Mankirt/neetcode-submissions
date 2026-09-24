class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        dic = {"1" : 1, "2" : 2, "3" : 3, "4" : 4, "5" : 5, "6": 6, "7" : 7, "8" : 8, "9" : 9, '0' : 0}
        rev_dic = {1 : '1', 2 : '2', 3:'3', 4:'4', 5:'5', 6:'6', 7:'7', 8:'8',9:'9',0:'0'}

        n1 = n2 = 0

        for ch in num1:
            n1 = n1 * 10 + dic[ch]
        
        for ch in num2:
            n2 = n2 * 10 + dic[ch]

        ans = n1 * n2
        res = ''
        if ans == 0: return '0'
        while ans > 0:
            res += rev_dic[ans%10]
            ans //= 10
        return res[::-1]