from MainController import *


# main 으로 돌아가게 되는 함수
def main():
    # 메뉴 출력
    IOManager.printMenu()

    # 참고용 함수
    #test()

    # main loop
    while True:
        try:
            # 메뉴 사용자 input
            sel = IOManager.getMenuInput()
            # 사용자 input 한 menu 명의 함수를 실행(띄어쓰기를 '_' 로 변환
            funcName = MENU_STRING[sel - 1].replace(" ", "_")
            funcName = funcName.replace("(", "")
            funcName = funcName.replace(")", "")
            eval(funcName + "()")
        except Exception as e:
            # 각종 에러 발생 시 Error String 출력
            IOManager.printError(str(e))


if __name__ == '__main__':
    main()
