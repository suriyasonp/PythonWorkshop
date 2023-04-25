import csv

def readCSV():
    with open('employee_birthday.txt') as csv_file:
        '''เปิดไฟล์ employee_birthday.txt โดยใส่ลงไปในตัวแปร csv_file'''
        csv_reader = csv.reader(csv_file, delimiter=',')
        '''สร้างตัวแปร  csv_reader สำหรับใช้อ่านไฟล์ CSV ทีละตัว csv.reader()คือฟังก์ชั่นสำหรับอ่านไฟล์ , delimiter=',' => โดยแยกข้อมูลด้วยเครื่องหมาย ,'''
        line_count = 0
        for row in csv_reader:
            if line_count == 0:
                print(f'Column names are {", ".join(row)}')
                line_count += 1
            else:
                print(f'\t{row[0]} works in the {row[1]} department, and was born in {row[2]}.')
                line_count += 1
        print(f'Processed {line_count} lines.')

        '''Notes: การใช้งาน CSV จะใช้เครื่องหมาย , และการเว้นบรรทัดในการแบ่งข้อมูล ข้อควรระวังสำหรับการใช้งานคือการใช้ , '''
def writeCSV():
    with open('employee_file.csv', mode='w') as employee_file:
        employee_writer = csv.writer(employee_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        employee_writer.writerow(['Jutamanee T', 'IT', 'March'])
        employee_writer.writerow(['Erica Meyers', 'IT', 'March'])
        employee_writer.writerow(['Cat Dog', 'IT', 'March'])

writeCSV()