from enum import Enum


# 디버그 모드 설정 : True 시 쿼리 / 결과 출력
IS_DEBUG_MODE = True

# 쿼리 종류  쿼리 추가시 여기와 query.xml에 추가
class QUERY(Enum):
    SELECT_CONCERT_HALL = 1
    SELECT_CONCERT = 2
    SELECT_AUDIENCES = 3
    INSERT_CONCERT_HALL = 4
    DELETE_CONCERT_HALL = 5
    INSERT_CONCERT = 6
    DELETE_CONCERT = 7
    INSERT_AUDIENCE = 8
    UPDATE_PCONCERT = 9
    SELECT_PERFORMANCE = 10
    DROP_TEST = 11
    CREATE_TABLES = 12