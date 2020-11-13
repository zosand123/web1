# a=[1,2,3,4,5,3,2,4,1,5]
# print(a)
# print(len(a))
# print(a.count(5))
# a.append('seven')
# print(a)
# a.append(['one','two','three'])
# print(a)
# a.insert(3,'*') #a.insert(인덱스,값) - 인덱스위치에 값을 집어넣어라
# print(a)
# print(a[7])
# a[3]='!'
# print(a)
# a.remove(5) #처음나타나는 5를 삭제
# print(a)
# del a[:3] #인덱스0부터 2번째까지 삭제
# del a #객체삭제
# print(a)

a=['cero','uno','dos','cuatro','cinco','seis','sete','ocho']

# for 변수 in 반복가능객체:
#    내용
for i in a: #i=1,2,...
    print(i) #들여쓰기로 for문의 시작과 끝을 구분

# range(시작(0일때 생략가능),종료(<),증감(1일때생략가능))
# print(range(1,10,1))
# print(list(range(1,10,1)))
# print(tuple(range(1,10,1)))
#
# for i in range(1,6,2):
#     print(i,a[i])
# for i in range(len(a)):
#     print(i,a[i])
#
# for i in range(5): # 종료값만 표시한 형태, 시작값생략시 0, 증감생략시 1
#     print(i)
#
# 1부터 100까지 숫자출력
# for i in range(1,101):
#     print(i,end=' ')
# print()
# print()
# for i in range(3,1000,3):
#     print(i, end=' ')
# print()
# print()
# for i in range(101):
#     print(i, end=' ')
# print()
#
# #컴프리헨션----------------------
# a=[i for i in range(101)]
# print(a)
# print()
#
# for i in range(100):
#     print(7)
# b=[7 for i in range(100)] #c를 간소화한가정
# print(b)
# print(len(b))
# c=[]
# for i in range(100):
#     c.append(7)
# print(c)
# c=[i for i in range(1,100,2)]
# # d=['good' for i in range(5)]
# d=['good' for _ in range(5)] #i변수가 의미없을때 _를 넣기도한다
# print(c)
# print(d)
# e=['good'+str(i) for i in range(5)]
# print(e)

# b='3'
# print(type(int(b)))

