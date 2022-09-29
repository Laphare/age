ask = input('请问您是否开过车')
if ask != 'yes' and ask != 'no' :
	print ('please input yes or no')
	raise SystemExit 
age = input('请问您的年龄')
age = int (age)
if  ask == 'yes':
	if age >= 18:
		print ('Pass')
	else:
		print ('How?')
elif ask == 'no':
	if age >= 18:
		print ('please join the dring test')
	else:
		print("come again when you 18")