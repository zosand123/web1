#1)함수정의
#def 함수명(매개변수):
#   내용
#2)함수호출
# 함수명(매개변수)

def f1(name):
    print('hi '+name)
#f1('kim')
#print(f1('lee')) #반환값없으므로 실행x
def f2(name):
    return 'hi~'+name

# print(f2('lee'))

def f3(x):
    y1=x*2
    y2=x*20
    y3=x*30
    return y1,y2,y3
r1,r2,r3=f3(3)
# print(r1,r2,r3)
r1=f3(70) #튜플로 반환
# print(list(r1))
def f4(x):
    y1=x*2
    y2=x*20
    y3=x*30
    return [y1,y2,y3]
r1=f4(5)
#print(r1)
r1,r2,r3=f4(5)
#print(r1,r2,r3)

def f5(x):
    y1=x*2
    y2=x*20
    y3=x*30
    return {'y1':y1,'y2':y2,'y3':y3}
r1=f5(8)
#print(r1)
#print(r1,r1.keys(),r1.values(),r1.items())
def f6(x,y):
    print('f6실행중')
    print(x,y)
#f6(3,4)
#f6(3,4,5)

def f7(x=1,y=2,z=3): #default값을 지정한것, 넣으면 차례대로 안넣으면 기본값
    print(x,y,z)
# f7(10,20,30)
# f7()
# f7(11,22)
# f7(z=99)

#def f8(x,=1,y=2,z): 오류, 기본값을 뒤로넣고 필수입력 앞으로
def f8(x,y,z=3):
    print(x,y,z)
f8(2,3)
f8(10,20,30)

# 가변인수 *,**
def f10(*args):
    print(args)
    print(type(args))
    hap=0
    for i in args:
        hap+=i
    print(hap)
#f10()
#f10(2,4,543,436)
#f10('one'+'two') 파이썬에선 문자의 연산 안됨

def f11(**args): #갯수의 제한이없는 딕셔너리로 매개변수 받을경우
    print(args)
    print(type(args))
#f11('a','b','c')
f11(name='kim',addr='busan',age=10)
