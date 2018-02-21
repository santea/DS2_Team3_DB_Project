import MainController
import sys, os
from prettytable import PrettyTable
from colorama import Fore, Style
from Constant import INPUT_TYPE, PAYMENT_TYPE


class IOManager:
    def __init__(self):
        return None

    # 메뉴 목록을 출력하는 함수
    @classmethod
    def printMenu(self):
        print("====================================================================")
        for i in range(len(MainController.MENU_STRING)):
            print(str(i + 1) + ". " + MainController.MENU_STRING[i])
        print("====================================================================")


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
        # except 는 에러 코드 라인 정보 출력
        print(f"{Fore.RED}[Error] " + fname + " (line : " + str(exc_tb.tb_lineno) + ") : ", e, f"{Style.RESET_ALL}")

    # 에러 출력시 사용하는 함수 빨간색으로 출력
    @classmethod
    def printError(self, msg):
        print(f"{Fore.RED}[Error] " + msg + f"{Style.RESET_ALL}")

    # 입력 받을때 쓰는 함수 정상적인 경우 필요한 형태로 입력된것을 리턴
    # text : 입력 받을때 띄울 text
    # maxLen : STR일 경우 최대 길이 (기본 200)
    # inputType : input 값의 종류 (기본 STR)
    # minvalue : int 인 경우 최소값 설정 (기본 0)
    @classmethod
    def input(self, text, maxLen=200, inputType=INPUT_TYPE.STR, minvalue=0):
        if inputType == INPUT_TYPE.STR:
            # input type 이 STR인 경우 빈 문자열일 경우 에러 출력 및 input Size 확인하여 maxlen 넘을 경우 maxlen만큼 자름
            inStr = input(text)

            if inStr == "":
                raise ValueError("Please input string")

            if maxLen <= len(inStr):
                self.printError("Input size error | max :" + str(maxLen) + ", input :" + str(len(inStr)))
                return inStr[:maxLen]
            else:
                return inStr
        elif inputType == INPUT_TYPE.INT:
            # input type 이 INT인 경우 int함수를 통해 숫자 입력인지 확인하고 아닐경우 에러 출력 / minvalue값도 체크하여 에러 출력
            inStr = input(text)
            try:
                inInt = int(inStr)
                if inInt < minvalue:
                    raise ValueError("Please input more then " + str(minvalue) + " integer value")
                return inInt

            except Exception:
                raise ValueError("Please input more then " + str(minvalue) + " integer value")
        elif inputType == INPUT_TYPE.GENDER:
            # input type 이 GENDER인 경우 m이나 f (대소문자 구분 x) 아닐경우 에러
            inStr = input(text)
            inStr = inStr.lower()
            if inStr != 'm' and inStr != 'f':
                raise ValueError("Please input 'M' or 'F'")
            else:
                return inStr
        elif inputType == INPUT_TYPE.SEAT:
            # input type 이 SEAT인 경우 빈문자 입력 확인 및 구분자 사이에 숫자 입력 확인 하여 에러 출력
            inStr = input(text)
            splitStr = inStr.split(",")
            returnStr = ""
            seatCnt = 0

            if inStr == "":
                raise ValueError("Please input string")

            for i in range(len(splitStr)):
                try:
                    seatCnt += 1
                    returnStr += splitStr[i]
                    if int(splitStr[i]) < minvalue:
                        raise ValueError
                    if i != len(splitStr) - 1:
                        returnStr += ","

                except ValueError:
                    raise ValueError("Please input more then " + str(minvalue) + " integer value (Seat Num)")

            return returnStr, seatCnt
        elif inputType == INPUT_TYPE.PAYMENT:
            # input type 이 PAYMENT인 경우 빈문자 인지 확인 하고 payment 에 지정된 텍스트인지 확인 하여 에러 출력
            inStr = input(text)
            inStr = inStr.lower()

            if inStr == "":
                raise ValueError("Please input string")

            validation = False

            paymentStr = ""
            for i in list(PAYMENT_TYPE):
                paymentStr += i.value + " "
                if i.value == inStr:
                    validation = True

            if validation == False:
                raise ValueError("Please input (" + paymentStr + ")")
            else:
                return inStr
        elif inputType == INPUT_TYPE.MENU:
            # input type 이 MENU 인 경우 숫자가 아니거나 MENU 범위 벗어난 경우 Error 출력
            inTxt = input(text)
            try:
                inNum = int(inTxt)
                if inNum < 1 or inNum > 18:
                    raise ()
            except:
                self.printError("Select your action between 1 and 18")
                # 에러 발생시 다시 입력받도록 함
                return self.input(text, inputType=INPUT_TYPE.MENU)
            return inNum
        return None
