def add(a, b):
    return a + b

def sub(a, b):
    return a-b
"""
직접 이 파일을 실행했을 때는 __name__ == '__main__'이 참이 되어 if문 다음 문장이 수행됩니다.
반대로 대화형 인터프리터나 다른 파일에서 이 모듈을 불러서 사용할 때는 거짓이 되어 if문 다음 문장이 수행되지 않습니다.
why?
파이썬의 __name__ 변수는 파이썬이 내부적으로 사용하는 특별한 변수 이름입니다.
만약 직접 mod1.py 파일을 실행할 경우 mod1.py의 __name__ 변수에는 __main__ 값이 저장됩니다. 
하지만 파이썬 셸이나 다른 파이썬 모듈에서 mod1을 import 할 경우에는 mod1.py의 __name__ 변수에는 mod1.py의 모듈 이름 값 mod1이 저장됩니다.
"""
if __name__ == '__main__':
    print(add(1, 4))
    print(sub(4, 2))