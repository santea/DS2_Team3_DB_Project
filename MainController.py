import sys
from DBController import DBController
from Constant import QUERY
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
    PrintManager.instance().printTable(re)

    print()
    # 파라미터가 2개인 쿼리 수행  query.xml의  SELECT_PERFORMANCE 참고
    re = DBController.instance().excuteQuery(QUERY.SELECT_CONCERT, '1', 1)
    # 출력은 이렇게... 리턴받은 객체를 넘겨주세요
    PrintManager.instance().printTable(re)

    # 에러 출력 예시
    PrintManager.instance().printError("에러는 이렇게 출력하세요")



# 1번 선택 시
def print_all_buildings():
    re = DBController.instance().excuteQuery(QUERY.SELECT_CONCERT_HALL)
    PrintManager.instance().printTable(re)


# 2번 선택 시
def print_all_performances():
    re = DBController.instance().excuteQuery(QUERY.SELECT_CONCERT)
    PrintManager.instance().printTable(re)


# 3번 선택 시
def print_all_audiences():
    re = DBController.instance().excuteQuery(QUERY.SELECT_AUDIENCES)
    PrintManager.instance().printTable(re)


# 4번 선택 시
def insert_a_new_building():
    name = input("Building name: ")
    loc = input("Building location: ")
    cap = input("Building capacity: ")
    try:
        cap = int(cap)
    except TypeError:
        PrintManager.instance().printError("Please Input number (capacity)")
        return
    DBController.instance().excuteQuery(QUERY.INSERT_CONCERT_HALL, name, loc, cap)
    print("A building is successfully inserted")


# 5번 선택 시
def remove_a_building():
    id = input("ConcertHall ID: ")

    re = DBController.instance().excuteQuery(QUERY.SELECT_CONCERT_BY_CONCERTHALL_ID, id)
    if len(re) == 0:
        PrintManager.instance().printError("Not Exist ConcertHall (" + id + ")")
    else:
        re = DBController.instance().excuteQuery(QUERY.DELETE_CONCERT_HALL, id)


# 6번 선택 시
def insert_a_new_performance():
    name = input("Performance name: ")
    typ = input("Performance type: ")
    price = input("Performance price: ")
    try:
        price = int(price)
    except TypeError:
        PrintManager.instance().printError("Please Input number (price)")
        return
    re = DBController.instance().excuteQuery(QUERY.INSERT_CONCERT, name, typ, price)
    print(re)


# 7번 선택 시
def remove_a_performance():
    id = input("Performance ID: ")
    re = DBController.instance().excuteQuery(QUERY.DELETE_CONCERT, id)
    print(re)


# 8번 선택 시
def insert_a_new_audience():
    name = input("Audience name: ")
    gender = input("Audience gender: ")
    if gender != 'M' or gender != 'F':
        PrintManager.instance().printError("Please input 'M' or 'F' gender")
        return

    price = input("Audience age: ")
    try:
        price = int(price)
    except TypeError:
        PrintManager.instance().printError("Please input number (price)")
        return
    re = DBController.instance().excuteQuery(QUERY.INSERT_AUDIENCE, name, gender, price)
    print(re)


# 9번 선택 시
def remove_an_audience():
    id = input("Audience ID: ")
    re = DBController.instance().excuteQuery(QUERY.DELETE_AUDIENCE, id)
    print(re)


# 10번 선택 시
def assign_a_performance_to_a_building():
    bId = input("Building ID: ")
    pId = input("Performance ID: ")
    re = DBController.instance().excuteQuery(QUERY.UPDATE_PCONCERT, bId, pId)
    print(re)


# 11번 선택 시
def book_a_performance():
    pId = input("Performance ID: ")
    aId = input("Audience ID: ")
    seat = input("seat number: ")
    splitSeat = seat.split(",")

    if len(splitSeat) == 1:
        try:
            seatNum = int(seat)
            re = DBController.instance().excuteQuery(QUERY.INSERT_RESERVATION, pId, aId, seatNum)
        except TypeError:
            PrintManager.instance().printError("Please input number (seat number)")
            return
    else:
        for i in range(len(splitSeat)):
            try:
                seatNum = int(splitSeat[i].replace(" ", ""))
                re = DBController.instance().excuteQuery(QUERY.INSERT_RESERVATION, pId, aId, seatNum)
            except TypeError:
                PrintManager.instance().printError("Please input number (seat number)")
                return


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

