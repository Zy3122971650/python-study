b = 0
a = 0
num4=0
num5=0
num6=0
num7=0
x= input("X的数组：").split(",")
y= input("Y的数组：").split(",")
num1 = 0
num2 = 0
num_x = len(x)
num_y = len(y)

# 计算平均值
for i1 in x:
    num1+=int(i1)
    pass
for i2 in y:
    num2+=int(i2)
    pass
x_mean = num1/num_x
y_mean = num2/num_y

#计算截距    
numb3 = range (len (x))

for i3 in numb3 :
    num4+=((int(x[i3]))-x_mean)*(int(y[i3])-y_mean)
    num5+=((int(x[i3]))-x_mean)**2
    pass
b=num4/num5
a = y_mean - (b*x_mean)

print("y="+str(b)+"x"+" "+ str(a))

# Y的预测值
def y_p(x_predict):        
    y_predict=b*int(x_predict)+a
    return(y_predict)
    pass
result = 0

# 计算相关系数
for i4 in numb3:
    num6+=((int(y[i4]))-y_p(x[i4]))**2
    num7+=((int(y[i4]))-y_mean)**2
    
    pass
result=num6/num7
print("R**2="+str(1-result))

       
                  
    
input("按任意键返回")
# 165,165,157,170,175,165,155,170
# 48,57,50,54,64,61,43,59