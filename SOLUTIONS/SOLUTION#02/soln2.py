def check_hands(LH,RH,word):
	check = False
	lh_count,rh_count = 0,0
	for alpha in word:
		if alpha in LH:
			lh_count+=1
		if alpha in RH:
			rh_count+=1

	if len(word) == lh_count:
		return 'true'
	elif len(word) == rh_count:
		return 'true'
	else:
		return 'false'
		

if __name__ == '__main__':
	LH = ['q','w','e','r','t','a','s','d','f','g','z','x','c','v','b']
	RH = ['y','u','i','o','p','h','j','k','l','n','m']
	for word in ['starwars','lampung','secret','ilmu','pony']:
		print(check_hands(LH,RH,word))

