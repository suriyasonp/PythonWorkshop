tupleExample =('Prame','Guide','Yeen')
print(tupleExample)

'''Ex1'''
tupleExample2 =('Bank','Kay')
print(tupleExample2)

'''Ex2'''
tupleExample3 = tupleExample+tupleExample2
print(tupleExample3)
print(tupleExample3[1])
print(tupleExample3[:2])

'''Ex3'''
tupleExample4 = tupleExample+tupleExample2*2
print(tupleExample4)

'''Ex4'''
print('Yeen' in tupleExample3)
'''เป็นการหา  Yeen ใน tupleExample3 ผลลัพธ์จะออกมาเป็น true or false'''

'''Ex5'''
for i in tupleExample3:
    print(i)
