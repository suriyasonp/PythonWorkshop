tupleExample = ("Paradorn","Leon")
print(tupleExample)
tupleExample2 = ("Peter","Tony")
tupleExample3 = tupleExample+tupleExample2
print(tupleExample3)
print(tupleExample3[:3])

print("Paradorn" and "Leon" in tupleExample3)

for i in tupleExample3:
    print(i)