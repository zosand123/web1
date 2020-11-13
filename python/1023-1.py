#주석은 #
#도움말 ctrl+click

# a='dkdkdk'
# print(a)
# a=3.5
# print(a)
# c=True
# print(c,a)
# print("a의 값은",a,"이다")
# print("a의 값은",a,"이다",sep="*",end='')
# print("a의 값은",a,"이다",sep="*")
# print('-'*30)
# a=30
# b=5
# print(a+b)
# print(type(a)) #<class 'int'>
# a='machine'
# print(type(a)) #<class 'str'>

#형변환
# print(a+str(b))

#a와 b의 값 바꾸기
# a=7
# b=10
# print(a,b)
# a,b=b,a
# print(a,b)

#변수에 한꺼번에 값 할당
# a,b,c,d=3,0,True,'2'
# print(a,b,c,d)
# print(bool(a))
# print(bool(b)) #형변환하면 0은 false 나머지숫자는 true
# d=int(d) #형변환
# print(type(d))

# print('a+d=',a+d)
# print('a/d=',a/d)
# print('a//d=',a//d) #몫
# print('a%d=',a%d) #나머지
# print('a**d=',a**d)#제곱

#관계연산자 ><!=등등 자바랑 동일

# print("---------------------------------")
# age=21
# b1=age<10
# b2=age>20
# print(b1,b2)
# print(10<=age<=30)
#비트연산자는 자격증시험칠때 이외에 절대안씀 (자바도 마찬가지)

#문자열 : '..',"..",'''여러줄문자''',"""여러줄문자"""
a='문자열 표현방법" @123!'
print(a)
a='문자열 표현방\'법" @123!'
print(a)
a='''점프 투 파이썬 오프라인 책 출간 (정보게이트)	2001.09
2	개인 위키에 "점프 투 파이썬" 공개'''
print(a)

#문자열연산
a='beau voir'
b='sartre'
c='and'
print(a,c,b)

#문자열 인덱싱 : 문자열중에서 특정데이터를 획득 []-*수료할때까지 계속나옴!!!*
#[인덱스]
#[시작인덱스:끝인덱스] 시작인덱스<=x<끝인덱스
a='0123456789'
print(a)
print(a[-1])
print(a[:7]) #왼쪽생략 처음부터
print(a[3:]) #오른쪽생략:끝까지 다
print(a[:]) #전부다가져오기 양쪽다 생략

print("---------------------------------")
a='pithon'
# a[1]='y' #에러 #문자열은 일부만 바꿀수없음!
print(a[0]+'y'+a[2:])

print("---------------------------------")
#포멧팅 python2에서 쓰는방식(3이랑 호환되긴함,해석을 위해서 배움)
a=10
b=20
c='green'
print(a,b,c)
print("[%d + %d = %s]"%(a,b,c)) #타입맞출 자신없으면 걍 다 s
# %s:문자열 %d:정수 %f:실수 %o:8진수 %x:16진수 %%:%
#""나 ''나 똑같으니 그냥 ""을 쓰자

#포멧팅 python3에서 쓰는방식
print("[{} + {} = {}]".format(a,b,c))
print("---------------------------------")
a='473985379852378192785237'
print(a.count('5')) #문자갯수세기
print(a.count('0'))
print(a.find('5')) #가장먼저 찾아지는 인덱스번호 출력
print(a.find('0')) #없으면 -1
print(a.index('5'))
#print(a.index('0')) #없으면 오류처리하는것만 차이점이고 나머진 index랑 find랑 똑같음