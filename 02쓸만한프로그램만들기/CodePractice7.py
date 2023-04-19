#정수 2개를 입력받아서 더하기, 곱하기, 제곱 연산을 하는 프로그램 작성

value1 = int(input('숫자1 입력:'))
value2 = int(input('숫자2 입력:'))
print(value1, '+', value2, '=', value1 + value2)
print(value1, '*', value2, '=', value1 * value2)
print(value1, '^', value2, '=', (pow(value1, value2))) 