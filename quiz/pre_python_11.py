"""11. 최대공약수를 구하는 함수를 구현하시오

예시
<입력>
print(gcd(12,6))

<출력>
6
"""
A=int(input('입력1:'))
B=int(input('입력2:'))


def gcd(a,b):
    c=min(a,b)
    for i in range(c,0,-1):
        if a%i==0 and b%i==0:
            return(i)

print('두 수의 최대 공약수는:',gcd(A,B))