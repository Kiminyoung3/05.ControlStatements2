#라이브러리에서 import를 가져온다.
import random
#import 라이브러리에서 랜덤 수를 생성하는 randint를 사용한다.

r_list = []
count = 0

while count <6 :
    count = count+1
    a = random.randint(1, 45)
    r_list.append(a)

print(r_list)
