"""3.Enter key를 눌러 주사위를 던지게 한 후, 주사위의 눈이 높은 사람이 승리하는
간단한 주사위 게임을 만드세요


예시
<입력>
첫번째 참가자 엔터키를 눌러 주사위를 던져 주세요 : 1~6 랜덤숫자 출력
두번째 참가자 엔터키를 눌러 주사위를 던져 주세요 : 1~6 랜덤숫자 출력

<출력>
첫 번째(두 번째) 참가자의 승리입니다. or 비겼습니다.

"""
import random

print('첫번째 참가자 엔터키를 눌러 주사위를 던져 주세요:',end='') #질문 뒤에 랜덤숫자가 줄바꿈 없이 나오는 방법?
input()
ran1=random.randint(1,6)
print(ran1)
input('두번째 참가자 엔터키를 눌러 주사위를 던져 주세요:')
ran2=random.randint(1,6)
print(ran2)
if ran1==ran2:
    print('비겼습니다.')
elif ran1<ran2:
    print('두번째 참가자의 승리입니다.')
elif ran1>ran2:
    print('첫번째 참가자의 승리입니다.')
else:
    print('정확히 입력해주세요.')
