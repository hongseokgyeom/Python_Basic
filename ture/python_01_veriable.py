print("-"*50)
print("Hello Python")
print("-"*50)

#참고 - escape code
# - 문법 \ (역슬러쉬) + @
# - 문자열(string) 내의 일부 문자의 의미를 달리하여 특정한 효과 추가
# - 예) \n 한 줄  , \t 탭 (8칸 공백)
# - c+s+f10(run)

print("Hello \npython")
print("Hello \tpython")
print("-"*50)
# 공부팁)
# - 몇버전 부터 나온 기술(신기술) -> 신기술 공부 , 구기술 공부 x -> 옛 코드 쓰는 업체는 코드 이해 못할수도

# 자료형(type)
# - python의 모든 자료형은 객체(object)
# - c, Java 언어 문자형(char): 'A', 'E' (키보드 제어시 필요) -> python은 x
# 1) 문자열(string) : "Hello" , 'Hi'
# 2) 정수형(int) : 3, 0, -1
# 3) 실수형(float) : 3.14, 0.0, -2.2
# 4) 논리형(boolean): True, False

# 예) 다양항 종류의 자료형을 사용하는 이유
# - Java 에서 정수형 : byre, short, int, long
# - Python 에서 정수형 : int
# 만들어진지 오래 된 언어는 다양한 종류의 자료형을 사용!
# 이유는: 자원(메모리)를 효율적으로 사용하기 위해서
# 예: 자료형은 담을 수 있는 크기의 범위가 지정되어 있음
#     예를 들어서 int는(-10000~10000)까지 담을 수 있다고 가정
#      그런데 우리 회사에서 툭정 값이 0~9만 사용!
#      int를 사용하게 되면 메모리낭비, 이런 경우 크기의 범위가 더
#      작은 자료형을 사용하면 좋음(short)
# python은 메모리 용량이 늘어남에 따라 int만 써도 충분함


# python 동적 타이핑 언어 -> python이 실행 될 때 Type을 지정!
# type() 함수 : ()안의 값의 Type 값을 확인 할 때 사용

print(type("ABC"))
print(type(123))
print("-"*50)
# 중요 - 형 변환(Type Casting)
# - Type Casting 을 사용하면 값을 원하는 자료형으로 변환 가능
# 1) int() : 정수형으로 변환
# 2) float() : 실수형으로 변환
# 3) str() : 문자열형으로 변환

# Type Casting 실습
int_a = 3
float_b = 3.14
str_c = "9.2"
str_int_c = "9"
str_float_d = "9.2"
# 1) 문자열 정수형("9") -> 정수형(9)
print(int(str_int_c))
# 2) 문자열 정수형("9.2") -> 실수형(9.0)
print(int(str_int_c))
# 3) 문자열 실수형("3.14") -> 정수형(3)
print(float(str_float_d))
# 4) 문자열 실수형("3.14") -> 실수형(Error x)
#print(int(str_float_d))
# 5) 정수형(3) -> 실수형(3.0)
print(float(int_a))
# 6) 정수형(3) -> 문자열("3")
print(str(int_a))
# 7) 실수형(3.14) -> 정수형(3)
print(int(float_b))
# 8) 실수형(3.14) -> 문자열("3.14")
print(str(float_b))  #123(코드 옆 작성은 2칸 띄우고 달기)
# *float("Hello"), int("Hello") 형변환 불가 -> 문자를 숫자로 바꿀수는 없으므로
print("-"*50)

#None
# - 아무런 값을 갖지 않을 때 사용
# - 일반적으로 변수가 초기값을 갖지 않게 변수만 생성하고 싶을때 사용
# - 기타 언어의 Null 과 같은 의미로 사용!
# 예) student_name 변수만 만들고 싶을때 그냥 쓰면 에러남 밑예시처럼 쓰면 에러 안남
student_name = None # 적극 권장 X (절대 사용금지)
student_name = ""   # 적극 권장 O
# 이유? "Null Pointer Exception" Error 개발자 공포의 대상!! -> 프로그램 다 꺼져버림

# 기본 자료형(Primitive Type) : 변수의 값이 저장
# 예시) int num = 4;
# 객체 자료형(Reference Type) : 변수의 값에 "주소" 가 저장됨
# 예시) string name = "10";

# 방에 값을 저장한다고 치면
# None, Null 은 값이 없는게 아니라 방만 남아있는상태
# 값이 없다 -> 방까지 모두 아에 없는상태

# *Java: 기본, 객체 모두 사용
# *Python: 객체만 사용

# C언어에서 변수 생성 -> int b;/ (변수 생성 값X)
# Python 변수 생성 -> b (변수 호출) "생성이 아님" -> 동적 타이핑 언어라
#                    값 보고 지정하기 때문에 값을 먼저 넣어줘야 되서 None 이라도 넣어줘야 생성됨

# 변수(Variable)
# - 변수 : "하나의 값"을 저장 할 수 있는 메모리 공간

num = 4
num = 10
print(num)  # 출력 10 즉 원래 값이 있어도 새로운 값이 들어오면 그 값만 남게됨(하나의값)

# 변수 생성 및 초기화(값을 다시 저장하는 행위)
# num = 5  # 문법
# 초기화 라고 하는 이유 : 삭제를 해도 공간만 사용할 수 있게 열리고 램에는 남는데
# 다른 변수를 지정해 줌으로써 그 값이 영구 삭제 되면서 새로운 값을 등록함

# 대입연산자(=) : 우측의 값을 좌축에 저장
# 동등연산자(==) : Equal
