held_val = 0
sum = 0
i = 1
j = 1
while i < 4000000:
    if i % 2 == 0: sum += i
    held_val = i
    i += j
    j = held_val
print(sum)