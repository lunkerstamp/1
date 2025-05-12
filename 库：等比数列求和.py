a1 = float(input("请输入等比数列的首项a："))
q = float(input("请输入等比数列的公比d："))
n = int(input("请输入要求和的项数n："))
sum_value=0
a = a1
for i in range(1,n+1):
    sum_value += a
    a *= q
print(f"等比数列前n项和为: {sum_value}")

a1 = float(input("请输入等比数列的首项a："))
q = float(input("请输入等比数列的公比q："))
n = int(input("请输入要求和的项数n："))
sum_value=0
a = a1
i = 1
while i<=n:
    sum_value += a
    a *= q
    i += 1
print(f"等比数列前n项和为: {sum_value}")

class CalculateSum:
    def __init__(self):
        self.a1 = float(input("请输入等比数列的首项a："))
        self.q = float(input("请输入等比数列的公比q："))
        self.n = int(input("请输入要求和的项数n："))
    def sum_dengbi(self):
        an = self.a1 *self.q* (self.n - 1)
        if self.q != 1:
            sum_value = (self.a1 - an*self.n) / (1 - self.q)
        else:
            sum_value = 1
        return sum_value

obj = CalculateSum()
result = obj.sum_dengbi()
print(f"等比数列前n项和为: {result}")

a1 = float(input("请输入等比数列的首项a："))
q = float(input("请输入等比数列的公比q："))
n = int(input("请输入要求和的项数n："))
list_dengbi = [a1*q**i for i in range(n)]
sum_value = sum(list_dengbi)
print(f"等比数列前n项和为: {sum_value}")