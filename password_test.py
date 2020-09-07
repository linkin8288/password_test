# 密碼重試程式
# 先在程式中，設定好密碼password = 'a123456'
# 讓使用者['最多輸入三次密碼]
# 不對的話，就印出'密碼錯誤'，還有__次機會'
# 對的話，就印出'登入成功'
# while True 是無限迴圈


password = 'a123456'
i = 3 # 剩餘機會
while i > 0: # 當i > 0就停止迴圈
	pwd = input('請輸入密碼') # 不能存入password不然會覆蓋掉
	if pwd == password:
		print('登入成功')
		break # 逃出迴圈
	else:
		i = i - 1
		print('密碼錯誤!')	
		if i > 0:
			print(' 還有', i, '次機會')
		else:
			print('沒機會嘗試了!，要鎖帳號了拉')