

class Solution(object):
    def isPalindrom(self, x):
        if x < 0 or (x % 10 and x != 0):
            return False
        
        numReversed = 0
        originalX = x
        
        while x > 0 :
            lastDigit = x % 10
            numReversed = numReversed * 10 + lastDigit
            
        
