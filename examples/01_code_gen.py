"""1. 코드 생성 예제"""
from utils import LMClient

with LMClient() as lm:
    code = lm.respond("Python으로 FizzBuzz 함수 만들어줘")
print(code)
