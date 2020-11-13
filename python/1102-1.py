# n=int(input('숫자(1-5)=')) #자동형변환 안됨
# if n==1:
#     print('안녕')
# elif n==2:
#     print('안녕 안녕')
# elif n==3:
#     print('안녕')
#     print('안녕')
#     print('안녕')
# else:
#     print('안녕')
#     print('안녕')
#     print('안녕')
#     print('안녕')

#a=['안녕','안녕',....]
#n=int(input('숫자='))
# a=[]
# for i in range(n):
#     a.append('안녕')
# print(a)

#숫자받아서 안녕 수만큼 출력
# a=['안녕' for i in range(n)]
# print(a)


#1-20홀수중 3의 배수인것만 b에
# b=[]
# for i in range(1,21,2):
#     if i%3==0:
#         b.append(i)
# print(b)
#-->컴프리핸션:컬렉션을 만드는 한줄짜리 반복문
# b=[i for i in range(1,21,2) if i%3==0]
# print(b)

#튜플 - 값변경안되는 점만 빼고 사용법은 리스트와 같다
#       파이썬이 주로 사용, 매개변수전달시, 반환값 전달시. 사람은 잘 사용안함.
# a=('감','사과','대추')
# print(a)
# print(type(a))
# for i in a :
#     print(i)

#인덱스와 같이 출력
# a=('빨강','파랑','노랑','초록')
# for i in enumerate(a):
#     print(i)
# print('-'*30)
# for i,v in enumerate(a):
#     print(i,v)

# a,b,c=1,'two','셋'
# print(a,b,c)
# a=1,'two','셋'#파이썬이 알아서 튜플로 싸서줌
# print(a) #파이썬이 알아서 튜플로 싸서줌
# print(a[1])

# a=range(1,10)
# print(list(a))
# print(tuple(a))

#dictionary{} :  java의 map과 비슷
#순서x,키와값 세트, 키는 중복x, 값은 중복가능
# friend={'name':'kim','age':20,1004:'yes'}
# print(type(friend))
# print(friend['age'])
# print(friend[1004])
# print('-'*30)
# for i in friend:
#     #print(i) - key만나옴
#     print(i,friend[i])
# print('-'*30)
# print(friend.values()) # 리스트로 반환
# print(friend.keys())
# print('-'*30)
# for i in friend.items(): #key 와 value 값 반환
#     print(i)
# for i,v in friend.items(): #key 와 value 값 따로따로 받기!
#     print(i,v)
# print('-'*30)
#a='javaScript'
# for i in a: #문자열을 주면 글자하나하나 뜯어져서 나옴
#     print(i)
# r=[i for i in a] #list로 만들기
# print(r)
#
# for i in enumerate(a): #dictionary로 받기
#     print(i)
# print('-'*30)
# r={}
# for i in enumerate(a):
#     #print(i)
#     #r[i[0]]=i[1]
#     r[i[1]]=i[0]
# print(r)
# print('-'*30)
# r={i[1]:i[0] for i in enumerate(a)}
# print(r)

#구구단
for dan in range(1,10):
    for i in range(1,10):
        print(i * dan, end=" ")
    print('')
print('-'*30)
#1-20홀수중 3의 배수인것만 b에
b=[]
for i in range(1,21,2):
    if(i%3==0):
        print(i)
#-->컴프리핸션:컬렉션을 만드는 한줄짜리 반복문
b=[i for i in range(1,21,2) if(i%3==0)]

print(b)

#튜플a를 인덱스와 같이 출력
# a=('빨강','파랑','노랑','초록')