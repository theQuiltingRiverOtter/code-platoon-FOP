def hailstone(num: int) -> int:
    steps = 0
    while num != 1:
        steps += 1
        if num % 2 == 0:
            num /= 2
        else:
            num = num * 3 + 1
    return steps


answer = hailstone(3)
print(answer)
