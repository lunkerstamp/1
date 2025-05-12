class CalculateSum:
    def __init__(self):
        self.a1 = float(input("请输入等差数列的首项a："))
        self.d = float(input("请输入等差数列的公差d："))
        self.n = int(input("请输入要求和的项数n："))
    def sum_dengcha(self):
        an = self.a1 + (self.n - 1) * self.d
        sum_value = self.n * (self.a1 + an) / 2
        return sum_value

obj = CalculateSum()
result = obj.sum_dengcha()
print(f"等差数列前n项和为: {result}")

a1 = float(input("请输入等差数列的首项a："))
d = float(input("请输入等差数列的公差d："))
n = int(input("请输入要求和的项数n："))
sum_value=0
for i in range(1,n+1):
    sum_value = sum_value + a1 + d*(i-1)
print(f"等差数列前n项和为: {sum_value}")

a1 = float(input("请输入等差数列的首项a："))
d = float(input("请输入等差数列的公差d："))
n = int(input("请输入要求和的项数n："))
sum_value=0
i=1
while i<=n:
    sum_value = sum_value + a1 + d*(i-1)
    i+=1
print(f"等差数列前n项和为: {sum_value}")

a1 = float(input("请输入等差数列的首项a："))
d = float(input("请输入等差数列的公差d："))
n = int(input("请输入要求和的项数n："))
list_dengcha = [a1 + i * d for i in range(n)]
sum_value = sum(list_dengcha)
print(f"等差数列前n项和为: {sum_value}")