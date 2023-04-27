myTuple = ('AA', 'BB', 'CC', 'YY')
print("myTuple", myTuple)

myTuple2 = ('XX', 'XE', 'ZZ')
print("myTuple2", myTuple2)

myTuple3 = myTuple + myTuple2
print("myTuple3 all members", myTuple3)
print("myTuple3 3 members", myTuple3[:3])
print('AA is in Tuple? ', 'AA' in myTuple3)

for item in myTuple3:
    print(item)