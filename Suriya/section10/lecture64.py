myList = ['AA', 'BB', 'CC']
myList.append('DD')
print(myList)

myList.remove('BB')
print(myList)

myList.sort(reverse=True)
print(myList)

myList[1] = 'XX'
print(myList)

del myList[1]
print(myList)