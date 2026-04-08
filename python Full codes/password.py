import getpass

user = input('User: ')
password = getpass.getpass('Password: ')

password_length = len(password)
password_hide = ('*' * password_length)

print(f'{user}, your password {password_hide} is {password_length} digits long')

# password = ''
#
# while True:
#     password = input('Enter your password: ')
#
#     if len(password) < 4:
#         print('Password too short')
#
#         continue
#
#     else:
#         print(f'You entered {password}')
#         break
#
# print(password)

