import sys
from DBController import DBController
from Constant import QUERY, INPUT_TYPE, PAYMENT_TYPE
from IOManager import IOManager


# 메뉴 출력 스트링
MENU_STRING = ["print all buildings",
               "print all performances",
               "print all audiences",
               "insert a new building",
               "remove a building",
               "insert a new performance",
               "remove a performance",
               "insert a new audience",
               "remove an audience",
               "assign a performance to a building",
               "book a performance",
               "print all performances which assigned at a building",
               "print all audiences who booked for a performance",
               "print ticket booking status of a performance",
               "exit",
               "reset database",
               "book a performance with a specific payment method (extend)",
               "print ticket booking status and sales of a performance (extend)"]


# 테스트 함수입니다!! 참고용...
def test():
    # Constant 파일의 DEBUG모드 있어요! True 하면 쿼리 sql이랑 결과 프린트 하게 해놨어요
    
    print()
    # 파라미터가 0개인 쿼리 수행  query.xml의  SELECT_BUILDING 참고
    re = DBController.instance().excuteQuery(QUERY.SELECT_CONCERT_HALL)
    # 출력은 이렇게... 리턴받은 객체를 넘겨주세요
    IOManager.printTable(re)

    print()
    # 파라미터가 2개인 쿼리 수행  query.xml의  SELECT_PERFORMANCE 참고
    #re = DBController.instance().excuteQuery(QUERY.SELECT_CONCERT, '1', 1)
    # 출력은 이렇게... 리턴받은 객체를 넘겨주세요
    #PrintManager.printTable(re)

    # 에러 출력 예시
    IOManager.printError("에러는 이렇게 출력하세요")


# 1번 선택 시
def print_all_buildings():
    # 콘서트 홀(Building) 정보 받아와서 출력
    re = DBController.instance().excuteQuery(QUERY.SELECT_CONCERT_HALL)
    IOManager.printTable(re)


# 2번 선택 시
def print_all_performances():
    # 콘서트(Performance) 정보 받아와서 출력
    re = DBController.instance().excuteQuery(QUERY.SELECT_CONCERT)
    IOManager.printTable(re)


# 3번 선택 시
def print_all_audiences():
    # 관객(Audience) 정보 받아와서 출력
    re = DBController.instance().excuteQuery(QUERY.SELECT_AUDIENCE)
    IOManager.printTable(re)


# 4번 선택 시 : 콘서트 홀(Building) 추가
def insert_a_new_building():
    # 필요 정보 입력
    name = IOManager.input("Building name: ")
    loc = IOManager.input("Building location: ")
    cap = IOManager.input("Building capacity: ", inputType=INPUT_TYPE.INT, minvalue=1)

    # DB에 insert 쿼리 수행 적용 컬럼 수가 1인지 비교하여 성공 출력
    if DBController.instance().excuteQuery(QUERY.INSERT_CONCERT_HALL, name, loc, cap) == 1:
        print("A building is successfully inserted")


# 5번 선택 시 :  콘서트 홀(Building) 삭제
def remove_a_building():
    # 필요 정보 입력
    id = IOManager.input("Building ID: ", inputType=INPUT_TYPE.INT, minvalue=1)

    # 콘서트홀 삭제 쿼리 수행 / 적용 컬럼 수가 1인지 비교하여 성공 출력 (빌딩 없는 경우)
    if DBController.instance().excuteQuery(QUERY.DELETE_CONCERT_HALL, id) == 0:
        IOManager.printError("Not Exist Building (" + str(id) + ")")
    else:
        print("A building is successfully removed")


# 6번 선택 시 : 공연 추가
def insert_a_new_performance():
    # 필요 정보 입력
    name = IOManager.input("Performance name: ")
    typ = IOManager.input("Performance type: ")
    price = IOManager.input("Performance price: ", inputType=INPUT_TYPE.INT)

    # DB에 insert 쿼리 수행 적용 컬럼 수가 1인지 비교하여 성공 출력
    if DBController.instance().excuteQuery(QUERY.INSERT_CONCERT, name, typ, price) == 1:
        print("A performance is successfully inserted")


# 7번 선택 시 : 공연 삭제
def remove_a_performance():
    # 필요 정보 입력
    id = IOManager.input("Performance ID: ", inputType=INPUT_TYPE.INT, minvalue=1)

    # 공연 삭제 쿼리 수행 / 적용 컬럼 수가 0 이면 빌딩이 없는 것이므로 에러 출력 (공연 없는 경우)
    if DBController.instance().excuteQuery(QUERY.DELETE_CONCERT, id) == 0:
        IOManager.printError("Not Exist Performance (" + str(id) + ")")
    else:
        print("A performance is successfully removed")


# 8번 선택 시 : 관객 추가
def insert_a_new_audience():
    # 필요 정보 입력
    name = IOManager.input("Audience name: ")
    gender = IOManager.input("Audience gender: ", inputType=INPUT_TYPE.GENDER)
    age = IOManager.input("Audience age: ", inputType=INPUT_TYPE.INT, minvalue=1)

    # DB에 insert 쿼리 수행  / 적용 컬럼 수가 1인지 비교하여 성공 출력
    if DBController.instance().excuteQuery(QUERY.INSERT_AUDIENCE, name, gender, age) == 1:
        print("A audience is successfully inserted")


# 9번 선택 시 : 관객 삭제
def remove_an_audience():
    # 필요 정보 입력
    id = IOManager.input("Audience ID: ", inputType=INPUT_TYPE.INT, minvalue=1)

    # DB에 DELETE 쿼리 수행  / 적용 컬럼 수가 0인지 비교하여 에러 출력 (관객 없는 경우)
    if DBController.instance().excuteQuery(QUERY.DELETE_AUDIENCE, id, id) == 0:
        IOManager.printError("Not Exist Audience (" + str(id) + ")")
    else:
        print("A audience is successfully removed")


# 10번 선택 시 : 공연 배정
def assign_a_performance_to_a_building():
    # 필요 정보 입력
    bId = IOManager.input("Building ID: ", inputType=INPUT_TYPE.INT, minvalue=1)
    pId = IOManager.input("Performance ID: ", inputType=INPUT_TYPE.INT, minvalue=1)

    # 공연 가져오는 함수 수행(DB 쿼리 후 없으면 에러 있으면 리턴)
    re = getPerformanceByID(pId)
    assign = re[0]['CONCERT_HALL_ID']

    # assign된게 없으면 에러 출력
    if assign is not None:
        IOManager.printError("Already assigned performance (" + str(pId) + " assigned to " + str(assign) + " building)")
        return

    # 콘서트홀 존재 유무 확인
    re = DBController.instance().excuteQuery(QUERY.SELECT_CONCERT_HALL_BY_ID, bId)
    if len(re) == 0:
        IOManager.printError("Not Exist building")
    else:
        size = int(re[0]['CAPACITY'])

        # 콘서트홀 assign update 쿼리 수행 / 적용 컬럼이 없을경우 에러 출력
        if DBController.instance().excuteQuery(QUERY.UPDATE_CONCERT_CONCERT_HALL_ID, bId, pId) != 0:
            # assing 된 후 예약 정보 insert 하는 프로시져 수행
            DBController.instance().excuteQuery(QUERY.INSERT_RESERVATION, pId, size)
            print("A performance is successfully assigned")
        else:
            IOManager.printError("assigned Error")


# 11번 선택 시 : 공연 예매
def book_a_performance():
    # 필요 정보 입력
    pId = IOManager.input("Performance ID: ", inputType=INPUT_TYPE.INT, minvalue=1)
    aId = IOManager.input("Audience ID: ", inputType=INPUT_TYPE.INT, minvalue=1)
    seatStr, seatCnt = IOManager.input("seat number: ", inputType=INPUT_TYPE.SEAT, minvalue=1)

    # 관객 ID 여부 확인
    re = DBController.instance().excuteQuery(QUERY.SELECT_AUDIENCE_BY_ID, aId)

    if len(re) == 0:
        IOManager.printError("Not Exist Audience (" + str(aId) + ")")
        return

    age = re[0]['AGE']

    # 공연 가져오는 함수 수행(DB 쿼리 후 없으면 에러 있으면 리턴)
    re = getPerformanceByID(pId)

    # 공연장 Assign 여부 확인
    price = re[0]['PRICE']
    hallId = re[0]['CONCERT_HALL_ID']
    if hallId is None:
        IOManager.printError("Not assigned Performance (" + str(aId) + ")")
        return

    # 해당 좌석 예약 여부 확인
    re = DBController.instance().excuteQuery(QUERY.SELECT_RESERVATION_BY_SEATNUMS, pId, seatStr, 'Y')
    if len(re) != 0:
        alreadySeat = []
        for i in re:
            alreadySeat.append(i['SEAT_NO'])
        IOManager.printError("Already reservation seat " + str(alreadySeat))
        return
    
    # 없는 좌석 있는지 확인 (좌석 범위 벗어나는 경우)
    re = DBController.instance().excuteQuery(QUERY.SELECT_RESERVATION_BY_SEATNUMS, pId, seatStr, 'N')
    if len(re) != seatCnt:
        IOManager.printError("Not Exist Seat")
        return

    # 내야할 금액 계산
    discount = 1

    if age <= 7:
        discount = 0
    elif age <= 12:
        discount *= 0.5
    elif age <= 18:
        discount *= 0.8

    price *= discount
    price = round(price)

    # 좌석 예약
    for seatNo in seatStr.split(','):
        # payment 정보 없으니 NULL로 하여 예약 정보 Update
        if DBController.instance().excuteQuery(QUERY.UPDATE_RESERVATION, aId, 'NULL',  price, pId, seatNo) == 0:
            IOManager.printError("Not exist Seat")
            return

    print("Successfully book a performance")

    # 좌석 수 곱하여 총 가격 출력
    price *= seatCnt
    print("Total ticket price is " + str(price))


# 12번 선택 시 : 공연장에 배정된 공연 목록 출력
def print_all_performances_which_assigned_at_a_building():
    # 필요 정보 입력
    bId = IOManager.input("Building ID: ", inputType=INPUT_TYPE.INT, minvalue=1)

    # 콘서트 홀(Building), 예약정보 가져와서 출력 / 없는 경우 에러 출력
    re = DBController.instance().excuteQuery(QUERY.SELECT_CONCERT_BY_HALL_ID, bId)
    if len(re) == 0:
        IOManager.printError("Not Exist building")
        return
    IOManager.printTable(re)


# 13번 선택 시 : 공연을 예매한 관객 정보 출력
def print_all_audiences_who_booked_for_a_performance():
    # 필요 정보 입력
    pId = IOManager.input("Performance ID: ", inputType=INPUT_TYPE.INT, minvalue=1)

    # 공연 정보 받아옴
    re = DBController.instance().excuteQuery(QUERY.SELECT_CONCERT_BY_ID, pId)

    # 공연 없는 경우 에러 출력
    if len(re) == 0:
        IOManager.printError("Not Exist Performance (" + str(pId) + ")")
    else:
        # 공연 예매한 관객 정보 쿼리 수행 후 결과 출력
        re = DBController.instance().excuteQuery(QUERY.SELECT_AUDIENCE_BY_CONCERT_ID, pId)
        IOManager.printTable(re)


# 14번 선택 시
def print_ticket_booking_status_of_a_performance():
    # 필요 정보 입력
    pId = IOManager.input("Performance ID: ", inputType=INPUT_TYPE.INT, minvalue=1)

    # 공연 가져오는 함수 수행(DB 쿼리 후 없으면 에러 있으면 리턴)
    re = getPerformanceByID(pId)
    assign = re[0]['CONCERT_HALL_ID']

    # Assign된 공연이 없는 경우
    if assign is None:
        IOManager.printError("Not assigned performance (" + str(pId) + " > " + str(assign) + ")")
        return

    # 예약 정보 쿼리 수행 후 결과 출력
    re = DBController.instance().excuteQuery(QUERY.SELECT_RESERVATION_BY_CONCERT_ID, pId)
    IOManager.printTable(re)


# 15번 선택 시 : 프로그램 종료
def exit():
    print("Bye!")
    sys.exit()


# 16번 선택 시 : 데이터베이스 리셋 및 생성
def reset_database():
    # reset 여부 확인
    reset = IOManager.input("Do you really want to reset database? : ")
    if reset.lower() == 'y':
        # 테이블이 있을 경우 drop
        if DBController.instance().excuteQuery(QUERY.SHOW_TABLES) > 0:
            DBController.instance().excuteQuery(QUERY.DROP_TABLES)

        # 테이블이 재생성
        DBController.instance().excuteQuery(QUERY.CREATE_TABLES)
        print("Database is successfully reset")
    return None


# 18번 선택 시 : 공연별 예매 정보 및 가격정보 출력
def print_ticket_booking_status_and_sales_of_a_performance():
    # 필요 정보 입력
    pId = IOManager.input("Performance ID: ", inputType=INPUT_TYPE.INT, minvalue=1)

    # 공연 가져오는 함수 수행(DB 쿼리 후 없으면 에러 있으면 리턴)
    re = getPerformanceByID(pId)
    assign = re[0]['CONCERT_HALL_ID']

    if assign is None:
        IOManager.printError("Not assigned performance (" + str(pId) + " > " + str(assign) + ")")
        return

    re = DBController.instance().excuteQuery(QUERY.SELECT_TICKET_BOOKING_STATUS, pId)
    IOManager.printTable(re)


# 17번 선택 시 : Payment 지정하여 예매
def book_a_performance_with_a_specific_payment_method_extend():
    # 필요 정보 입력
    pId = IOManager.input("Performance ID: ", inputType=INPUT_TYPE.INT, minvalue=1)
    aId = IOManager.input("Audience ID: ", inputType=INPUT_TYPE.INT, minvalue=1)
    seatStr, seatCnt = IOManager.input("seat number: ", inputType=INPUT_TYPE.SEAT, minvalue=1)
    payment = IOManager.input("Payment: ", inputType=INPUT_TYPE.PAYMENT)

    # 관객 ID 여부 확인
    re = DBController.instance().excuteQuery(QUERY.SELECT_AUDIENCE_BY_ID, aId)

    if len(re) == 0:
        IOManager.printError("Not Exist Audience (" + str(aId) + ")")
        return

    age = re[0]['AGE']

    # 공연 가져오는 함수 수행(DB 쿼리 후 없으면 에러 있으면 리턴)
    re = getPerformanceByID(pId)

    # 공연장 Assign 여부 확인
    price = re[0]['PRICE']
    hallId = re[0]['CONCERT_HALL_ID']
    if hallId is None:
        IOManager.printError("Not assigned Performance (" + str(aId) + ")")
        return

    # 해당 좌석 예약 여부 확인
    re = DBController.instance().excuteQuery(QUERY.SELECT_RESERVATION_BY_SEATNUMS, pId, seatStr, 'Y')
    if len(re) != 0:
        alreadySeat = []
        for i in re:
            alreadySeat.append(i['SEAT_NO'])
        IOManager.printError("Already reservation seat " + str(alreadySeat))
        return

    # 없는 좌석 있는지 확인
    re = DBController.instance().excuteQuery(QUERY.SELECT_RESERVATION_BY_SEATNUMS, pId, seatStr, 'N')
    if len(re) != seatCnt:
        IOManager.printError("Not Exist Seat")
        return

    # 내야할 금액 계산
    discount = 1

    if age <= 7:
        discount = 0
    elif age <= 12:
        discount *= 0.5
    elif age <= 18:
        discount *= 0.8

    if payment == PAYMENT_TYPE.CARD_HYUNDAI.value:
        discount *= 0.6
    elif payment == PAYMENT_TYPE.CARD_SAMSUNG.value:
        discount *= 0.5
    elif payment == PAYMENT_TYPE.DEPOSIT.value or payment == PAYMENT_TYPE.CASH.value:
        discount *= 0.95
    price *= discount
    price = round(price)

    # 좌석 예약
    for seatNo in seatStr.split(','):
        if DBController.instance().excuteQuery(QUERY.UPDATE_RESERVATION, aId, payment,  price, pId, seatNo) == 0:
            IOManager.printError("Not exist Seat")
            return

    print("Successfully book a performance")

    # 좌석 수 곱하여 총 가격 출력
    price *= seatCnt

    # 할인률 계산 100단위로
    discount = 1 - discount
    discount *= 100

    strDiscount = str(round(discount, 1))

    # 끝자리 0인경우 삭제 ex) 10.0 -> 10
    split = strDiscount.split('.')
    if len(split) > 1 and split[1] == '0':
        strDiscount = split[0]

    print("Total ticket price is " + str(price) + " (" + strDiscount + "% discount)")


# 18번 선택 시 : 가격 정보 포함하여 예매 정보 출력
def print_ticket_booking_status_and_sales_of_a_performance_extend():
    # 필요 정보 입력
    pId = IOManager.input("Performance ID: ", inputType=INPUT_TYPE.INT, minvalue=1)

    # 공연 가져오는 함수 수행(DB 쿼리 후 없으면 에러 있으면 리턴)
    re = getPerformanceByID(pId)
    assign = re[0]['CONCERT_HALL_ID']

    if assign is None:
        IOManager.printError("Not assigned performance (" + str(pId) + " > " + str(assign) + ")")
        return

    re = DBController.instance().excuteQuery(QUERY.SELECT_TICKET_BOOKING_STATUS, pId)
    IOManager.printTable(re)


# 공연 정보 가져오고 없으면 에러 발생
def getPerformanceByID(pId):
    re = DBController.instance().excuteQuery(QUERY.SELECT_CONCERT_BY_ID, pId)
    if len(re) == 0:
        raise EnvironmentError("Not Exist Performance (" + str(pId) + ")")
    return re

