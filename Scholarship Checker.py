marks = int(input('Please enter your marks: '))
income = int(input('Please enter your parents annual income: '))
if marks>=90:
    if income<300000:
        print('You are eligible for a scholarship')
elif income>300000:
    print('You are eligible for a merit certificate')
elif marks>=75:
    if income<300000:
           print('You are eligible for a partial scholarship')
elif income>300000:
        print('You are not eligible for a scholarship')
if marks<75 and income<1000000000000000000:
     print('You are not eligible for anything')