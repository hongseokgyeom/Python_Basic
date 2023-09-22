# 컬렉션 타입
# - 변수 하나에 값을 여러개 저장
# - 실질적으로 변수를 컬렉션 1개가 저장
# - *리스트(List), 투플(Tuple), *딕트(Dictionary), 세트(Set)

# 1. 리스트(List)
# - 시퀀스 자료형(연속 된 값을 저장)
# - 대괄호 사용[]
# - 정렬 가능
# - mutable(생성 된 후 변경 가능)
# - index 사용(slicing 가능)
# - packing 과 unpacking 가능
# - 멤버함수 : append(), extend(), insert(), remove(), pop(), index(), sorted() 등등
# 2차원 리스트는 표(table)과 동일한 형태

# 리스트 초기화(생성)
list_a = [1, 2, 3]
list_b = []
list_c = ["chosun", 98, 3.14, [1, 2, 3]]

print(list_c[1:3])  # 리스트 슬라이싱
print(list_c[0])  # 리스트 단일 값 추출
# 즉 문자열에서 쓰던 함수들 그대로 다 사용가능

#패킹과 언패킹
list_d = ["A", "B", "C"]  # 패킹
a, b, c = list_d # 언패킹

# a = list_d[0] -> Java, c

# append() : 마지막값에 추가
a = [1,2,3,4,5]
a.append(10)
print(a)

#insert() : 원하는 인덱스에 값 추가
a.insert(1,"A")  # 앞이 인덱스 뒤가 값
print(a)

# extend() : 리스트 확장 (list_a + list_b)
a = [1, 2, 3]
b = [3, 4, 5]
# a.append(b) -> [1, 2, 3, [3, 4, 5]] 즉, 리스트를 그냥 통으로 넣어버림
a.extend(b)  # a를 기준으로 병합 즉 a 가 123345 가 됨
print(a)

# 또는 그냥  print(a+b) 만 써도 됨

# remove() : 값으로 삭제
a = ["a", "b", "c"]
a.remove("b")
print(a)
# pop() : 인덱스로 삭제
b = ["a", "b", "c"]
c = b.pop(0)  # 값을 삭제 전 변수에 담아서 삭제 후 사용가능(선택사항)
print(b) # [b,c]
print(c) # [a, b, c]

# index() : 찾고자 하는 값의 인덱스 반환 tmi) ()안에 들어가는 값은 매개변수라고 함
a = [1, 2, 3]
print(a.index(3)) # 인덱스 반환 즉, 2 반환
# sort(), sorted() : 리스트 값 정렬
# - sort() : 원본 값 정렬
# - sorted() : 복제 한 값 정렬
a = [9, 3, 2, 1, 5, 8, 10]
b = sorted(a)  # 오름차순
c = sorted(a, reverse = True)  #내림차순
print(a)
print(b)
# 원본값을 잘 안바꾸기 때문에 보통 sorted 를 많이 씀 원본을 수정하는 경우는 극히 드뭄

# 1. 투플(tuple) ex) 기차
# - list 와 대부분 동일
# - 시퀀스자료형 (정렬 불가능)
# - immutable(생성 된 후 변경 불가능)
# - index 사용(slicing 가능)
# - packing unpacking 가능
# - () 자동(생략가능)
# 여러분이 직접 tuple 을 생성하는 경우 x
# -> 파이썬에서 결과값을 받을때 저절로 저장

print("_"*50)
a = [1, 2, 3]  #list
b = (1, 2, 3)  #Tuple
c = 1, 2, 3  #Tuple
a[0] = 99
print(a)

# b[0] = 99  Tuple 은 안됨
# print(b)

# 투플 원소가 1개일때

a = (1, 2, 3)  #Tuple
b = 1, 2, 3  #Tuple
c = (1)  #Tuple
d = 1  #Int
e = 1,
print(type(b))
print(type(d))
print(type(e))
print("_"*50)

a = 5
b = 8
a, b = b, a
#temp = a
#a = b
#temp = b
print(a)
print(b)

# 3. 세트(set) ex) 복주머니
# - 수학의 집합 개념
# - 순서 없음(index 없음, 정렬 불가능)
# - 중복값을 허용하지 않음(중요)
# - {}사용
# - 멤버함수 : union(), intersection(), difference()등등
# - 주로 중복값 제거용으로만 쓴다
print("_"*50)
set_a = {1, 2, 3}
set_b = {1, 1, 1, 1, 2, 2, 2, 3, 3, 4, 5}
print(set_a)
print(set_b)

# 중복값 제거 활용방법
a = ["A", "A", "B", "B", "C", "C", "D", "E"]  #List type
# a = set(a)  #() 안의 값을 set 타입으로 변환
# a = list(a)
a = list(set(a))  # 2개를 합침, 안쪽부터 계산 list - > set-> list
print(a)
print(type(a))
print("_"*50)

# 4. 딕트(dict) ex) 복주머니
# - 순서가 없음(index 없음, 정렬 불가능)
# - {key:value} 사용 -> key value I pair
# - key 는 중복불가, value 중복 가능
# - ket 를 통해서만 value 에 접근 가능
# - 멤버함수 : update(), get(), keys(), value(), items()
# 외부에서 데이터를 받아올 때 대부분 JSON 형식으로 전달
#      - JSON == DICT(동일)
print("_"*50)
dict_a = {"Korea" : "Seoul",
          "Canada" : "Ottawa",
          "USA" : "WachingtonD.C" }
print(dict_a)
import pprint
pprint.pprint(dict_a)

# update() : dict와 dict 병합
a = {"a" : 1,
     "b" : 2}
b = {"b" : 3,
     "c" : 5}
a.update(b) # 병합시 중복key 있는경우 입력값(b)이 우선
print(a)

# pop : dict 원소를 key 를 통해서 삭제
c = a.pop("a")
print(a)
print(c)  # {"a" : 1} 삭제된 value(key x)
print("_"*50)

# in() : ()안에 key 값 존재 확인

print("c" in a)
print("f" in a)

# get() : 값 접근
# list, tuple, dict 접근 -> 컬렉션[index or key] ex : a[2]
print(a["c"])
# print(a["f"]) key 없으면 error 발생
print(a.get("f")) # key 가 없으면 none  출력

# keys(), values(), items()
#print(a.keys()  #key 만 추출
#print(a.values())  #value 만 추출
#print(a.items())  #(key, value) 추출
# clear() : dict 초기화
print(a)
a.clear()
print(a)
e = {}
print(type(e))
print("_"*50)