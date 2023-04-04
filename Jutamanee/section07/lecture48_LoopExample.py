'''1
*
2
**
3
***
4
****
5
*****
'''

'''------------=1=--------------'''
'''number = int(input("Number :"))
text = ""
for x in range(number):
    text = text + "*"
print(text)'''
'''------------=2=--------------'''
'''number = int(input("Number :"))
print(number*"*")'''
'''------------=3=--------------'''
'''number = int(input("Number :"))
text=""
for x in range(number):
    text=""
    for y in range(x+1):
        text += "*"
    print(text)'''
'''------------=4=--------------'''
number = int(input("Number :"))
for x in range(number):
    print("*"*(x+1))