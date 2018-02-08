import MainController
import sys, os
from prettytable import PrettyTable
from colorama import Fore, Style


class PrintManager:
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

    def printMenu(self):
        print("=============================================")
        for i in range(len(MainController.MENU_STRING)):
            print(str(i + 1) + "." + MainController.MENU_STRING[i])

    def getMenuInput(self):
        inTxt = input("\nSelect your action: ")
        try:
            inNum = int(inTxt)
            if inNum < 1 or inNum > 16:
                raise ()
        except:
            self.printError("1~16사이의 숫자만 입력 해 주세요.")
            return self.getMenuInput()
        return inNum

    # 쿼리한 결과를 테이블 형태로 출력 (Dic이 리스트로 되어있는 자료형)
    def printTable(self, obj):
        if len(obj) > 0:
            # table 헤더 설정
            table = PrettyTable(list(obj[0].keys()))
            # table 행 입력
            for i in range(len(obj)):
                # None 을 빈 문자열로 교환
                val = list(map(lambda x: "" if x is None else x, obj[i].values()))
                table.add_row(val)

            # table 출력 (초록색)
            print(f"{Fore.GREEN}")
            print(table, f"{Style.RESET_ALL}")

    # Except 발생시 정보 출력
    def printExcept(self, e):
        exc_type, exc_obj, exc_tb = sys.exc_info()
        fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]

        print(f"{Fore.RED}[Error] " + fname + " (line : " + str(exc_tb.tb_lineno) + ") : ", e, f"{Style.RESET_ALL}")

    def printError(self, msg):
        print(f"{Fore.RED}[Error] " + msg + f"{Style.RESET_ALL}")
