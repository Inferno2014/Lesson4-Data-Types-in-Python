username = input('Enter your username: ')
pswd = input('Enter Your Password: ')
if username=='admin':
    if pswd=='admin123':
        print('Login Successful')
if username!='admin':
    print('Incorrect username')
if pswd!='admin123':
    print('Incorrect password')
 
