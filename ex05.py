y = 0
x = float(input("Ditigite seu salário: "))
if x < 500:
    y = x * 1.15
    print("o Reajuste do salário é: ", y)
elif x <= 1000:
    y = x * 1.10
else:
    y = x * 1.05

print("O novo reajuste do salário é: ", y)