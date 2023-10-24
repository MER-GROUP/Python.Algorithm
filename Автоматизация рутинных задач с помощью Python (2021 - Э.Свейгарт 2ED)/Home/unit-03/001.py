def collatz(n: int) -> int:
    if n % 2:
        return 3 * n + 1
    return n // 2

if __name__ == '__main__':
    while True:
        try:
            n = collatz(int(input()))
            break
        except ValueError:
            print('Enter the integer number !')

    while True:
        print(n)
        if 1 == n:
            break
        n = collatz(n)