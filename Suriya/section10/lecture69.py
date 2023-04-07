# Dictionary

dict1 = {'Name': 'James', 'Age': 33}
print(dict1['Name'])

dict1['Lastname'] = 'Kotlin'

print(dict1['Name'], dict1['Lastname'])
dict1.clear()
print(dict1)

dict1['Name'] = 'Anna'
print(dict1)

dict1s = [{'Name': 'James', 'Lastname': 'Kotlin', 'Age': 33}, {'Name': 'John', 'Lastname': 'Tiny', 'Age': 30}]
print(dict1s[1]['Name'])
