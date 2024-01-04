score = input("請輸入年齡:")
if(int(score) < 6):
    print("可看普遍級")
elif(int(score) < 12):
    print("可看普遍級及保護級")
elif(int(score) < 18):
    print("可看限制級以外的所有影片")
elif(int(score) >= 18):
    print("您已成年，可看所有影片")