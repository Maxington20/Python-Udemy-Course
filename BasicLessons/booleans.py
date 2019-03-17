username = 'admin'
password = 'admin123'

if username == 'admin' and password == 'admin123': # Both conditions must be true for the code to run
    print('Valid User')
else:
    print('invalid user')

if username == 'admin' or password == 'admin123': # Only one of the conditions must be true
    print('sort of valid user')