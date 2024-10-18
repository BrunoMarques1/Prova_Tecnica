def pertence_fibonacci(n):
    fibonacci = [0,1]

    while True:
        if (fibonacci[-1] == n) or (fibonacci[0] == n):
            print(f'O número {n} está presente na sequência de fibonacci')
            print(fibonacci)
            break
        elif (fibonacci[-1] > n):
            print(f'O número não está presente na sequência de fibonacci')
            break
        else:
            soma = fibonacci[-1] + fibonacci[-2]
            fibonacci.append(soma)


pertence_fibonacci(34)