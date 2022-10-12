def factorial(n, memo = {}):
    if n in memo:
        return memo[n]
    if n <= 2:
        return 1

    memo[n] = factorial(n-1, memo) + factorial(n-2, memo)
    return memo[n]


if __name__ == '__main__':
    print(factorial(6))