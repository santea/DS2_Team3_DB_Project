from MainController import *


# main 으로 돌아가게 되는 함수
def main():
    # 메뉴 출력
    PrintManager.printMenu()

    # github test111
    # github test 222

    # github test1112222

    # 참고용 함수
    test()

    # main loop
    while True:
        try:
            sel = PrintManager.getMenuInput()
            eval(MENU_STRING[sel - 1].replace(" ", "_") + "()")
        except Exception as e:
            PrintManager.printError(str(e))


if __name__ == '__main__':
    main()
