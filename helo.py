
print('ver 0.1')
print('\n 1. hello\n 2. world\n 3. 1+2\n 4. up\n')

a1 = 'hello '
a2 = 'world'
a3 = a1 + a2

def up():
	exec('git pull https://github.com/L0L225/hello.git')



a = int(input('> '))
if a == 1:
	print(a1)
elif a == 2:
	print(a2)
elif a == 3:
	print(a3)
elif a == 4:
	up()
else:
	print('err')

