player_1_black = [0, 2, 4, 6, 8]
player_1_white = [1, 3, 5, 7]
player_2_black = [0, 2, 4, 6, 8]
player_2_white = [1, 3, 5, 7]

player_1_score = 0
player_2_score = 0

player_1_num = 0
player_2_num = 0

index = 0
player_1_submitted_num = -1

import random, time

class player_1_black_and_white():
    def __init__(self, number):
        self.number = number
    def check(self):
        print('나 :', '흑 -', player_1_black, '백 -', player_1_white)
    def remove(self, number):
        if number == 0 or number == 2 or number == 4 or number == 6 or number == 8:
            player_1_black.remove(number)
        elif number == 1 or number == 3 or number == 5 or number == 7:
            player_1_white.remove(number)


class player_2_black_and_white():
    def __init__(self, number):
        self.number = number
    def check(self):
        # print('성모 :', '흑 -', player_2_black, '백 -', player_2_white)
        print('성모 :', '흑 -', len(player_2_black), '백 -', len(player_2_white))
    def remove(self, number):
        if number == 0 or number == 2 or number == 4 or number == 6 or number == 8:
            player_2_black.remove(number)
            print('\'성모\'가 \'흑\'을 제출하였습니다')
        elif number == 1 or number == 3 or number == 5 or number == 7:
            player_2_white.remove(number)
            print('\'성모\'가 \'백\'을 제출하였습니다')

def isInteger(submission):
    if submission.isdigit():
        submission_2 = int(submission)
        if 0 <= submission_2 <= 8:  
            global player_1_submitted_num
            player_1_submitted_num = submission_2
        else: 
            print('잘못 입력하였습니다.')
            submission = input("제출할 숫자 : ")
            isInteger(submission)
    else:
        print('잘못 입력하였습니다.')
        submission = input("제출할 숫자 : ")
        isInteger(submission)

def player_2_isitinlist():
    player_2_random_num = random.randint(0, 8)
    if player_2_random_num in player_2_black or player_2_random_num in player_2_white:
        player_2_submitted_num = player_2_random_num
        global player_2_num
        player_2_num = player_2_submitted_num
        player_2.remove(player_2_submitted_num)
    else:
        player_2_isitinlist()

def player_1_isitinlist():
    submission = input("제출할 숫자 : ")
    global player_1_submitted_num
    isInteger(submission)
    if player_1_submitted_num in player_1_black or player_1_submitted_num in player_1_white:
        global player_1_num
        player_1_num = player_1_submitted_num
        player_1.remove(player_1_submitted_num)
    else:
        print('제출한 숫자가 리스트에 없습니다.')
        player_1_isitinlist()

def check_score(player_1_num, player_2_num):
    if player_1_num > player_2_num:
        global player_1_score
        global player_2_score
        player_1_score += 1
        print('내가 이겼습니다.')
        time.sleep(1)
        print('나의 점수 : %d' %player_1_score)
        print('\'성모\'의 점수 : %d' %player_2_score)
        time.sleep(1)
        global index
        index = 1
    elif player_1_num < player_2_num:
        player_2_score += 1
        print('\'성모\'가 이겼습니다.')
        time.sleep(1)
        print('나의 점수 : %d' %player_1_score)
        print('\'성모\'의 점수 : %d' %player_2_score)
        time.sleep(1)
        index = 0
    elif player_1_num == player_2_num:
        print('무승부입니다.')
        time.sleep(1)
        print('나의 점수 : %d' %player_1_score)
        print('\'성모\'의 점수 : %d' %player_2_score)
        time.sleep(1)
        pass

def who_goes_first():
    print('누가 카드를 먼저 제시할지 결정합니다.')
    print('.')
    time.sleep(1)
    print('.')
    time.sleep(1)
    print('.')
    time.sleep(1)
    global index
    decision = random.randint(0, 1)
    if decision == 0:
        index = decision
        print('\'성모\'가 먼저 카드를 제시합니다.')
        print('-----------------------------------------------')
    if decision == 1:
        index = decision
        print('내가 먼저 카드를 제시합니다.')
        print('-----------------------------------------------')

player_1 = player_1_black_and_white(2)
player_2 = player_2_black_and_white(2)

while(True):
    who_goes_first()
    i = 1
    while i < 10:
        print('       Round %d      ' %i)
        if index == 0:
            player_2_isitinlist()
            player_2.check()
            time.sleep(1)
            print('')
            time.sleep(1)
            player_1.check()
            player_1_isitinlist()
            time.sleep(1)
            print('')
            check_score(player_1_num, player_2_num)
        elif index == 1:
            player_1.check()
            player_1_isitinlist()
            print('')
            time.sleep(1)
            player_2_isitinlist()
            player_2.check()
            print('')
            time.sleep(1)
            check_score(player_1_num, player_2_num)
        i += 1
        print('-----------------------------------------------')

    print('')
    time.sleep(1)
    print('최종 결과 :')
    time.sleep(1)
    if player_1_score < player_2_score:
        print('\'성모\'가 승리했습니다.')
        time.sleep(1)
        answer = input('게임을 다시 시작하겠습니까?(Y/N) : ')
        if answer == 'Y':
            pass
            time.sleep(1)
        else:
            break
    elif player_1_score == player_2_score:
        print('비겼습니다.')
        time.sleep(1)
        answer = input('게임을 다시 시작하겠습니까?(Y/N) : ')
        if answer == 'Y':
            pass
            time.sleep(1)
        else:
            break
    else:
        print('내가 승리했습니다.')
        answer = input('게임을 다시 시작하겠습니까?(Y/N) : ')
        if answer == 'Y':
            pass
            time.sleep(1)
        else:
            break