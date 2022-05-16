
for i in range(0,4):
    name=input("이름 : ")
    score=int(input("점수를 입력하세요:"))
    
    if score >=90 :
        print("%s의 학점: a"%name)
    elif score>=80 :
        print("%s의 학점: b"%name)
    elif score>=70 :
        print("%s의 학점: c"%name)  
    elif score>=60 : 
        print("%s의 학점: d"%name)     
    else :
        print("%의 학점:f"%name)
        
         
        