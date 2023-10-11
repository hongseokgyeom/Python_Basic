# 제어문
# 1. 조건문 (if, switch case도 있긴 있으나 잘 안씀 if 문 위주)
# 2. 반복문 (for, while)


# 반복문(Loop)
# - 반복적인 작업을 가능하게 해주는 도구
# - list, str, tuple 등 컬렉션 타입의 아이템을 하나씩 순회 하면서 사용가능 (for)
# - 특정 조건을 만족하는 경우 (while)

# 반복횟수 o -> for
# 반복횟수 x -> while

# for 문
# for i in [1, 2, 3]
#    print(i)
# range(시작, 끝, 증감)
# range(3) 시작값 생략이므로 0부터  => 0, 1, 2
# range(1, 10) => 1, 2, 3, 4, 5, 6, 7, 8, 9 증감 생략시 +1
# range(2, 5, 2) => 2, 4

for i in range(1,10):
    print(i)

temp = ["A", "B","C","D","E","F","G","H","I","J"]
for alpha in temp:
    print(alpha)

# 반복횟수(index) 출력하고 싶은 경우!
# - enumerate()

for alpha in enumerate(temp):
    print(i, alpha)
print('-'*50)

# 구구단 2단 출력
# 2 x 1 = 2
# input() 활용 그 숫자 단 출력
for i in range(1,10):
    print(f"2x{i}={2*i}")
print('-'*50)

dan = int(input("단수 :"))
for i in range(1,10):
    print(f"{dan}*{i}={dan*i}")

# 2단 부터 9단까지 출력

for i in range(2,10):
    for j in range(1,10):
        print(f"{i}x{j}={i*j}")
# dict 이용
temp = {"A" : 1,
        "B" : 2,
        "C" : 3}

# dict -> for -> key 값 출력
# keys(), values(), items() 아무것도 안썼을 때 keys 가 나오므로 굳이 쓸 필요 없음..
for element in temp.values():
    print(element)

for element in temp.items():
    print(element)

for key, value in temp.items():
    print("******")
    print(key)
    print(value)

# break, continue
# break : 즉시 반복문 빠져나감
# continue : 즉시 다음 반복으로
#홀수 출력
for i in range(30):
    if i % 2 ==0:
        continue