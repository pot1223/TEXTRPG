# TODO : lesson

import time
import introduction

line = "\n--------------------------------------------\n"

print(line)
print("두 시가 되었습니다.")
print(line)

time.sleep(2)
print("성모: 점심시간이 끝났습니다.")
time.sleep(2)
print("성모: 이제 남은 인강을 들어주세요.")

time.sleep(2)
print(line)
print("그러나 배는 너무 부르고, 인강은 너무 지루합니다.")
print("인강을 듣는 척 성모의 눈을 속이면서 유투브를 보세요!")
print(line)

def lunch():
    time.sleep(2)
    print("성모: 여러분 다들 인강은 잘 듣고 계신가요?")
    time.sleep(2)
    print("\n성모가 확인 질문을 던졌습니다. 대답을 골라주세요.\n")
    time.sleep(1)
    a1_1 = "네, 당연하죠!"
    a1_2 = "아뇨, 유투브를 보고 있어요."
    print("1. {}\n2. {}".format(a1_1, a1_2))
    a1 = int(input())

    if a1 == 1:
        print("{}: {}".format(introduction.name, a1_1))
        time.sleep(2)
        print("\n성모: 네, 좋습니다. 계속 들어주세요.")
        time.sleep(2)
        print("\n성모가 속았습니다! 유투브를 계속 합니다.")
    elif a1 == 2:
        print("{}: {}".format(introduction.name, a1_2))
        time.sleep(2)
        print("\n성모: 유투브를 보셨다구요? 실망이네요.")
        time.sleep(2)
        print("\n성모가 실망했습니다. 피로그래밍에서 제명당할 위기입니다.")
        time.sleep(2)
        print("응답을 다시 선택해주세요.")
        lunch()

    time.sleep(2)
    print(line)

    print("성모: 여러분, 강의 몇 강까지 들으셨나요?")
    time.sleep(2)
    print("\n이런! 성모가 진도를 물어봅니다.")
    time.sleep(2)
    print("그러나 다행히 아무도 대답을 하지 않습니다.")
    time.sleep(2)
    print("\n성모: 음...그럼 20강 중에 3강보다 적게 들었다.")
    time.sleep(2)
    print("\n그러나 성모는 피로그래밍 회장입니다.")
    time.sleep(2)
    print("역시나 쉽게 포기하지 않는군요.")

    time.sleep(2)
    print("\n유투브를 하느라 인강을 듣지 않았으니, 눈치껏 대답해야 합니다. 손을 들까요?\n")
    a2_1 = "손을 든다"
    a2_2 = "손을 들지 않는다"
    time.sleep(1)
    print("1. {}\n2. {}".format(a2_1, a2_2))
    a2 = int(input())

    if a2 == 1:
        print("{}: ({})".format(introduction.name, a2_1))
        time.sleep(2)
        print("\n성모: 4시간 동안 3강도 못 들었다구요? 실망이네요.")
        time.sleep(2)
        print("\n성모가 실망했습니다. 피로그래밍에서 제명당할 위기입니다.")

        time.sleep(2)
        print("\n피로그래밍에서 살아남기 위해 빠르게 변명을 해야합니다.\n")
        a2_1_1 = "집에 가서 다 들어올게요."
        a2_1_2 = "오늘 밤 새겠습니다."
        time.sleep(1)
        print("1. {}\n2. {}".format(a2_1_1, a2_1_2))
        a2_1_0 = int(input())

        if a2_1_0 == 1:
            print("{}: {}".format(introduction.name, a2_1_1))
        elif a2_1_0 == 2:
            print("{}: {}".format(introduction.name, a2_1_2))

        time.sleep(2)
        print("\n성모: 좋습니다. 그런 열정, 아주 피로그래머다운 모습입니다.")
        time.sleep(2)
        print("\n성모가 감동했습니다.")

    elif a2 == 2:
        print("{}: ({})".format(introduction.name, a2_2))
        time.sleep(2)
        print("\n성모: 음...그럼 10강보다 적게 들었다.")
        time.sleep(2)
        print("\n손을 들까요?\n")
        time.sleep(1)
        print("1. {}\n2. {}".format(a2_1, a2_2))
        a2_2 = int(input())

        if a2_2 == 1:
            print("{}: ({})".format(introduction.name, a2_1))
            time.sleep(2)
            print("\n성모: 좋습니다. 수고하셨습니다. 이제 집에 가시면 됩니다.")
        elif a2_2 == 2:
            #print("{}: ({})".format(introduction.name, a2_2))
            time.sleep(2)
            print("\n성모: 오..그럼 10강 이상 들으신 건가요?")
            time.sleep(2)
            print("\n성모: 너무 좋습니다. 이제 집에 가시면 됩니다.")

    time.sleep(2)
    print(line)
    print("성공입니다! 성모를 완벽하게 속였습니다.")
    print(line)

lunch()