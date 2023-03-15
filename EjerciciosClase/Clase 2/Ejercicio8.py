def funcionPrimos(start, end, step):
    primos = []
    for num in range(start, end+1, step):
        if num > 1:
            for i in range(2, int(num**(1/2))+1):
                if (num % i) == 0:
                    break
            else:
                primos.append(num)
    return primos
primos = funcionPrimos(0, 10, 1)
print(f"Los números primos son: {primos}")