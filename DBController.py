import pymysql.cursors
from PrintManager import PrintManager
from xml.etree.ElementTree import parse
from Constant import IS_DEBUG_MODE


class DBController:
    __instance = None

    @classmethod
    def __getInstance(cls):
        return cls.__instance

    @classmethod
    def instance(cls, *args, **kargs):
        cls.__instance = cls(*args, **kargs)
        cls.instance = cls.__getInstance
        return cls.__instance

    def __init__(self):
        return None

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
            PrintManager.printExcept(e)

        return con

    def excuteQuery(self, queryType, *param):
        connection = self.getConnection()
        result = None

        if connection is None:
            return None

        try:
            with connection.cursor() as cursor:

                sql = self.__readQueryFromXml(queryType) % param
                splitSql = sql.split(";")

                if IS_DEBUG_MODE:
                    print("query >", sql)

                for i in range(len(splitSql)):
                    if splitSql[i].strip() == "":
                        break
                    cursor.execute(splitSql[i])

                    if "insert" in splitSql[i] or "update" in splitSql[i] or "delete" in splitSql[i]:
                        # insert update delete 쿼리는 수행후 row count 리턴
                        result = cursor.rowcount
                    else:
                        # select 는 결과 리턴
                        result = cursor.fetchall()

                if IS_DEBUG_MODE:
                    print("result >", result)
        except Exception as e:
            PrintManager.printExcept(e)
        finally:
            connection.close()

        return result

    def __readQueryFromXml(self, queryType):
        tree = parse("query.xml")
        query = tree.getroot()
        element = query.find(queryType.name)
        if element is None or element.text == "":
            PrintManager.printError(queryType.name + "를 query.xml 파일에서 찾지 못함 확인해주세요")
            return None
        return element.text
