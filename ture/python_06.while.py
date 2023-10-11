# while 반복문
# - 반복횟수를 모르는 경우
# - 조건이 만족하는 동안 계속 반복
# - 조건이 True 이면 무한 반복
# - 조건이 False 이면 반복종료
# - while 문 조건 True - 무한loop문(조심)
# - 반드시 break 문과 함께 사용할 것

# while 문 기본문법
# while 문 조건:
#   실행문


a = list(range(1, 6))  # [1, 2, 3, 4, 5, 6]
print(a)

i = 0  #index
while i < len(a):
    print(a[i])
    i += 1
