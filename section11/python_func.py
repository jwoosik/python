'''
파이썬의 특별한 함수 스타일
'''

# 코드의 생략
def pass_func():
    ... # pass, ... 같은 의미


# 가변 매개 변수
def show(*vals:int, horiz:int=1):
    print(vals)
    for n in vals:
        if horiz == 1:
            print(n, end='\t')
        else:
            print(n)
    print()
    
def greet(message:str, temp:int=2, count:int=3):    # 뒤에 있는 매개변수부터 값을 넣어라
    for n in range(count):
        if count == 2:
            return  # return 뒤에 값이 없으면 그 즉시 빠져나간다.
        
        
        print(message)
        
greet('안녕하세요.', count=5)
greet('반갑습니다.')
    
show(1,2,3,4,5, horiz=1)
show(1,2,3,)