"""3. 텍스트 요약 예제"""
from utils import LMClient

with LMClient() as lm:
    summary = lm.respond("다음 글 요약해줘: 장문의 글...")
print(summary)
