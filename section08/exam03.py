'''
저장된 비밀번호를 맞히는 프로그램을 구현하세요.
저장된 비밀번호는 'qwerty'이며 최대 5번 시도할 수 있습니다.
5번 이내에 비밀번호를 맞히면 '비밀번호를 맞혔습니다.' 를 출력하고
그렇지 않으면 '비밀번호 입력 횟수를 초과했습니다.' 를 출력하세요.

출력 결과
비밀번호를 입력하세요 >>> 123456 
비밀번호를 입력하세요 >>> asdfgh
비밀번호를 입력하세요 >>> qwerty
비밀번호를 맞혔습니다.

비밀번호를 입력하세요 >>> 123456
비밀번호를 입력하세요 >>> asdfgh
비밀번호를 입력하세요 >>> zxcvbn
비밀번호를 입력하세요 >>> 098765
비밀번호를 입력하세요 >>> poiuyt
비밀번호 입력 횟수를 초과했습니다.
'''

correct = False
for n in range(5):
    password = input('비밀번호를 입력하세요 >>> ')
    if password == 'qwerty':
        correct = True
        break

if correct == True:
    print('비밀번호를 맞혔습니다.')
else:
    print('비밀번호 횟수를 초과했습니다.')