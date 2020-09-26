prod = 0
high_prod = 0
for i in range(100,1000):
    for j in range(100,1000):
        prod = i * j
        if prod > high_prod and str(prod) == str(prod)[::-1]: high_prod = prod
print(high_prod)