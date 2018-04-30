import time
import pymysql
from datetime import datetime
db=pymysql.connect("host","root","password","database")
cursor=db.cursor()
cursor.execute("select * from Birthday")
data = cursor.fetchall() #((),()) 元组包含的形式
cursor.close()
db.close()

#处理结果 可视化
#i=range(len(data))
#for j in i:
#    print("-"*(len(str(data[j][2]))+13))
#    print("|","姓名",data[j][1]," "*((len(str(data[j][2])))+13-8-2-(len(str(data[j][1])))),"|")
#    print("|","出生日期",data[j][2],"|")
#    print("-"*((len(str(data[j][2])))+13))
#    pass 
    
 #自动添加

while True:
    name_find=["Unkonw"]*1000
    name_base=["Unkonw"]*1000
    Day_list=["Unkonw"]*1000
    Day_list1=["Unkonw"]*1000
    Day_list2=["Unkonw"]*1000
    def Add(number,name,G_year):
        name_find[number]=name
        name_base[number]=name=["姓名：{}".format(name),"出身年月：\n阳历年：{}\n农历年：0.0.0.0".format(G_year)]
        pass
    i=range(len (data))
    for j in i:
        number1=int(data[j][0])-1
        name=data[j][1]
        G_year=str(data[j][2])
        Add(number1,name,G_year)
        pass

    print(datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
    time_list_last=datetime.now().strftime('%Y %m %d %H:%M:%S').split()

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
        birthDay_3=birthDay_2[1].split("：")
        birthDay_4=str(birthDay_3[1][:4])
        birthDay_5=str(birthDay_3[1][4:6])
        birthDay_6=str(birthDay_3[1][6:8])
        birthDay_G_last=[None]*3
        birthDay_G_last[0]= birthDay_4
        birthDay_G_last[1]= birthDay_5
        birthDay_G_last[2]= birthDay_6
       
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
    y=name_find.index("Unkonw")
    name_find[y:]=[]
    name_base[y:]=[]
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
