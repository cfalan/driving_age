


# this is for diving age


driving = input('Did you drive before?  ')

if driving != 'yes' and driving != 'no':

	print ('please input yes or no')
	raise SystemExit

age = input('How old are you?  ')
age = int(age)


if driving == 'yes':
	if age < 18:
		print ('you are under 18')
	else:
		print ('cool man, enjoy your drive')
elif driving == 'no':
	if age < 18:
		print ('good boy, you can get driving license soon.')
	else:
		print ('are you afraid of driving?')

#test
# test 3
#python3 driving_age.py
#cd /users/alanchan/documents/coding
#cd /users/alanchan/desktop