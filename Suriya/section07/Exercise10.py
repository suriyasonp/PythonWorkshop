result = ""
start = int(input("Start:"))
step = int(input("Step:"))

for i in range(5):
    result += str(start + step * i + 1)
    print(start + step * i, end=" ")
print(result)
