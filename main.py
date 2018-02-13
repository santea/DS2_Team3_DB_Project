from MainController import *


# main 으로 돌아가게 되는 함수
def main():
    # 메뉴 출력
    IOManager.printMenu()

    # 참고용 함수
    test()

    # main loop
    while True:
        try:
            sel = IOManager.getMenuInput()
            eval(MENU_STRING[sel - 1].replace(" ", "_") + "()")
        except Exception as e:
            IOManager.printError(str(e))


if __name__ == '__main__':
    main()
