n = int(input())

factor1 = n % 2 == 0
factor2 = n > 4 and n <= 12

print(
    int(factor1 and factor2),
    int(factor1 or factor2),
    int(factor1 != factor2),
    int((not factor1) and (not factor2))
    # also known as int(not(factor1 or factor2))
)