a=" blue red green "
# print(len(a)) #길이
# print(a)
# print("안녕")
# print("["+a.lstrip()+"]") #왼쪽여백없애기
# print("["+a.rstrip()+"]") #오른쪽여백없애기
# print("["+a.strip()+"]")  #양쪽여백없애기
#
# #a.replace('찾는 문자열','바꿀문자열') ->문자열치환
# print(a.replace(' ','')) #blueredgreen
# print(a.upper())
# print(type(a))

#split하면 list됨--------------------
# a="one-two-three four-five six"
# print(a.split('-'))
# print(a.split(' '))
# print(type(a.split(' ')))
# b=a.split(' ')
# print(b)
# #'기호'.join(리스트)
# print('%'.join(b))
# print(type('%'.join(b)))
#정상종료는 exit code 0

#입력받기-------------------------------
# print("입력하세요.")
# line=input()
# print(line,type(line))
# print(line.split())

#파이썬의 collection : <>은 사용안함
#[]리스트 :인덱스0부터시작
# ()튜플,
# {}딕셔너리,set

a=[1,56,'blue',[1,2,3],1111,'안농',3333,True]
print(a,type(a))
print(a[0])
print(a[1:4])
print(a[3:])
print(a[:4])
print(a[3][0]) #변수안의 변수에 접근
#----
b=['tomato','abrico','raisin']
print(b[1])
b[2]='캠벨' #raisin에서 캠벨로 변경
print(b)
b.append('샤인머스킷') #요소추가!
print(b)
print(sorted(b)) #정렬
a=[3,78,100,55,3]
print('합계',sum(a))
print('평균',sum(a)/len(a)) #avg함수아예없음
print(dir(a)) #a라는 객체에 사용할수있는함수
# print(reversed(b))
# print(list(reversed(b)))

