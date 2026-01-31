파이썬에서 LMStudio 활용해보기

1️⃣ **코드 생성**

```python
from utils.lm_clientimport LMClient

with LMClient()as lm:
    code = lm.respond("Python으로 FizzBuzz 함수 만들어줘")
print(code)

```

2️⃣ **자연어 → JSON 구조화 (중간에 번역 넣어서 결과물 퀄리티 비교해보기)**

```python
with LMClient()as lm:
    workflow_json = lm.respond("""
    아래 요구사항을 JSON으로 변환해줘:
    - 사용자 로그인 기능 필요
    - 하루 1000명 예상
    - Python 기반 FastAPI
    """)
print(workflow_json)

```

3️⃣ **텍스트 요약**

```python
with LMClient()as lm:
    summary = lm.respond("다음 글 요약해줘: 장문의 글...")
print(summary)

```

4️⃣ **간단한 챗봇**
```python
with LMClient()as lm:
    answer = lm.respond("안녕, 오늘 기분은 어때?")
print(answer)

```