import math as mymodule

pi=mymudule.pi

def myradius(r):
    result=2*pi*r
    return result

def myarea(r):
    return pi*mymodule.pow(r,2)

i = int(input("반지름을 입력하시오:"))
result1 = myradius(i)
result2 = myarea(i)

print("둘레는",result1,"넓이는",result2)
print("둘레는 "+str(result1)+" 넓이는 "+str(result2))
print("둘레는 {0} 넓이는 {1}".format(result1,result2))
print("둘레는 %f 넓이는 %f" % (result1,result2))


a=2

def sum(num):
    a= num+1 
    return a 
print(sum(4))
print(a)

b=[1,2,3,"안녕"]

def myfunc(c):
    c.append(4)
    c.remove(1)

print(b)    
myfunc(b)
print(b)


def gugudan(num) :
    print("구구단은"+str(num)+"단입니다.")
    for i in range(1,10):
        print("%d x %d =%d"%(num,i,num*i))
        
a=int(input("몇단을 출력할까요?"))
gugudan(a)
        
           