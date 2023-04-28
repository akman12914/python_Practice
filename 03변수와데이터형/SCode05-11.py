#종합계산기

select = 0;
mathExpress = "";
answer = 0;
x = 0;
y = 0;

select = int(input("1. 입력한 수식 계산 2. 두 수 사이의 합계: : "))

if select == 1 : 
    mathExpress = input("*** 수식을 입력하세요 :")
    print("%s 결과는 %f입니다." % (mathExpress, eval(mathExpress)))
elif select == 2 :
    x = int(input(" *** 첫 번째 숫자를 입력하세요 :"))
    y = int(input(" *** 두 번째 숫자를 입력하세요 :"))
    for i in range(x, y+1):
        answer = answer + i
    print("%d +...+ %d는 %d입니다." % (x, y, answer))
else : 
    print("1 또는 2만 입력하시길..:)")