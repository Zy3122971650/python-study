from math import *
array=[1,2,3,4,5,6,7,8,9]
glod=9
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
        
a=bsearch (array,glod)
print(a)
print(array)
input()
