"""1. 코드 생성 예제 - 로또 번호 생성기"""
from utils import LMClient

with LMClient() as lm:
    code = lm.respond("""
로또 번호 생성하는 Python 코드 만들어줘. 1~45 중 6개 숫자를 중복 없이 뽑아야 해.

반드시 지켜야 할 규칙:
- 순수 Python 코드만 출력
- ```python 같은 마크다운 코드블록 사용 금지
- 설명이나 주석 없이 실행 가능한 코드만
""")
print(code)
