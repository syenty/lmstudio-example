"""2. 자연어 → JSON 구조화 예제"""
from utils import LMClient

with LMClient() as lm:
    workflow_json = lm.respond("""
    아래 요구사항을 JSON으로 변환해줘:
    - 사용자 로그인 기능 필요
    - 하루 1000명 예상
    - Python 기반 FastAPI
    """)
print(workflow_json)
