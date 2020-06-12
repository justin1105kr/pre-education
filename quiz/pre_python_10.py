"""10. 팩토리얼을 구하는 함수를 작성하시오.
ex ) 5! = 5x4x3x2x1
  print(factoral(5)) -> 120 출력
  
예시
<입력>
print(factorial(5))

<출력>
120
  """
a=int(input("입력:"))
def factorial(a):
    r=1
    for i in range(1,a+1):
        r*=i #*=를 사용하지 않고 만들 수는 없나?
    return r
print(factorial(a))
