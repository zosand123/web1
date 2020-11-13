# import os
# import sys
# import urllib.request
# import json
# client_id = "b3sD4mEfhUBH9gHc8DCt"
# client_secret = "2SmGkrIAOp"
# encText = urllib.parse.quote("python")
# url = "https://openapi.naver.com/v1/search/blog?query=" + encText # json 결과
# # url = "https://openapi.naver.com/v1/search/blog.xml?query=" + encText # xml 결과
# request = urllib.request.Request(url)
# request.add_header("X-Naver-Client-Id",client_id)
# request.add_header("X-Naver-Client-Secret",client_secret)
# response = urllib.request.urlopen(request)
# rescode = response.getcode()
# if(rescode==200):
#     response_body = response.read()
#     result=response_body.decode('utf-8')
# else:
#     print("Error Code:" + rescode)
#
# d1=json.loads(result)
# #print(d1)
# #items안에 title,description의 내용 출력
# #print(d1['items'])
# for doc in d1['items']:
#     print(doc['title'])
#     print(doc['description'])
#     print('-'*30)

#번역접근--------------------------------------------------------
# 네이버개발자센터 > 파파고번역 > 개발가이드보기 > 예제코드링크 > 네이버 Papago NMT API 예제
import os
import sys
import urllib.request
import json
client_id = "P5NC3PzLiI6T454duFcX"
client_secret = "XsmZUUqUp0"
encText = urllib.parse.quote("hi")
data = "source=en&target=ko&text=" + encText
url = "https://openapi.naver.com/v1/papago/n2mt"
request = urllib.request.Request(url)
request.add_header("X-Naver-Client-Id",client_id)
request.add_header("X-Naver-Client-Secret",client_secret)
response = urllib.request.urlopen(request, data=data.encode("utf-8"))
rescode = response.getcode()
if(rescode==200):
    response_body = response.read()
    result=response_body.decode('utf-8')
else:
    print("Error Code:" + rescode)
dic=json.loads(result)
print(dic['message']['result']['translatedText'])