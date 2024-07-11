#변수 두 개 이용
sum = 0
x = 0
while x<100:
    x=x+1
    if x%2 == 1:
        sum = sum+x
print(sum)


print("="*30)

#리스트를 이용(sum함수를 사용하지 않고)
l = []
k = 0
while k<100:
    k=k+1
    if k%2 == 1:
        l.append(k)
b = 0
for a in l:
    b = b+a
print(b)