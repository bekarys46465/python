def divisible_by_3_and_4_generator(n):
    for i in range(n + 1):
        if i % 3 == 0 and i % 4 == 0:
            yield i

n = 20
for number in divisible_by_3_and_4_generator(n):
    print(number)
