#문자열의 이해(string)

#1. 문자열 인덱스
# - 문자열은 각 문자마다 순서(인덱스)가 있음
# - 첫번째 문자부터 마지막 문자까지 순차적으로 인덱스
# - 인덱스 시작은 0
# - 인덱스는 공백 포함
print("_"*50)
print("python")
# 문자추출
# - 인덱스를 통해서 문자 추출
# - 인덱스 범위를 벗어난 경우 오류(Error : index out of range)
lang = "python"
print(lang[0])
print(lang[2])
#print(lang[9]) : Error
# -1 인덱스 (Reverse Index)
# - 우측에서 좌측으로 인덱스
# - 시작값 -1
print(lang[-1])
print(lang[-3])
print("_"*50)
#Id 를 이메일로 ~~~~~@gmail.com

#문자열 슬라이싱
# - lang[3] : 문자 1개 추출
# - 부분 문자열을 추출하고 싶은 경우
# 시작인덱스 끝 인덱스 필요!
msg = "Python is all you need"
print(msg[0:6])  # 끝인덱스(+1 해야함)
print(msg[:6])  # 시작인덱스 생략시 -> 자동 0입력
print(msg[3:])  # 끝 인덱스 생략 -> 자동 -1 입력
#Quiz
#msg에서 "need"만 추출
print(msg[-4:])
print(msg[18:])
print("_"*50)
#문자열 함수
#문자열 길이 계산
str = "Hello world"
# 정방향 인덱스 0~10, 역방향 인덱스 -11 ~ -1
print(len(str))
print("_"*50)
# - 데이터 전처리 1A,1a -> 1A 로 통일 (upper()) 
print(str.upper())  #전부 대문자로
print(str.lower())  #전부 소문자로
print("_"*50)
# 4.3 .replace() :문자열 내의 특정 문자 치환
print(str.replace("H","J")
# 4.4 .split() : 구분자를 기준으로 문자열 분할(Default: 공백)
b = "hello world what a nice weather"
print(b.split("W"))  #즉 w 기준으로 하였기 때문에 공백도 그대로 놔두고 분할함
print(b.split())
# 4.5 .strip() : 문자열의 좌우 공백 제거
id = "                 python1004              "
print(id)
print(id.strip())
# 4.6 .find() and rfind() : 문자열 내부의 특정 문자의 위치 인덱스 출력(단, 중복되는 내용을 다 찾진 않고 제일 먼저 나온 값의 인덱스만 출력)
print(str.find("o"))  # 앞에서부터 Hell"o" world 를 찾음
print(str.rfind("o"))  # 뒤에서부터 Hello w"o"rld 를 찾음 
print(str.find("world"))  # 없으면 -1 출력
print(str.find("World"))  # 단어의 첫글자의 인덱스 출력
print(str.rfind("World"))  # 뒤에서 부터 읽는다고 뒷글자가 나오는게 아니라 단어의 첫글자 인덱스 출력
# 4.7 .in() : 특정 문자열 포함하는지 확인 (True, False 출력)
print("Hi" in "Hi Python")

# 1. "cherry1004@gmail.com" 안에서 id 만 추출

id  = "cherry1004@gmail.com"
val = (id[:10])
print(val)

# 2. "cherry1004@gmail.com"
#    "job1234@gmail.com"
#    "abc@gmail.com"
val= id[:id.find("@")]
print(val)

#3. naver, daum 등 추출하는 프로그램
url = "www.naver.com"
#print(val)  # naver
start = url.find(".") + 1
end = url.frind(".")
val = url[start:end]
print(val)
