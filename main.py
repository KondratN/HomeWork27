def line_length(a, b):
    return ((a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2) ** 0.5


print(line_length((15, 7), (22, 11)), line_length((0, 0), (1, 1)))


def climbStairs(n):
    if n == 1:
        return 1
    if n == 2:
        return 2
    return climbStairs(n - 1) + climbStairs(n - 2)

print(climbStairs(8))
