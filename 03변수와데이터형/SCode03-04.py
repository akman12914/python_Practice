#16진수 받아서 출력하기 
sel = int(input("입력 진수 결정(16/10/8/2) :"))
num1 = input("값 입력:")


if sel == 16 : 
    num = int(num1, 16)
if sel == 10 :
    num = int(num1, 10)
if sel == 8 :
    num = int(num1, 8)
if sel == 2 :
    num = int(num1, 2)

print("16진수 ==>", hex(num))
print("10진수 ==>", num);
print("8진수 ==>", oct(num))
print("2진수 ==>", bin(num))