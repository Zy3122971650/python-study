import time
from datetime import datetime
day1=0
day2=0
day3=0
day_last=0
while True:
    #获取&计算日期
    print(datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
    time_list_last=datetime.now().strftime('%Y %m %d %H:%M:%S').split()
    

    #数据部分
    name = input ("查询谁的信息：")
    name_find=[None]*100
    name_base=[None]*100
    name_find[0]='称呼1'
    name_base[0]=称呼1=["姓名：XX","出身年月：\n阳历年：X.X.X\n农历年：X.X.X"]
    name_find[1]="称呼2"
    name_base[1]=称呼2=["姓名：XX","出身年月：\n阳历年：X.X.X\n农历年：X.X.X"]
    name_find[2]='TEST'
    name_base[2]=TEST=["姓名：TEST","出身年月：\n阳历年：1972.4.7\n农历年：1971.12.17"]
    name_find[3]='称呼3'
    name_base[3]=称呼3=["姓名：XX","出身年月：\n阳历年：X.X.X\n农历年：X.X.X"]

    number = name_find.index(name)

      #获取出生年份信息
    birthDay_1=name_base[number][1]
    birthDay_2=birthDay_1.split("\n")
    
    birthDay_G=birthDay_2[1].split("：")
    birthDay_N=birthDay_2[2].split("：")

    birthDay_N_last=str(birthDay_N[1]).split(".")
    birthDay_G_last=str(birthDay_G[1]).split(".")  #0年 1月 2日

    _31day=[1,3,5,7,8,10,12]
    _28day=[2]
    _30day=[4,6,9,11]
    #天数函数
    def counter ():
        day2=0
        for i in size_month:
            month=(int(time_list_last[1]))+1+i
            if month in _31day:
                day2=day2+31
            elif  month in _30day :
                day2=day2+30
            elif  month in _28day :
                day2=day2+28
                pass
            pass
        return(day2)

    if (int(time_list_last[0]))>(int(birthDay_G_last[0])):
        if (int(time_list_last[1]))<(int(birthDay_G_last[1])):
            size=(int(birthDay_G_last[1]))-(int(time_list_last[1]))-1#生日还没过
            size_month=range(size)
            if (int(time_list_last[1]))==2:
                day1=28-(int(time_list_last[2]))
                day2=counter()
            elif ((int(time_list_last[1])) in _30day)==True:
                day1=30-(int(time_list_last[2]))
                day2=counter()
            elif ((int(time_list_last[1])) in _31day)==True:
                day1=31-(int(time_list_last[2]))
                day2=counter()  
                pass
            
            #------------------------------------------------------
        elif (int(time_list_last[1]))>(int(birthDay_G_last[1])):
            size=12-(int(birthDay_G_last[1]))#到今年结束的步长
            size_month=range(size)
            if (int(time_list_last[1]))==2:
                day1=28-(int(time_list_last[2]))
                day2=counter()
            elif ((int(time_list_last[1])) in _30day)==True:
                day1=30-(int(time_list_last[2]))
                day2=counter()
            elif ((int(time_list_last[1])) in _31day)==True:
                day1=31-(int(time_list_last[2]))
                day2=counter()  
                pass
            day3=day2
            #----------------------------------------------------
            size=(int(birthDay_G_last[1]))-1 #第二年到生日
            size_month=range(size)
            if (int(time_list_last[1]))==2:
                day1=28-(int(time_list_last[2]))
                day2=counter()
            elif ((int(time_list_last[1])) in _30day)==True:
                day1=30-(int(time_list_last[2]))
                day2=counter()
            elif ((int(time_list_last[1])) in _31day)==True:
                day1=31-(int(time_list_last[2]))
                day2=counter()  
                pass
            day2=day2+(int(birthDay_G_last[2]))
            day_last=day1+day2+day3
            #-----------------------------------------------------
        elif (int(time_list_last[1]))==(int(birthDay_G_last[1])):
            if ((int(time_list_last[2]))-(int(birthDay_G_last[2])))>0:
                size=12-(int(birthDay_G_last[1]))#到今年结束的步长
                size_month=range(size)
                if (int(time_list_last[1]))==2:
                    day1=28-(int(time_list_last[2]))
                    day2=counter()
                elif ((int(time_list_last[1])) in _30day)==True:
                    day1=30-(int(time_list_last[2]))
                    day2=counter()
                elif ((int(time_list_last[1])) in _31day)==True:
                    day1=31-(int(time_list_last[2]))
                    day2=counter()  
                    pass
                day3=day2
                #----------------------------------------------------
                size=(int(birthDay_G_last[1]))-1 #第二年到生日
                size_month=range(size)
                if (int(time_list_last[1]))==2:
                    day1=28-(int(time_list_last[2]))
                    day2=counter()
                elif ((int(time_list_last[1])) in _30day)==True:
                    day1=30-(int(time_list_last[2]))
                    day2=counter()
                elif ((int(time_list_last[1])) in _31day)==True:
                    day1=31-(int(time_list_last[2]))
                    day2=counter()  
                    pass
                day2=day2+(int(birthDay_G_last[2]))
                day_last=day1+day2+day3
            elif ((int(time_list_last[2]))-(int(birthDay_G_last[2])))<0:
                day_last=((int(time_list_last[1]))-(int(birthDay_G_last[1])))
                pass
            elif ((int(time_list_last[2]))-(int(birthDay_G_last[2])))==0:
                day_last=0
                pass
            pass
        pass
    elif (int(time_list_last[0]))<(int(birthDay_G_last[0])):
        print("怕不是假人")
        print("请检查数据库数据")
    
    for i in name_base[number]:
        print(i)
        pass
    print("距离下次生日还有："+str(day_last)+"天")
    if day_last==0:
        print("他今天是寿星哦!!")
    time.sleep(500/1000)
    pass

#阴历生日还无法计算

