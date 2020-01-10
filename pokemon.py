# import threading

# def print_time_delay():
#     threading.Timer(1.0, print_time_delay).start()
#     print('Hello world')

# print_time_delay()

def ask_hour(received_hour):
    if received_hour.isdigit():
        received_hour_2 = int(received_hour)
        if 0 <= received_hour_2 <= 24:  
            global hour
            hour = received_hour_2
            print("뭐야 벌써 %d시라고!!!!" %received_hour_2)
        else: 
            print('뭐야 그런 시간은 없는데.', end="")
            received_hour = input('지금이 몇 시라고? : ')
            ask_hour(received_hour)
    else:
        print('뭐야 그런 시간은 없는데.', end="")
        received_hour = input('지금이 몇 시라고? : ')
        ask_hour(received_hour)

def which_game_to_play(value):
    if value.isdigit():
        value_2 = int(value)
        if value_2 == 1:  
            time.sleep(5)
            print('')
            print('')
            import black_and_white
        elif value_2 == 2:
            time.sleep(5)
            print("")
            print("")
            import indian_poker
        else: 
            print('잘못 입력하였습니다.')
            value = input('플레이할 게임을 선택하세요 : ')
            which_game_to_play(value)
    else:
        print('잘못 입력하였습니다.')
        value = input('플레이할 게임을 선택하세요 : ')
        which_game_to_play(value)

import time
print('......................')
time.sleep(1)
print('......................')
time.sleep(1)
print('뭐야 벌써 시간이.......')
time.sleep(1)
received_hour = input("지금이 몇 시지? : ")
ask_hour(received_hour)
time.sleep(1)
print('피로그래밍 과제가 아직 산더미같이 남았다고!!!')
time.sleep(1)
print('빨리 시작해야겠는걸')
time.sleep(1)
print('')
time.sleep(1)
print('까똑')
print('')
time.sleep(1)
print('정성모')
time.sleep(1)
print('''
 ------------------------------------------------------
|                                                      |
|  [2주차 과제 안내]                                   |
|    강의: 코딩도장 파이썬 끝까지 모두 수강해오기      |
|    강의 제출: 전과 동일                              |
|                                                      |
|                                                      |
 ------------------------------------------------------
''')
time.sleep(1)
print('으아아아아아')
time.sleep(1)
print('')
time.sleep(1)
print('')
time.sleep(1)
print('GAME START!')
time.sleep(1)
if 0 <= hour < 10:
    hour_left = 10 - hour
elif 10 <= hour <= 12:
    hour_left = 22- hour
elif 13 <= hour <= 24:
    hour_left = 34 - hour
print('남은 시간 : %d' %hour_left)
time.sleep(1)
print('게임 설명 : 성모와의 카드 게임에서 승리하여 과제를 끝내세요!')
time.sleep(1)
print('             게임에서 승리하면')
time.sleep(1)
print('            \"과제를 끝마친자\" 칭호를 얻습니다')
time.sleep(1)
print('')
time.sleep(1)
print('성모 : ')
time.sleep(1)
print('후후후 게임을 시작하지')
time.sleep(1)
print('Do you want to play a game?')
time.sleep(1)
print('')
print('1. 흑과 백         2. 인디언 포커')
value = input('플레이할 게임을 선택하세요 : ')
which_game_to_play(value)
