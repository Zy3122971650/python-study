import matplotlib.pyplot as plt
import string as st
import re
from math import *



print("多个算式用;隔开","定义域用区间表示")

def  bsearch (array,glod,constraint=None):    #待查找的数组，目标值，如果constraint==0 目标值不存在于数组中时则取大于它最近值，若==1则返回No
    i=0
    array.sort()
    long=len(array)
    num_star=0
    num_end=(long-1)
    if constraint == None:
        constraint=1
    while True:
        if i ==0 :
            indx=float((long-1)/2)
        else:
            indx=float((long)/2)
        i+=1
        if int(indx)!=indx :
            num1=ceil(indx)
            num2=floor(indx)
        else:
            num1=int(indx)
            num2=int(indx)-1
            pass
        if (glod in array)==False and constraint==1:
            return("No") 
        if array[num1]==glod or array[num2]==glod or (array[num1]>glod and array[num2]<glod):
            if array[num1]==glod or (array[num1]>glod and array[num2]<glod):
                return (num1)
            elif array[num2]==glod:
                return(num2)
        elif  array[num1]>glod and array[num2]>glod:
            num_end=num2
            long=(num_end+num_star)
        elif  array[num1]<glod and array[num2]<glod:
            num_star=num1
            long=(num_end+num_star)
        
            
            pass#返回目标值或者目标值不存在时，返回大于它最近的值
def get_expression () :
    global size
    temp_expression=input("请输入要求解的算数：")
    temp_dod_x=input("定义域：").strip()
    if temp_dod_x == "":
        temp_dod_x="[-10,10]"
        pass 
    
    size=input ("你想多精细：").strip()
    if size == "":
        size= 0.01
        pass
    size=float(size)
    if "[" in temp_dod_x: #极值可否取
        star_x=0
    else:
        star_x=1
        pass
    if "]" in temp_dod_x:
        end_x=0
    else:
        end_x=1 
        pass

    #X的定义域
    temp_dod_x=temp_dod_x.strip("[]()")
    dod_x_array=temp_dod_x.split(",")
    
    res=float(dod_x_array[0])
    dod_x=[]
    while res<float(dod_x_array[1]):
        res+=size
        dod_x.append(res)
        pass
    expression=temp_expression.split(";")
    
    return(expression,dod_x)
    pass#获取表达式，定义域


def draw (expression,dod_x_source):
    for i in expression:        
        #初始化
        dod_x=dod_x_source.copy()
        global size
        name=i
        i=i.split("=")
        i=i[1]
        print("计算开始")
        try :
            res_y=[eval(i) for x in dod_x]
            plt.plot(dod_x,res_y,label="{}".format(name))
        except:
            x_really=i
            #纠正不能取'0'定义域   
            #x_really = re.search('\(\S+\)',i,re.U) #正则取括号真实定义域   y=((x+1)**2)取不到正确值  需要多次匹配
            #x_really=(x_really.group()).strip("()")  会将前面两个括号全部消去  采取手动去括号
            while True:
                x_really = re.search('\(\S+\)',x_really,re.U)
                x_really=x_really.group()
                x_really=list(x_really)
                if x_really.count("(")==1:
                    break
                #去括号
                x_really.pop(0)
                x_really.pop((len(x_really))-1)
                x_really="".join('%s' %id for id in x_really)
            try:
                
                x_indx=x_really.index('x')
                x_really[x_indx]=0
                x_really="".join('%s' %id for id in x_really)
                glod=float(0-(eval(x_really)))
                unnum=[]#Undersirable number
               
                #多次取值 扣掉‘0’
                while True :
                    indx=bsearch(dod_x,glod,1)
                    if indx=="No":                       
                        break
                    unnum.append(indx)
                    dod_x.pop(indx)
                for i3 in (unnum):
                    dod_x1=dod_x[:i3]
                    res_y=[eval(i) for x in dod_x1 ]
                    plt.plot(dod_x1,res_y,label="{}".format(name))
                    dod_x[:i3]=[]
                plt.plot(dod_x,res_y,label="{}".format(name))
            except:
                #纠正只能取正定义域函数定义域
                #重复片段
                x_really=i
                while True:
                    x_really = re.search('\(\S+\)',x_really,re.U)
                    x_really=x_really.group()
                    x_really=list(x_really)
                    if x_really.count("(")==1:
                        break
                    #去括号
                    x_really.pop(0)
                    x_really.pop((len(x_really))-1)
                    x_really="".join('%s' %id for id in x_really)
                    #重复片段
                if 'log' in i :
                    #将定义域取正
                    #转化X为0
                    x_indx=x_really.index('x')
                    x_really[x_indx]=0
                    x_really="".join('%s' %id for id in x_really)
                    glod=float(0-(eval(x_really)))
                    indx=bsearch(dod_x,glod,0)
                    dod_x=dod_x[(indx):]
                res_y=[eval(i) for x in dod_x ]
                plt.plot(dod_x,res_y,label="{}".format(name))
                #end
            print("该定义域不能为 负 已经纠正")
    plt.legend()
    plt.show()
#执行函数
while True:
    # gca = 'get current axis'
    ax = plt.gca()
    # 将右边和上边的边框（脊）的颜色去掉
    ax.spines['right'].set_color('none')
    ax.spines['top'].set_color('none')
    # 绑定x轴和y轴
    ax.xaxis.set_ticks_position('bottom')
    ax.yaxis.set_ticks_position('left')
    # 定义x轴和y轴的位置
    ax.spines['bottom'].set_position(('data', 0))
    ax.spines['left'].set_position(('data', 0))
    #expression,dod_x=get_expression()
    #draw(expression,dod_x)
    try:
        expression,dod_x_source=get_expression()
        draw(expression,dod_x_source)
    except:
        print("格式有误")
        continue
    pass

