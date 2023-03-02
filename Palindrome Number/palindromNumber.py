

class Solution(object):
    def isPalindrom(self, x):
        if x < 0 or (x % 10 and x != 0):
            return False
        
        numReversed = 0
        originalX = x
        
        #reverse number function
        while x > 0 :
            lastDigit = x % 10
            numReversed = numReversed * 10 + lastDigit
            x = x // 10
        
       # cause Palindrom we use above code
       return numReversed == originalX
            
        
