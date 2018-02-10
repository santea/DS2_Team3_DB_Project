from enum import Enum


# 디버그 모드 설정 : True 시 쿼리 / 결과 출력
IS_DEBUG_MODE = True

# 입력창 입력 타입 종류
class INPUT_TYPE(Enum):
    STR = 1
    INT = 2
    GENDER = 3
    SEAT = 4

# 쿼리 종류  쿼리 추가시 여기와 query.xml에 추가
class QUERY(Enum):
    SELECT_CONCERT_HALL = 1
    SELECT_CONCERT = 2
    SELECT_AUDIENCE = 3
    INSERT_CONCERT_HALL = 4
    DELETE_CONCERT_HALL = 5
    INSERT_CONCERT = 6
    DELETE_CONCERT = 7
    INSERT_AUDIENCE = 8
    DELETE_AUDIENCE = 9
    UPDATE_CONCERT_CONCERT_HALL_ID = 10
    SELECT_PERFORMANCE = 11
    UPDATE_RESERVATION = 13
    INSERT_RESERVATION = 14
    SELECT_AUDIENCE_BY_CONCERT_ID = 15
    SELECT_RESERVATION_BY_SEATNUMS = 16
    SHOW_TABLES = 17
    DROP_TABLES = 18
    CREATE_TABLES = 19
    SELECT_CONCERT_BY_ID = 20
    SELECT_CONCERT_HALL_BY_CONCERT_ID = 21
    SELECT_CONCERT_HALL_BY_ID = 22
    SELECT_AUDIENCE_BY_ID = 23
    SELECT_CONCERT_BY_HALL_ID = 24
    SELECT_RESERVATION_BY_CONCERT_ID = 25
