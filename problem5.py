i = 40
j = 20
while True:
    if i % j == 0 and j > 1: j -= 1
    elif j == 1:
        print(i)
        break
    else:
        i += 20
        j = 20


