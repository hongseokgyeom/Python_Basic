# 조건문 : if elif else
# - 특정 조건을 만족하는 경우에만 수행 할 작업이 있는경우
# - 조건문의 경우 if elif else 밑에 코드 들여쓰기 필수

# if (조건1){                      if 조건1
#    code                             code
# else if (조건2){                 elif 조건1
#    code                             code
# 제어문 기본 문법
# if 조건1:
#    code
# elif 조건2:
#      code
# else:
#      code
#  이러한 방식 chain 이라하고 참이라고 나올때 까지 하나만 실행

# 조건문 4가지 조합
# 1. if
# 2. if ~ elif
# 3. if ~ else
# 4. if ~ elif ~ else

# 점수 계산기
# - 91~ 100 A
# - 81~ 90 B
# - 71~ 80 C
# - 61~ 70 D
# - 60 이하 f

# score = int(input("input score : "))
# if score >= 91:
#    print("A")
# elif score >= 81:
#     print("B")
# elif score >= 71:
#    print("C")
# elif score >= 61:
#     print("D")
# else:
#    print("F")

# 논리 연산자 : AND OR NOT
# 1 . AND
# 조건1 조건 2 결과
#  F     F     F
#  T     F     F
#  F     T     F
#  T     T     T


# 2. OR
# 조건1 조건2 결과
#  F     F    F
#  F     T    T
#  T     F    T
#  T     T    T

# 3. NOT
# T -> F
# F -> T

# 문제 1. 어떤 종류의 학생인지 맞추기
# 초등, 중등, 고등, 대학생, 학생
print('-'*50)
from datetime import datetime


# input() : 키보드 값 입력 -> (문자열)
born = int(input("당신이 태어난 년도를 입력하세요 : "))
today = datetime.today().year
age = today - born + 1
if 0<= age <= 26:
    if age >= 20:
        print("대학생")
    elif age >= 17:
        print("고등학생")
    elif age >= 14:
        print("중학생")
    elif age >= 8:
        print("초등학생")
else:
    print("학생이 아닙니다")