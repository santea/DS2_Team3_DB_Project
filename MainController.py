import sys
from DBController import DBController
from Constant import QUERY, INPUT_TYPE
from PrintManager import PrintManager


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
               "reset database"]


# 테스트 함수입니다!! 참고용...
def test():
    # Constant 파일의 DEBUG모드 있어요! True 하면 쿼리 sql이랑 결과 프린트 하게 해놨어요
    
    print()
    # 파라미터가 0개인 쿼리 수행  query.xml의  SELECT_BUILDING 참고
    re = DBController.instance().excuteQuery(QUERY.SELECT_CONCERT_HALL)
    # 출력은 이렇게... 리턴받은 객체를 넘겨주세요
    PrintManager.printTable(re)

    print()
    # 파라미터가 2개인 쿼리 수행  query.xml의  SELECT_PERFORMANCE 참고
    re = DBController.instance().excuteQuery(QUERY.SELECT_CONCERT, '1', 1)
    # 출력은 이렇게... 리턴받은 객체를 넘겨주세요
    PrintManager.printTable(re)

    # 에러 출력 예시
    PrintManager.printError("에러는 이렇게 출력하세요")


# 1번 선택 시
def print_all_buildings():
    re = DBController.instance().excuteQuery(QUERY.SELECT_CONCERT_HALL)
    PrintManager.printTable(re)


# 2번 선택 시
def print_all_performances():
    re = DBController.instance().excuteQuery(QUERY.SELECT_CONCERT)
    PrintManager.printTable(re)


# 3번 선택 시
def print_all_audiences():
    re = DBController.instance().excuteQuery(QUERY.SELECT_AUDIENCES)
    PrintManager.printTable(re)


# 4번 선택 시
def insert_a_new_building():
    name = PrintManager.input("Building name: ")
    loc = PrintManager.input("Building location: ")
    cap = PrintManager.input("Building capacity: ", inputType=INPUT_TYPE.INT)

    if DBController.instance().excuteQuery(QUERY.INSERT_CONCERT_HALL, name, loc, cap) == 1:
        print("A building is successfully inserted")


# 5번 선택 시
def remove_a_building():
    id = PrintManager.input("Buinding ID: ")

    if DBController.instance().excuteQuery(QUERY.DELETE_CONCERT_HALL, id) == 0:
        PrintManager.printError("Not Exist ConcertHall (" + id + ")")
    else:
        print("A building is successfully removed")


# 6번 선택 시
def insert_a_new_performance():
    name = PrintManager.input("Performance name: ")
    typ = PrintManager.input("Performance type: ")
    price = PrintManager.input("Performance price: ", inputType=INPUT_TYPE.INT)
    if DBController.instance().excuteQuery(QUERY.INSERT_CONCERT, name, typ, price) == 1:
        print("A performance is successfully inserted")


# 7번 선택 시
def remove_a_performance():
    id = PrintManager.input("Performance ID: ")
    if DBController.instance().excuteQuery(QUERY.DELETE_CONCERT, id) == 0:
        PrintManager.printError("Not Exist Performance (" + id + ")")
    else:
        print("A performance is successfully removed")


# 8번 선택 시
def insert_a_new_audience():
    name = PrintManager.input("Audience name: ")
    gender = PrintManager.input("Audience gender: ", inputType=INPUT_TYPE.GENDER)
    price = PrintManager.input("Audience age: ", INPUT_TYPE.INT)
    if DBController.instance().excuteQuery(QUERY.INSERT_AUDIENCE, name, gender, price) == 1:
        print("A audience is successfully inserted")


# 9번 선택 시
def remove_an_audience():
    id = PrintManager.input("Audience ID: ")
    if DBController.instance().excuteQuery(QUERY.DELETE_AUDIENCE, id) == 0:
        PrintManager.printError("Not Exist audience (" + id + ")")
    else:
        print("A audience is successfully removed")


# 10번 선택 시
def assign_a_performance_to_a_building():
    bId = PrintManager.input("Building ID: ")
    pId = PrintManager.input("Performance ID: ")
    if DBController.instance().excuteQuery(QUERY.UPDATE_PCONCERT, bId, pId) == 2:
        print("A performance is successfully assigned")


# 11번 선택 시
def book_a_performance():
    pId = PrintManager.input("Performance ID: ")
    aId = PrintManager.input("Audience ID: ")
    splitSeat = PrintManager.input("seat number: ", INPUT_TYPE.SEAT)

    #자리 있는지 검사하는 부분 들어가야함

    for i in range(len(splitSeat)):
        DBController.instance().excuteQuery(QUERY.INSERT_RESERVATION, pId, aId, splitSeat[i])


# 12번 선택 시
def print_all_performances_which_assigned_at_a_building():
    return None


# 13번 선택 시
def print_all_audiences_who_booked_for_a_performance():
    return None


# 14번 선택 시
def print_ticket_booking_status_of_a_performance():
    return None


# 15번 선택 시 : 프로그램 종료
def exit():
    print("Bye!!!")
    sys.exit()


# 16번 선택 시 : 데이터베이스 리셋 및 생성
def reset_database():
    DBController.instance().excuteQuery(QUERY.DROP_TEST)
    DBController.instance().excuteQuery(QUERY.CREATE_TABLES)
    return None

