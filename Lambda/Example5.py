def myfunc(n):
  return lambda a : a * n

mydoubler = myfunc(4)

print(mydoubler(12))