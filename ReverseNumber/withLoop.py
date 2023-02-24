while True : 
    Num = int(input("\ninput the number\n"))
    reverseNum = 0

    while Num != 0:
        operation = Num % 10
        reverseNum = (reverseNum * 10) + operation
        Num //= 10
   
    print (str(reverseNum))
