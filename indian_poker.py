# TODO : Indian Poker

import random
import time


def indian_poker():
    time.sleep(3)
    print("\n인디언 포커를 시작합니다.")
    line = "\n--------------------------------------------\n"

    print(line)
    user = random.randint(1, 10)
    boss = random.randint(1, 10)
    time.sleep(2)
    print("<< 카드 선택 완료 >>\n")
    time.sleep(2)
    print("성모의 카드는 {}입니다.".format(boss))

    time.sleep(2)
    print(line)
    print("<< 베팅 시작 >>\n")
    time.sleep(2)
    print("베팅을 시작합니다.")
    time.sleep(2)
    print("현재 총 보유 금액은 20원입니다. 기본 베팅 금액으로 1원이 차감됩니다.")

    user_money = 19
    boss_money = 19

    user_bet = 1
    boss_bet = 1

    for i in range(20):
        # 성모 베팅
        time.sleep(2)
        boss_plus = random.randint(user_bet - boss_bet, boss_money)
        boss_bet += boss_plus

        # 성모 포기
        if boss_plus == 0:
            print(line)
            print("## 승리 ##\n")
            print("성모가 게임을 포기했습니다. 내 카드는 {}입니다.".format(user))
            if boss == 10:
                print("성모의 카드가 10이므로 성모에게서 10원을 뺏어옵니다.")
            break

        print("\n성모가 {}원을 더 베팅했습니다. 현재 성모의 총 베팅 금액은 {}원입니다.".format(boss_plus, boss_bet))

        # 베팅 완료
        if user_bet == boss_bet:
            time.sleep(2)
            print(line)
            print("<< 결과 공개 >>\n")
            time.sleep(2)
            print("{}원으로 베팅이 끝났습니다. 서로의 카드를 공개합니다.\n".format(user_bet))
            time.sleep(2)
            if user > boss:
                print("## 승리 ##")
                print("내 카드는 {}, 성모의 카드는 {}입니다. 성모에게서 {}원을 뺏어옵니다.".format(user, boss, user_bet))
            elif user == boss:
                print("## 무승부 ##")
                print("두 카드 모두 {}입니다. 재경기를 시작합니다.".format(user))
                indian_poker()
            else:
                print("## 패배 ##")
                print("내 카드는 {}, 성모의 카드는 {}입니다. 성모에게 {}원을 뺏겼습니다.".format(user, boss, user_bet))
            break

        # 나 베팅
        time.sleep(2)
        print("\n현재 보유 금액은 {}원, 나의 총 베팅 금액은 {}원입니다.".format(user_money, user_bet))
        time.sleep(2)
        print("\n추가 베팅 금액을 입력하세요. 베팅 금액은 {}원 이상이어야 합니다.".format(boss_bet-user_bet))
        time.sleep(2)
        user_plus = input("게임 포기를 원하시면, '포기'를 입력하세요.")

        if int(user_plus) < boss_bet - user_bet:
            print("베팅 금액은 {}원 이상이어야 합니다.".format(boss_bet - user_bet))
            user_plus = input("게임 포기를 원하시면, '포기'를 입력하세요.")

        # 나 포기
        if user_plus == "포기":
            print(line)
            print("## 패배 ##\n")
            print("게임을 포기했습니다.\n내 카드는 {}입니다.".format(user))
            if user == 10:
                print("성모에게 10원을 뺏겼습니다.")
            break
        user_bet += int(user_plus)

        # 보유금액 차감
        user_money -= int(user_plus)
        boss_money -= boss_plus

        # 베팅 완료
        if user_bet == boss_bet:
            time.sleep(2)
            print(line)
            print("<< 결과 공개 >>\n")
            time.sleep(2)
            print("{}원으로 베팅이 끝났습니다. 서로의 카드를 공개합니다.\n".format(user_bet))
            time.sleep(2)
            if user > boss:
                print("## 승리 ##")
                print("내 카드는 {}, 성모의 카드는 {}입니다. 성모에게서 {}원을 뺏어옵니다.".format(user, boss, user_bet))
            elif user == boss:
                print("## 무승부 ##")
                print("두 카드 모두 {}입니다. 재경기를 시작합니다.".format(user))
                indian_poker()
            else:
                print("## 패배 ##")
                print("내 카드는 {}, 성모의 카드는 {}입니다. 성모에게 {}원을 뺏겼습니다.".format(user, boss, user_bet))
            break


indian_poker()