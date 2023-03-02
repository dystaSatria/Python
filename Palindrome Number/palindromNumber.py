

class Solution(object):
    def isPalindrom(self, x):
        if x < 0 or (x % 10 and x > 0):
            return False
        
        lastNumber = 0 
