AUTH = True

# 사용 승인 체크 데코레이터
def auth_required(func):
    pass

# 이 함수에 완성된 데코레이터를 적용해주세요.
def order_list():
    print("*********************")
    print("구매 리스트 출력")
    print("만두, 아이스크림, 콜라")
    print("*********************")

# 이 함수에 완성된 데코레이터를 적용해주세요.
def return_list():
    print("*********************")
    print("반품 리스트 출력")
    print("커피, 책")
    print("*********************")

# 이 함수에는 데코레이터를 적용하지 마세요.
def recommend_list():
    print("*********************")
    print("추천 목록 출력")
    print("참치, 라면, 피자")
    print("*********************")

while True:
    print("============================")
    print("[1] : 구매 리스트")
    print("[2] : 교환 반품 리스트")
    print("[3] : 오늘의 추천 상품")
    c = input("메뉴 선택: ")

    if c == "1":
        order_list()
    elif c == "2":
        return_list()
    elif c == "3":
        recommend_list()
    else:
        break


