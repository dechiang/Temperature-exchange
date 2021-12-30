# 攝氏Ｃ轉換成華氏Ｆ程式
# 讓使用者輸入（攝氏溫度）轉換成華氏
# C = (F-32)*5/9

tempc = input('請輸入華氏溫度Ｃ： ')
tempc = int(tempc)
tempf = tempc * (9/5) + 32
print('華氏溫度為：', tempf)

