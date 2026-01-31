"""2. 자연어 → JSON 구조화 예제 - 프로젝트 설정 파싱"""
from enum import Enum

from pydantic import BaseModel, Field

from utils import LMClient


class Language(str, Enum):
    JAVA = "Java"
    PYTHON = "Python"
    TYPESCRIPT = "TypeScript"
    KOTLIN = "Kotlin"


class Database(str, Enum):
    MYSQL = "MySQL"
    POSTGRESQL = "PostgreSQL"
    MONGODB = "MongoDB"


class ProjectConfig(BaseModel):
    """프로젝트 설정 스키마"""

    language: Language = Field(description="프로그래밍 언어")
    version: str = Field(description="언어 버전 (Java: 8/11/17/21, Python: 3.10/3.11/3.12)")
    framework: str = Field(description="프레임워크 이름 (예: SpringBoot, FastAPI, Express)")
    database: Database = Field(description="데이터베이스")
    project_name: str = Field(description="프로젝트 이름 snake_case로")


# 사용자 요구사항
user_request = "python으로 주문 관리 서비스 프로젝트 구성해줘"

with LMClient() as lm:
    config = lm.respond_structured(
        f"""다음 요구사항을 분석해서 프로젝트 설정을 추출해줘.

요구사항: {user_request}

규칙:
- version은 해당 언어의 적절한 버전 선택
  - Java: 8, 11, 17, 21 중 선택 (최신 권장: 21)
  - Python: 3.10, 3.11, 3.12 중 선택
- database는 실무 운영 환경 기준으로 선택 (H2 같은 테스트용 제외)
- project_name은 snake_case로
- 명시되지 않은 값은 실무 관점에서 합리적으로 추론""",
        ProjectConfig,
    )

print(f"언어: {config.language.value} {config.version}")
print(f"프레임워크: {config.framework}")
print(f"데이터베이스: {config.database.value}")
print(f"프로젝트명: {config.project_name}")
print()
print("JSON 출력:")
print(config.model_dump_json(indent=2))
