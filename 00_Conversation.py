import time


# TODO : Introduction
def intro():
    line = "\n--------------------------------------------\n"

    print("Welcome! This is pirogramming.\n반갑습니다. 여기는 <피로한 피로그래밍 (12기 ver.)>입니다.")

    time.sleep(2)
    name = input("\n성모: 안녕하세요! 만나서 반갑습니다. 이름이 무엇인가요?")
    print("{0}: {0}".format(name))

    time.sleep(1)
    answer = input('\n성모: 안녕하세요, {}님! 피로그래밍은 정말 피로한 게임입니다. 준비되셨나요?'.format(name))
    print("{}: {}".format(name, answer))
    time.sleep(1)
    print("성모: 좋습니다. 그럼 조금 후에 뵙겠습니다.")

    time.sleep(2)
    print(line)
    print("{}님, 환영합니다.\n<피로한 피로그래밍 (12기 ver.)> 게임을 시작합니다.\n\nloading...".format(name))
    print(line)

    time.sleep(2)
    print("\n성모에게서 문자가 왔습니다.\n\n")

    time.sleep(2)
    print("                   정성모")
    print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
    time.sleep(1)
    print("                 문자 메시지")
    print("              (오늘) 오후 11:10")
    print("  ┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓")
    print("  ┃")
    print("  ┃  안녕하세요, {}님!".format(name))
    print("  ┃  축하드립니다.")
    print("  ┃  피로그래밍 12기에 합격하셨습니다.")
    print("  ┃  유노윤호의 열정을 보여주세요!")
    print(" ᐸ")
    print("  ┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛")

    time.sleep(2)
    print("\n\n피로그래밍에 합격했네요.")
    time.sleep(2)
    print("그러나 두 달 동안 피로그래밍에서 살아남는 것은 쉽지 않습니다.")
    time.sleep(2)
    print("12기 퀘스트를 모두 완수하고 진정한 피로그래머에 도전하세요.")


# TODO : Conclusion
def conclusion():
    line = "\n--------------------------------------------\n"

    print(line)
    print("12기의 모든 퀘스트를 완수했습니다!")
    print("성모가 흐뭇한 표정으로 걸어옵니다.")
    print(line)

    time.sleep(2)
    print("성모: 수고하셨습니다. 당신은 이제 진정한 피로그래머입니다.")
    time.sleep(2)
    print("성모: 앞으로 있을 모든 피로그래밍 활동에서")
    time.sleep(2)
    print("성모: 유노윤호한 모습 계속 보여주시길 기대합니다.")

    time.sleep(2)
    print(line)
    print("<피로한 피로그래밍 (12기 ver.)> 게임을 종료합니다.")
    print("<피로한 피로그래밍 (13기 운영진 ver.)>은 2020년 6월에 출시됩니다.")
    print(line)

intro()
conclusion()