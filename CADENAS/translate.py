str='aeiou'
b={}
for carazter in range(97,124):
	if carazter in str :
		b[carazter]='X'

	print (str.translate(b))