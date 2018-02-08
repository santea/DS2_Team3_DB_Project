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
                                  user='santea32@gmail.com',
                                  password='qwer43qwer!',
                                  db='db_kimseontae',
                                  charset='utf8',
                                  cursorclass=pymysql.cursors.DictCursor)
        except Exception as e:
            PrintManager.instance().printExcept(e)

        return con

    def excuteQuery(self, queryType, *param):
        connection = self.getConnection()
        result = None

        if connection is None:
            return None

        try:
            with connection.cursor() as cursor:
                sql = self.__readQueryFromXml(queryType) % param
                if IS_DEBUG_MODE:
                    print("query >", sql)
                cursor.execute(sql)

                result = cursor.fetchall()
                if IS_DEBUG_MODE:
                    print("result >", result)
        except Exception as e:
            PrintManager.instance().printExcept(e)
        finally:
            connection.close()
        return result

    def __readQueryFromXml(self, queryType):
        tree = parse("query.xml")
        query = tree.getroot()
        element = query.find(queryType.name)
        if element is None or element.text == "":
            PrintManager.instance().printError(queryType.name + "를 query.xml 파일에서 찾지 못함 확인해주세요")
            return None
        return element.text
