for casenum in range(int(input())):
    num = 0
    a, b = map(int, input().split(' '))
    for i in range(a, b + 1):
        prod = 1
        for x in str(i):
            prod *= int(x)
        num += True if prod % sum([int(x) for x in str(i)]) == 0 else False
    print('Case #' + str(casenum + 1) + ': ' + str(num))
