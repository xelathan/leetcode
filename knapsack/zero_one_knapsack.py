import typing

def debug_print(dp: list[list[int]]):
    output = ""
    for i in range(len(dp)):
        for j in range(len(dp[i])):
             output += str(dp[i][j]) + " "
        output += '\n'
    print(output)
            


def main() -> int:
    values = [1, 2, 5, 6]
    weights = [2, 3, 4, 5]
    c = 8
    n = len(values)


    dp = [[0 for _ in range(c + 1)] for _ in range(n + 1)]

    for i in range(1, n + 1):
        for j in range(1, c + 1):
            if weights[i - 1] <= j:
                    dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - weights[i - 1]] + values[i - 1])
            else:
                dp[i][j] = dp[i - 1][j]

    debug_print(dp)
    return 0



if __name__ == "__main__":
    main()
    