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
    re = DBController.instance().excuteQuery(QUERY.SELECT_CONCERT)
    # 출력은 이렇게... 리턴받은 객체를 넘겨주세요
    PrintManager.instance().printTable(re)

    print()
    # 파라미터가 2개인 쿼리 수행  query.xml의  SELECT_PERFORMANCE 참고
    re = DBController.instance().excuteQuery(QUERY.SELECT_PERFORMANCE, '1', 1)
    # 출력은 이렇게... 리턴받은 객체를 넘겨주세요
    PrintManager.instance().printTable(re)

    # 에러 출력 예시
    PrintManager.instance().printError("에러는 이렇게 출력하세요")



# 1번 선택 시
def print_all_buildings():
    re = DBController.instance().excuteQuery(QUERY.SELECT_CONCERT_HALL)
    PrintManager.instance().printTable(re)
    return None


# 2번 선택 시
def print_all_performances():
    return None


# 3번 선택 시
def print_all_audiences():
    return None


# 4번 선택 시
def insert_a_new_building():
    return None


# 5번 선택 시
def remove_a_building():
    return None


# 6번 선택 시
def insert_a_new_performance():
    return None


# 7번 선택 시
def remove_a_performance():
    return None


# 8번 선택 시
def insert_a_new_audience():
    return None


# 9번 선택 시
def remove_an_audience():
    return None


# 10번 선택 시
def assign_a_performance_to_a_building():
    return None


# 11번 선택 시
def book_a_performance():
    return None


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

