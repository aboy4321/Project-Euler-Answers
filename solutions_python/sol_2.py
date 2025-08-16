def main():
    sum = 0
    start = 1
    num = 0
    while num < 4000000:
        num = start + num
        sum += num
    return sum

print(main())

def fib():
    summ = 0
    start = 1
    num = 0
    while num < 4000000:
        if num % 2 == 0:
            num = num + start

