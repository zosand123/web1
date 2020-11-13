people={'name':'Kate','age':'45','addresse':'Austrailia'}
# print(people)
# print(type(people))
# print(people["addresse"])
people['Family name']='Blanchett'
# print(people)
# del people['age']
# print(people)
# for i in people:
#     print(i)
# for i in people.items():
#     print(i)
# for i,v in people.items():
#     print(i,v)
# print(people.keys())
# print(people.values())

#set : 중복 제거됨
a={1,2,3,4,5,6,3,5,5,6}
# print(a)
# print(type(a))

b=[2,5,4,5,2,4,5,6,6,3]
# print(set(b))
# b=set(b) #list를 set으로 변환
# print(b)

a.add(8)
# print(a)
# a.update([55,66])
# print(a)

#정규표현식
# ?	물음표는 0번 또는 1차례까지의 발생을 의미한다. 이를테면 colou?r는 "color"와 "colour"를 둘 다 일치시킨다.
# *	별표는 0번 이상의 발생을 의미한다. 이를테면 ab*c는 "ac", "abc", "abbc", "abbbc" 등을 일치시킨다.
# +	덧셈 기호는 1번 이상의 발생을 의미한다. 이를테면 ab+c는 "abc", "abbc", "abbbc" 등을 일치시키지만 "ac"는 일치시키지 않는다.
# {n}[6]	정확히 n 번만큼 일치시킨다.
# {min,}[6]	"min"번 이상만큼 일치시킨다.
# {min,max}[6]	적어도 "min"번만큼 일치시키지만 "max"번을 초과하여 일치시키지는 않는다.

a='''3412  Bob 123
    3834  Jonny 333
    1248   Kate 634
    1423   Tony 567
    2567  Peter 435
    3567  Alice 535
    1548  Kerry 534'''

import re #정규식사용
#re.findall(r'정규식',문자열)
r1=re.findall(r'[0-9]',a)
print(r1)
r1=re.findall(r'[0-9]+',a)
print(r1)
r1=re.findall(r'[A-Z]',a)
print(r1)
r1=re.findall(r'[A-Za-z]',a)
print(r1)
r1=re.findall(r'[A-SU-Z][a-z]+',a)
print(r1)        