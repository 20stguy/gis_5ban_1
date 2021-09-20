# # func라는 함수를 받는다
# def decorator(func):
# # 함수안에 새로운 함수를 선언한다
#     def decorated():
#         print('함수 시작!')
#         func()
#         print('힘수 끝!')
#     return decorated
#
#
# # 앞뒤 함수 시작, 함수 끝이라는 코드가 지저분하다 -> decorator쓰기
# @ decorator # decorator로 꾸며주게 된다
# def hello_world():
#     # print('함수 시작!')
#     print('Hello World')
#     # print('힘수 끝!')
#
# hello_world()
#
# # 실습
# # 삼각형의 넓이 계산 함수 작성
# # 사각형의 넓이 계산 함수 작성
# # 입력값이 모두 양수인지 확인하고, 아닐경우 Error를 발생시키는
# # Decorator 작성 적용
#
# def decorator(func):
#     def decorated(horizontal, vertical):
#         if horizontal < 0 or vertical < 0:
#             print("Error")
#         else:
#             func
#     return decorated
#
# #
# @decorator
# def triangle(a, b):
#     # horizontal = []
#     # vertical = []
#     print(horizontal * vertical / 2)
#
# @decorator
# def square():
#     # horizontal = []
#     # vertical = []
#     print(horizontal * vertical)
#
# triangle
#
# # 강사님 방법
# def check_integer(func):
#     def decorated(width, height):
#         if width >= 0 and height >= 0:
#             return func(width, height)
#         else:
#             raise Value Error('Input must be  positive value')
#         return decorated
#
#
# @check_integer
# def
#
#
# @check_interger
# def
#
#
#
# class User(is_authenticated):
#     def Ise

