class Solution(object):
    def minAddToMakeValid(self, s):
  
        open=0
        close=0

        for i in s:
           if i == '(':
              close += 1
           else:
               if close > 0:
                   close -= 1
               else:
                    open += 1
        return(open+close)  
