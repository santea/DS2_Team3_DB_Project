import MainController
import sys, os
from prettytable import PrettyTable
from colorama import Fore, Style
from Constant import INPUT_TYPE


class IOManager:
    def __init__(self):
        return None

    @classmethod
    def printMenu(self):
        print("============================================================")
        for i in range(len(MainController.MENU_STRING)):
            print(str(i + 1) + ". " + MainController.MENU_STRING[i])
        print("============================================================")

    @classmethod
    def getMenuInput(self):
        inTxt = input("\nSelect your action: ")
        try:
            inNum = int(inTxt)
            if inNum < 1 or inNum > 16:
                raise ()
        except:
            self.printError("Select your action between 1 and 16")
            return self.getMenuInput()
        return inNum

    # 쿼리한 결과를 테이블 형태로 출력 (Dic이 리스트로 되어있는 자료형)
    @classmethod
    def printTable(self, obj):
        if obj is None or len(obj) == 0:
            self.printError("No result")
        elif len(obj) > 0:
            # table 헤더 설정
            table = PrettyTable(list(obj[0].keys()))
            # table 행 입력
            for i in range(len(obj)):
                # None 을 빈 문자열로 교환
                val = list(map(lambda x: "" if x is None else x, obj[i].values()))
                table.add_row(val)

            # table 출력 (초록색)
            print(f"{Fore.GREEN}")
            table.padding_width = 3
            print(table, f"{Style.RESET_ALL}")

    # Except 발생시 정보 출력
    @classmethod
    def printExcept(self, e):
        exc_type, exc_obj, exc_tb = sys.exc_info()
        fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]

        print(f"{Fore.RED}[Error] " + fname + " (line : " + str(exc_tb.tb_lineno) + ") : ", e, f"{Style.RESET_ALL}")

    @classmethod
    def printError(self, msg):
        print(f"{Fore.RED}[Error] " + msg + f"{Style.RESET_ALL}")

    @classmethod
    def input(self, text, maxLen=200, inputType=INPUT_TYPE.STR, minvalue=0):
        if inputType == INPUT_TYPE.STR:
            inStr = input(text)
            if maxLen <= len(inStr):
                self.printError("Input size error | max :" + str(maxLen) + ", input :" + str(len(inStr)))
                return inStr[:200]
            else:
                return inStr
        elif inputType == INPUT_TYPE.INT:
            inStr = input(text)
            try:
                inInt = int(inStr)
                if inInt < minvalue:
                    raise ValueError("Please input more then " + str(minvalue) + " integer Value")
                return inInt

            except Exception:
                raise ValueError("Please input more then " + str(minvalue) + " integer Value")
        elif inputType == INPUT_TYPE.GENDER:
            inStr = input(text)
            if inStr != 'M' and inStr != 'F':
                raise ValueError("Please input 'M' or 'F'")
            else:
                return inStr
        elif inputType == INPUT_TYPE.SEAT:
            inStr = input(text)
            splitStr = inStr.split(",")
            returnStr = ""
            seatCnt = 0
            for i in range(len(splitStr)):
                try:
                    seatCnt += 1
                    returnStr += splitStr[i]
                    if int(splitStr[i]) < minvalue:
                        raise ValueError
                    if i != len(splitStr) - 1:
                        returnStr += ","

                except ValueError:
                    raise ValueError("Please input more then " + str(minvalue) + " integer Value (Seat Num)")

            return returnStr, seatCnt

        return None
