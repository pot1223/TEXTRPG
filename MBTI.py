# TODO : MBTI

import time


line = "\n--------------------------------------------\n"

time.sleep(3)

print("\n성모: 진정한 피로그래머에 도전하기 전, 먼저 성격 검사를 실시해 본인의 성향을 파악하세요.")
time.sleep(2)
print("성모: 피로그래밍에서는 MBTI 검사를 변형한 <PIRO> 성격 검사를 제공합니다.")
time.sleep(2)

print(line)
print("<PIRO>를 시작합니다.")
print(line)

# 에너지 방향
q_energy = ["문제1. 다른 피로그래머에게 자신을 소개하는 것이 어렵지 않습니다.",
            "\n문제2. 워크샵에서 먼저 대화를 시작하는 편이었습니다."]
a_energy = 0

# 인식 기능
q_info = ["문제3. 피로그래밍 과제를 할 때 즉흥적으로 움직이기 보다는 주의 깊게 미리 계획합니다.",
          "문제4. 코드를 짤 떄 대체로 상상보다는 경험에 더 의존하는 편입니다."]
a_info = 0

# 판단 기능
q_decision = ["문제5. 팀 과제에서 결정을 내려야 할 때, 일반적으로 가슴보다 논리가 더 중요합니다.",
              "문제6. 다른 피로그래머가 어떤 일로 슬퍼할 때, 위로하기 보다 문제 해결법을 제시합니다."]
a_decision = 0

a_message = "      [동의]  4  3  2  1  [비동의]"

time.sleep(2)
for q in q_energy:
    print(q)
    print(a_message)
    a_energy += int(input("답변"))

for q in q_info:
    print("\n", q, sep="")
    print(a_message)
    a_info += int(input("답변"))

for q in q_decision:
    print("\n", q, sep="")
    print(a_message)
    a_decision += int(input("답변"))

r_energy = "E" if (a_energy > 4) else "I"
r_info = "S" if (a_info > 4) else "N"
r_decision = "T" if (a_decision > 4) else "F"

result = r_energy + r_info + r_decision
print(line)
print("<< 검사결과 >>\n")
print("당신의 PIRO 성격유형은 {}, ".format(result), end="")

if result == "EST":
    print("<활동적인 사업가형>입니다.\n피로그래밍을 통해 스타트업에 도전해 보세요!")
if result == "ESF":
    print("<친절한 사교자형>입니다.\n팀 과제에서 분위기를 고조시키는 우호적인 성격입니다.")
if result == "ENT":
    print("<지도적인 발명가형>입니다.\n팀 과제에서 풍부한 상상력으로 타인을 활력적으로 인도합니다.")
if result == "ENF":
    print("<열정적인 달변가형>입니다.\n다른 피로그래머들의 성장을 도모하고, 새 관계를 만들어 나갑니다.")
if result == "IST":
    print("<끈기있는 백과사전형>입니다.\n한 번 시작한 일은 끝까지 해내는, 장기 프로젝트에서 꼭 필요한 사람입니다.")
if result == "ISF":
    print("<온화한 성인군자형>입니다.\n성실하고 따뜻한 성격으로, 많은 피로그래머들이 프로젝트를 함께 하길 원하는 사람입니다.")
if result == "INT":
    print("<아이디어가 넘치는 과학자형>입니다.\n팀 과제에서 전체를 조합해 전략적으로 비전을 제시합니다.")
if result == "INF":
    print("<통찰적인 잔다르크형>입니다.\n 뛰어난 통찰력으로 프로젝트에서 이상적인 결과물을 만들어 냅니다.")
print(line)

time.sleep(2)
print("성모: 피로그래머가 되기 위한 사전준비가 모두 끝났습니다.")
time.sleep(2)
print("성모: 이제 진정한 피로그래머에 도전하세요!")
