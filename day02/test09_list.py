# date : 20240130
# desc : 복합자료형 list

# s1 = 80
# s2 = 90
# s3 = 100
# s4 = 50
# s5 = 60 # 학생수만큼 변수를 생성 

# 총갯수가 10(n)이면 인덱스의 마지막 값은 9(n-1)
#index=0   1    2   3   4   5   6   7   8    9 # 0부터 시작
#index=-10 -9  -8   -7  -6  -5  -4  -3  -2   -1
std = [80, 90, 100, 50, 60, 55, 77, 88, 99, 100]

print(std[5]) # n-1을 초과해서 인덱스를 요청할 수 없다.(list index out of range) 

list_1 = [265, 3.5, '문자열', True, [1,2,3,4],(5,6), std] # python에서는 어떤 값이든 리스트에 넣을 수 있다.
print(list_1)
print(list_1[5])

list_1[6] = '바꾼값' # 원래 리스트가 문자열로 변경
print(list_1)

## 리스트 연산
print(list_1[2])
print(list_1[3])

print(list_1[2:3+1]) # 콜론 뒤의 수는 출력하고 싶은 인덱스 숫자에 +1이 필수(파이썬만 해당)

# 마이너스 인덱스
print(std[-8:-4]) # 파이썬에서만 가능. 마이너스는 되도록 사용X
# 이중리스트
print(list_1[4][2]) # [1,2,3,4] 중 3(2번 인덱스)만 가져오기

list_2 = [[1,2,3],[4,5,6],[7,8,9]]
print(list_2[1][2]) # 6

list_4 = [1,2,3]
list_5 = [7,8,9]
# 리스트 연산에서는 + 와 * 만 사용가능
print(list_4 + list_5) # + : 리스트들을 연결
print(list_5 * 2) # * : 리스트를 반복

# len() : 리스트 길이 함수
print(len(list_1))
print(len(std))

# append() : 리스트 마지막에 하나 추가
# insert(index, val) 리스트의 index 이후에 val을 추가.
print(list_1)
list_1.append('Hello!')
print(list_1)

list_1.insert(2, 100) # 2번 인덱스에 값을 추가(기존의 값은 뒤로 밀린다)
print(list_1)

# extend() : 기존 리스트 확장
list_4.extend(list_5) # + 와 extend는 거의 유사하나, + 는 값을 할당해 주어야하지만 extend는 별도의 할당 과정이 필요X
print(list_4)
print(list_5)

# del : 리스트 값 삭제
del list_4[3] # list_4의 3번 인덱스 값을 삭제
print(list_4)
del list_4 # list_4 자체를 삭제(사용시 주의!!)

# pop : # 마지막 또는 지정한 인덱스의 값\을 꺼내오기
val = list_5.pop() # 마지막 값을 꺼내오기
print(val) # 9 
print(list_5) # [7,8]

print(std) # [80, 90, 100, 50, 60, 55, 77, 88, 99, 100]
val = std.pop(2) # 2번 인덱스 값을 꺼내옴
print(val) # 100
print(std) # [80, 90, 50, 60, 55, 77, 88, 99, 100]

# clear : 리스트를 비워냄
list_5.clear() # del()은 완전 삭제, print도 안됨/ clear()은 내용만 삭제, 리스트는 비어있는 상태로 남아있음
print(list_5)

# sort() : 리스트 안의 값들을 정렬
print(list_1)
# list_1.sort() # 문자열, 숫자, 불이 섞여있는 리스트는 정렬 X
std.sort() # 오름차순 정렬
print(std)
std.sort(reverse=True) # 내림차순 정렬
print(std)

# in, not in
print(99 in std) # std 안에 99가 있는가? : True
print(98 in std) # std 안에 98이 있는가? : False

# reverse(), copy(), count() ...

# * 리스트 : 전개연산자
list_a = [1,3,5]
list_b = [2,4,8]
list_c = [*list_a, *list_b]
print(list_c)

list_d = [list_a, list_b]
print(list_d)