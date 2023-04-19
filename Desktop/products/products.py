# 讀取檔案
products = []
with open('products.csv', 'r', encoding='utf-8') as f:
	for line in f:
		if '商品,價格' in line:
			continue #繼續，跳到下一run
		name, price = line.strip().split(',') #去掉換行符號以及分割，切割完之後直接丟進去變數，切幾份就要幾個變數
		products.append([name, price]) #小清單裝進大清單
print(products)		

# 讓使用者輸入
while True: #用while通常是在不知道執行次數的條件下使用
	name = input('請輸入商品名稱： ')
	if name == 'q': #quit
		break
	price = input('請輸入價格： ')	
	price = int(price) #型別轉換成整數
	products.append([name, price])
print(products)

#印出所有購買紀錄
for p in products: 
	print(p[0], '的價格是', p[1])

#寫入檔案
with open ('products.csv', 'w', encoding='utf-8') as f: #編碼調整
	f.write('商品,價格\n') #增加欄位
	for p in products:
		f.write(p[0] + ',' + str(p[1]) + '\n') #將price變為字串