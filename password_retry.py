password = 'a123456'
x = 3
while x > 0:
	x = x - 1
	pwd = input('請輸入密碼（最多輸入3次) :') #password answer
	if pwd == password:
		print('登入成功！')
		break
	else:
		print('密碼錯誤！')
		if x > 0:
			print('還有' , x , '次機會')
		else:
			print('已輸入錯誤超過三次！請十分鐘後再試')
