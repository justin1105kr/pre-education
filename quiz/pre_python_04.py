"""4. 삼각형의 가로와 높이를 받아서 넓이를 출력하는 함수를 작성하시오.


예시
<입력>
print(Triangle(10,20))

<출력>
100

"""


def Triangle(width,height):
    result=(height*width)/2
    return result

w=int(input('가로:'))
h=int(input('세로:'))

print('삼각형의 넓이는',Triangle(w,h),'입니다.')
