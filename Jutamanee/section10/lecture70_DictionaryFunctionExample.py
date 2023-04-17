words = {"Bird":"มันคือนก","Cat":"มันคือแมว","Dog":"มันคือหมา","book":"มันคือหนังสือ","Fan":"พัดลม"}
print(words)
print(words["Bird"])
words.copy()
print(words.items())
print(words.keys())
print(words.values())

for i in words.keys():
    print(i)

for j in words.values():
    print(j)
