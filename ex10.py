def fibonacci(n):
    fibonacci_sequence = [0, 1]
    for i in range(2, n):
        fibonacci_sequence.append(fibonacci_sequence[i-1] + fibonacci_sequence[i-2])
    return
    fibonacci_sequence[ :n]

n = int(input("Digite o número de termos da sequência de fibonacci: "))
print("Os", n, "primeiros números da sequência de Fibonacci são: ", fibonacci(n))