# file : test12_dictionary.py
# date : 20240130
# desc : 복합자료형 딕셔너리

## 사전형 key와 value 쌍을 나열해 놓은 자료형
# { key:value, key:value, key:value, ... }
dict_movie = { 'name':'어벤저스 엔드게임', 'type':'히어로 무비', 'year':2019, 
              'director':['온소리 루소','조 루소'], 
              'cast':['아이언맨','타노스','헐크','토르','닥터스트레인지'] }

# 조회              
print(dict_movie['name'])
print(dict_movie['year'])
print(dict_movie['director'])
print(dict_movie['cast'])

# 추가, 수정
dict_movie['year'] = 2020 # 수정 : 기존의 key
print(dict_movie)

dict_movie['producer'] = '케빈 파이기' # 추가 :  새로운 key
print(dict_movie)

#print(dict_movie['musician']) # 존재하지 않는 key를 조회할 경우 : 오류발생

# 키에 대한 값을 찾을 때
if 'producer' in dict_movie: # 딕셔너리에 키가 있는지 확인할 때
    print(dict_movie['producer'])
else:
    print('제작자 없음')

musician = dict_movie.get('musician') # ,get() : 값이 있다면 그 값을 가져오지만, 해당 값이 없을 경우 None을 가져옴
print(musician) # 오류(예외) 발생 X
#print(dict_movie['musician']) # 오류(예외) 발생
print('반복문 1 출력------------------------------------------------------------------------')
# 반복문으로 출력
for key in dict_movie:
    print(key, ':', dict_movie[key])

print('반복문 2 출력------------------------------------------------------------------------')
for key, value in dict_movie.items(): # items()함수 : 딕셔너리에 있는 key와 value의 쌍을 얻음
    print(key, ':', value)