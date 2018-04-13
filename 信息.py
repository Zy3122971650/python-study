import time
from datetime import datetime
while True:
    #获取&计算日期
    print(datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
    time_list_last=datetime.now().strftime('%Y %m %d %H:%M:%S').split()
    

    #数据部分
    name_find=["Unkonw"]*1000
    name_base=["Unkonw"]*1000
    Day_list=["Unkonw"]*1000
    Day_list1=["Unkonw"]*1000
    Day_list2=["Unkonw"]*1000

    name_find[0]='xx'
    name_base[0]=xx=["姓名：xx","出身年月：\n阳历年：1972.2.1\n农历年：1971.12.17"]
    name_find[1]="xxxxx"
    name_base[1]=xxxxx=["姓名：xxxxx","出身年月：\n阳历年：1976.1.31\n农历年：1976.12.13"]
    name_find[2]='TEST'
    name_base[2]=TEST=["姓名：TEST","出身年月：\n阳历年：1972.4.14\n农历年：1971.12.17"]
    name_find[4]='xxx'
    name_base[4]=xxx=["姓名：xxx","出身年月：\n阳历年：2002.2.25\n农历年：2002.02.14"]
    name_find[3]='xxxx'
    name_base[3]=xxxx=["姓名：xxxx","出身年月：\n阳历年：2001.6.22\n农历年：0.0.0.0"]

    y=name_find.index("Unkonw")
    name_find[y:]=[]
    name_base[y:]=[]

      #获取出生年份信息
   

    _31day=[1,3,5,7,8,10,12]
    _28day=[2]
    _30day=[4,6,9,11]
    def Days():
        day1=0
        day2=0
        day3=0
        day_last=0
        global _30day
        global _28day
        global _31day
        birthDay_1=name_base[number][1]
        birthDay_2=birthDay_1.split("\n")
        birthDay_G=birthDay_2[1].split("：")
        birthDay_N=birthDay_2[2].split("：")
        birthDay_N_last=str(birthDay_N[1]).split(".")
        birthDay_G_last=str(birthDay_G[1]).split(".")  #0年 1月 2日

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
                    if year%400 == 0 :
                        y2=day2+29
                    else :
                        day2=day2+28
                        pass
                    
               
                    pass

                pass
            
            return(day2)
    #生日时间计算
        if (int(birthDay_G_last[1]))==2 and (int(birthDay_G_last[2]))==29 :
            year = 0
            while year%400 != 0:
                year=year+1
                pass

            size_year = year - time_list_last[0] - 2
            size=12-(int(birthDay_G_last[1]))#到今年结束的步长
            size_month=range(size)
            if (int(time_list_last[1]))==2:
                if year%400 ==0:
                    day1=29(int(time_list_last[2]))
                else :
                    day1=28-(int(time_list_last[2]))
                day2=counter()
                pass
            elif ((int(time_list_last[1])) in _30day)==True:
                day1=30-(int(time_list_last[2]))
                day2=counter()
            elif ((int(time_list_last[1])) in _31day)==True:

                day1=31-(int(time_list_last[2]))
                day2=counter()  
                pass
            day3=day2
            size=(int(birthDay_G_last[1]))-1 #第二年到生日
            size_month=range(size)
            if (int(time_list_last[1]))==2:
                if year%400 ==0:
                    day1=29(int(time_list_last[2]))
                else :
                    day1=28-(int(time_list_last[2]))
                    day2=counter()
                    pass
            elif ((int(time_list_last[1])) in _30day)==True:
                day1=30-(int(time_list_last[2]))
                day2=counter()
            elif ((int(time_list_last[1])) in _31day)==True:
                day1=31-(int(time_list_last[2]))
                day2=counter()  
                pass
            day2=day2+(int(birthDay_G_last[2]))
            day4=size_year*365
            day_last=day1+day2+day3+day4
        elif (int(time_list_last[0]))>(int(birthDay_G_last[0])):
            if (int(time_list_last[1]))<(int(birthDay_G_last[1])):
                size=(int(birthDay_G_last[1]))-(int(time_list_last[1]))-1#生日还没过
                size_month=range(size)
                year = (int(time_list_last[1]))
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
                day_last=day1+day2
            #------------------------------------------------------
            elif (int(time_list_last[1]))>(int(birthDay_G_last[1])):#生日过了
                size=12-(int(birthDay_G_last[1]))#到今年结束的步长
                size_month=range(size)
                year=(int(time_list_last[0]))
                if (int(time_list_last[1]))==2:
                    if year%400 ==0:
                        day1=29(int(time_list_last[2]))
                    else :
                        day1=28-(int(time_list_last[2]))
                    day2=counter()
                    pass
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
                year=(int(time_list_last[0]))+1
                if (int(time_list_last[1]))==2:
                    if year%400 ==0:
                        day1=29(int(time_list_last[2]))
                    else :
                        day1=28-(int(time_list_last[2]))
                    day2=counter()
                    pass
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
            elif (int(time_list_last[1]))==(int(birthDay_G_last[1])):# 生日和时间在一块
                if ((int(time_list_last[2]))-(int(birthDay_G_last[2])))>0:
                    size=12-(int(birthDay_G_last[1]))#到今年结束的步长
                    size_month=range(size)
                    year=(int(time_list_last[0]))
                    if (int(time_list_last[1]))==2:
                        if year%400 ==0:
                            day1=29(int(time_list_last[2]))
                        else :
                            day1=28-(int(time_list_last[2]))
                            day2=counter()
                            pass
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
                    year=(int(time_list_last[0]))
                    if (int(time_list_last[1]))==2:
                        if year%400 ==0:
                            day1=29(int(time_list_last[2]))
                        else :
                            day1=28-(int(time_list_last[2]))
                            day2=counter()
                            pass
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
                    day_last=((int(birthDay_G_last[2]))-(int(time_list_last[2])))
                    pass
                elif ((int(time_list_last[2]))-(int(birthDay_G_last[2])))==0:
                    day_last=0
                    pass
                pass
            pass
        elif (int(time_list_last[0]))<(int(birthDay_G_last[0])):
            print("怕不是假人")
            print("请检查数据库数据")    
            pass
        return (day_last)
    

    #测试功能  最近过生日的
    print("="*30)
    x=range (len(name_find))
    
    for i in x:
        number = i
        Day_list1[i]=Days()
        Day_list2[i]=name_find[number]
        pass
    Day_list1[y:]=[]
    Day_list=Day_list1.copy()
    

    for i in x :
        v=min(Day_list)
        width=10-len(str(v))
        v1=Day_list1.index(v)
        Day_list[v1]=999999
        print("距生日还有："+str(v)+"天"+ "-"*width +str(Day_list2[v1]))
    
    
    print("="*30)
    #-----end


    name = input ("查询谁的信息：")
    number = name_find.index(name)
    day_last=Days()
    for i in name_base[number]:
        print(i)
        pass
    print("距离下次生日还有："+str(day_last)+"天")
    if day_last==0:
        print("他今天是寿星哦!!")
        pass
    print("="*30)
    time.sleep(500/1000)
    
    pass

#阴历生日还无法计算



