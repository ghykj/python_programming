#ctrl+shift+f10 = 실행

def add(n1,n2):
    n1+n2

add2 = lambda n1, n2 : n1 + n2
print(type(add2))
print(add2(100,200))

class User:
    #생성자 선언
    def __init__(self, name):
        self.name = name

    #toString() - 안 할 경우 print 하면 객체 주소가 나옴
    def __str__(self):
        return self.name
"""
파이썬 모듈 안에는 함수와 클래스를 선언 할 수 있디
block comment
"""
#객체생성
user = User("파이썬")
print(user)
