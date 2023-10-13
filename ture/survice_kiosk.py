# 키오스크 기능들

# 사용자 메뉴 선택 가능
# 1. 메인 메뉴 선택(1, 2, 3, 99)
# 2. 세부 메뉴 선택(1 ~ 4 or 1 ~ 3)
# max_cnt : 메뉴별 갯수
# menu_type : main or sub

def user_choice(max_cnt, menu_type):
    while True:
        choice = int(input(">> 번호 : "))
        # main 메뉴에서 99 를 입력하면
        if choice == 99 and menu_type == "main":
            return choice
        if max_cnt >= choice >= 1:
            return choice
        else:
            print("MSG : 올바른 번호를 입력하세요")