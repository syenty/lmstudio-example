"""4. 간단한 챗봇 예제"""
from utils import LMClient

with LMClient() as lm:
    answer = lm.respond("안녕, 오늘 기분은 어때?")
print(answer)
