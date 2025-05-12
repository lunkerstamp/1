a1,a2 = 1,1
n = int(input("请输入要求和的项数n："))
sum_value=0
a,b = a1,a2
for i in range(1,n+1):
    sum_value += b
    if i >= 2:
        b += a
        a = b - a
print(f"斐波那契数列前n项和为: {sum_value}")

a1,a2 = 1,1
n = int(input("请输入要求和的项数n："))
sum_value=0
a,b = a1,a2
i = 1
while i<=n:
    sum_value += a
    i += 1
    a,b = b,a+b
print(f"斐波那契数列前n项和为: {sum_value}")

import math
class CalculateSum:
    def __init__(self):
        self.n = int(input("请输入要求和的项数n："))
    def sum_Fibonacci(self):
        sum_value = 0
        b = math.sqrt(5)
        for i in range(self.n+1):
           c = ((1 + b)/2)**i - ((1 - b)/2)**i
           ai = c/b
           sum_value += int(ai)
        return sum_value

obj = CalculateSum()
result = obj.sum_Fibonacci()
print(f"斐波那契数列前n项和为: {result}")

a1,a2 = 1,1
n = int(input("请输入要求和的项数n："))
sum_value=0
list_Fibonacci = [1,1]
a,b = a1,a2
if n >= 3:
    for i in range(3,n+1):
        list_Fibonacci.append(list_Fibonacci[-1]+list_Fibonacci[-2])

sum_value = sum(list_Fibonacci)
print(f"斐波那契数列前n项和为: {sum_value}")