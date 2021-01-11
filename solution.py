from collections import Counter
class Solution:
    def findSpecialInteger(self, arr) -> int:
        a=Counter(arr)
        b=sorted(a.items(),key=lambda x:x[1],reverse=True)
        for i in b:
            return(i[0])
s=Solution()
arr=[1,2,2,6,6,6,6,7,10]
print(s.findSpecialInteger(arr))          