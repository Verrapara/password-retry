# 密碼重式程式
# 先在程式碼中，設定好密碼 password = ‘a123456’
# 讓使用者『最多只能輸入三次密碼』
# 不對的話就印出”密碼錯誤！還有＿次機會“
# 對的話就列印出”登錄成功“

password = 'a123456' #先將密碼記起來
i = 3 #剩餘機會
while True:
	pwd = input('請輸入密碼: ') #不能存入password因為這樣重複存入，密碼縮寫是pwd
	if pwd == password: #因為已經在password存入a123456所以不用打密碼，直接打password
	   print('登錄成功')
	   break #如果密碼是對的，我們就逃出迴圈
	else:
		i = i - 1 #每輸入一次就又減一次
		print('密碼錯誤！還有',i,'次機會') #要將字串拆解，會變成字串，正數，字串
		if i == 0:
			break





