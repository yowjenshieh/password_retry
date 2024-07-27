password = 'a123456'
x = 3
while True:
	pwd = input('請輸入密碼（最多輸入3次) :') #password answer
	if pwd == password:
		print('登入成功！')
		break
	else:
		x = x - 1
		print('密碼錯誤！還有' , x , '次機會')
		if x == 0:
			break
