deposit = int(input("請輸入手機金額:"))
spend = deposit
deposit = int(input("請輸入本金金額:"))
deposit -= spend
print("剩餘款為:" + str(deposit))