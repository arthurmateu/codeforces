for _ in range(int(input())):
    a, b, x, y, n = (int(x) for x in input().split())

    reduce_a = min(n, a - x)
    reduce_b = min(n - reduce_a, b - y)
    product1 = (a - reduce_a) * (b - reduce_b)

    reduce_b = min(n, b - y)
    reduce_a = min(n - reduce_b, a - x)
    product2 = (a - reduce_a) * (b - reduce_b)

    print(min(product1, product2))
