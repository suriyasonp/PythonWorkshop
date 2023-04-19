x = "hello"
assert x == "goodbye" , "x should be 'hello'"
'''assert  ทำงานคล้ายๆกับ if จะคอยตรวจเช็คเงื่อนไข ถ้าเงื่อนไขเป็นเท็จ ข้อความด้านหลัง x should be 'hello จะแสดง'''

for i in range(10):
    print(i)
    assert i < 5,"Error"