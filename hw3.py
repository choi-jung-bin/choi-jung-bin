name = input()
score=int(input())
if(score in range(90,101)):
    print("%s의 학점 : A"%name)
elif(score in range(80,90)): 
     print("%s의 학점 : B"%name)
elif(score in range(70,80)): 
    print("%s의 학점 : C"%name)
elif(score in range(60,70)):
    print("%s의 학점 : D"%name)
else:
    print("%s의 학점:F"%name)
    
       