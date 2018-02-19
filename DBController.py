import pymysql.cursors
from IOManager import IOManager
from xml.etree.ElementTree import parse
from Constant import IS_DEBUG_MODE


class DBController:
    __instance = None

    # Singleton 객체로 구현
    @classmethod
    def __getInstance(cls):
        return cls.__instance

    # Singleton 객체로 구현
    @classmethod
    def instance(cls, *args, **kargs):
        cls.__instance = cls(*args, **kargs)
        cls.instance = cls.__getInstance
        return cls.__instance

    def __init__(self):
        return None

    # DB 연결 후 연결객체 리턴
    def getConnection(self):
        try:
            con = pymysql.connect(host='147.46.215.246',
                                  port=33060,
                                  user='akirus82@naver.com',
                                  password='dbintrodb',
                                  db='db_kimbyeongsu',
                                  charset='utf8',
                                  autocommit=True,
                                  cursorclass=pymysql.cursors.DictCursor)
        except Exception as e:
            IOManager.printExcept(e)

        return con

    # 쿼리 를 수행함
    # queryType : CONSTANT에 정의된 쿼리 타입
    # *param : 쿼리에 들어가는 파라미터 들
    def excuteQuery(self, queryType, *param):
        # 연결 및 연결객체 가져옴
        connection = self.getConnection()
        result = None

        if connection is None:
            return None

        try:
            # 커서 획득
            with connection.cursor() as cursor:
                # query.xml에서 정의된 쿼리 가져옴 / param 넘겨온 정보로 붙여서 쿼리를 만듬
                sql = self.__readQueryFromXml(queryType) % param

                # 쿼리가 여러개인 경우 ; 로 나눠서 수행
                splitSql = sql.split(";")

                if IS_DEBUG_MODE:
                    print("query >", sql)

                for i in range(len(splitSql)):
                    if splitSql[i].strip() == "":
                        break
                    # 쿼리 수행
                    cursor.execute(splitSql[i])

                    if "insert" in splitSql[i] or "update" in splitSql[i] or "delete" in splitSql[i] or "show" in splitSql[i]:
                        # insert update delete 쿼리는 수행후 row count 리턴
                        result = cursor.rowcount
                    else:
                        # select 는 결과 리턴
                        result = cursor.fetchall()

                if IS_DEBUG_MODE:
                    print("result >", result)
        except Exception as e:
            IOManager.printExcept(e)
        finally:
            connection.close()

        return result

    # 쿼리타입을 받아서 query.xml에서 쿼리를 읽어오는 함수
    def __readQueryFromXml(self, queryType):
        tree = parse("query.xml")
        query = tree.getroot()
        element = query.find(queryType.name)
        # 정의된 쿼리가 없는경우 에러 출력
        if element is None or element.text == "":
            IOManager.printError("Can not find " + queryType.name + " from query.xml")
            return None
        # 쿼리가 있는 경우 쿼리 텍스트 리턴
        return element.text
