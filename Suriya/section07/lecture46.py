start = 2
result = 0
for i in range(5):
    for j in range(12):
        result = start * (j + 1)
        print(str(start) + " x " + str(j + 1) + " = " + str(result))
        if (j+1) % 12 == 0:
            print("-----------------")
    start += 1