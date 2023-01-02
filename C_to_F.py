#摄氏℃转换成华氏℉ 程式
#让使用者输入摄氏温度，然后打印出华氏温度

celsius = input('请输入摄氏度℃: ')
celsius = float(celsius) #根据实际使用情况，最后使用float浮点数。使用者可能会输入带小数点的温度数字
fahrenheit = celsius * (9 / 5) + 32 # 运算符号要有空格，保持好格式
print ('华氏温度为', fahrenheit ,'℉') #容易少逗号。