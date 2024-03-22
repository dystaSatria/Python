class Solution:
    def addBinary(self, a: str, b: str) -> str:
        s = []  
        var = 0  
        i = len(a) -1 
        j = len(b)  - 1

        while i >= 0 or j >= 0 or var:
            if i >= 0:
                var += int(a[i])  
                i -= 1

            if j >= 0:
                var += int(b[j])  
                j -= 1  

            s.append(str(var % 2)) 
            var //= 2  
        return ''.join(reversed(s))  

def main():
    
    a = input("Enter the first binary number: ")
    b = input("Enter the second binary number: ")


    solution = Solution()
    result = solution.addBinary(a, b)

    
    print("The binary sum is:", result)

if __name__ == "__main__":
    main()
