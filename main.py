#출처: https://wikidocs.net/29
import mod1
print(mod1.add(3, 4))
print(mod1.sub(4, 2))

# mod1.add처럼 쓰지 않고 add처럼 모듈이름 없이 함수이름만 쓰고 싶은 경우, from 모듈이름 import 모듈함수를 씁니다.
from mod1 import add, sub
print(add(3, 4))
print(sub(4, 2))

# *는 '모든 것'이라는 뜻입니다.
from mod1 import *
print(add(3, 4))
print(sub(4, 2))

# class일 경우
import mod2
print(mod2.PI)
a = mod2.Math()
print(a.solv(2))
print(mod2.add(mod2.PI, 4.4)) # add 함수 역시 당연히 사용할 수 있습니다.