from enum import Enum


# 디버그 모드 설정 : True 시 쿼리 / 결과 출력
IS_DEBUG_MODE = True

# 쿼리 종류  쿼리 추가시 여기와 query.xml에 추가
class QUERY(Enum):
    SELECT_BUILDING = 1
    SELECT_PERFORMANCE = 2
    SELECT_AUDIENCES = 3
    INSERT_BUILDING = 4
    DELETE_BUILDING = 5
    INSERT_PERFORMANCE = 6
    DELETE_PERFORMANCE = 7
    INSERT_AUDIENCE = 8
    UPDATE_PERFORMANCE = 9