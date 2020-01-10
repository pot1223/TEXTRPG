
for n in range(1):
    import random
    Men = ["아이즈원 최예나", "아이유", "레드벨벳 아이린", "여자친구 은하", "ITZY 예지", "트와이스 다현" ]
    Women=["BTS 뷔","EXO 찬열 ", "정성모", "BTS 진","AB6IX 이대휘"]
    random.shuffle(Men)
    random.shuffle(Women)
    f = []
    def ideal_type():
        if len(a)%2 == 0:
            loop = len(a) // 2
            for i in range(0, loop):
                while True:
                    if loop == 1:
                        print("<< 준결승 >>n")
                    else:
                        print("<< 제 %d 강 >> " %(2**loop))
                    print("%s vs %s" %(a[i], a[i+1]))
                    print("앞사람이 맘에 들면 1번을, 뒷사람이 맘에들면 2번을 입력")
                    print("n 입력:", end = ' ')
                    temp = int(input())
                    print()
                    if temp == 1:
                        a.remove(a[i+1])
                        break
                    elif temp == 2:
                        a.remove(a[i])
                        break
                    else:
                        print("잘못 입력하셨습니다. 다시 입력하세요.")
                        print()
        elif len(a)%2 != 0:
            workover = a[-1]
            a.remove(a[-1])
            loop = len(a) // 2
            for i in range(0, loop):
                while True:
                    if loop == 1:
                        print("<< 준결승 >>n")
                    else:
                        print("<< 제 %d 강 >>n " %(2**loop))
                    print("%s vs %s" %(a[i], a[i+1]))
                    print("앞사람이 맘에 들면 1번을, 뒷사람이 맘에들면 2번을 입력")
                    print("n 입력:", end = ' ')
                    temp = int(input())
                    print()
                    if temp == 1:
                        a.remove(a[i+1])
                        break
                    elif temp == 2:
                        a.remove(a[i])
                        break
                    else:
                        print("잘못 입력하셨습니다. 다시 입력하세요.")
                        print()
            a.append(workover)
    while True:
        print("원하는 점심상대가 남자라면 1번을, 여자라면 2번을 입력하세요.")
        print("n 입력:", end = ' ')
        c = int(input())
        print()
        if c == 1:
            a = Women[:]
            break
        elif c == 2:
            a = Men[:]
            break
        else:
            print("잘못 입력하셨습니다. 다시 입력하세요.")

    while len(a) != 1:
        ideal_type()
    print("당신의 점심상대는", a[0], "입니다")