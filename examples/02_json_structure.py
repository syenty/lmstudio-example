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


class BuildTool(str, Enum):
    # Java
    MAVEN = "Maven"
    GRADLE = "Gradle"
    # Python
    POETRY = "Poetry"
    UV = "uv"
    # Node
    NPM = "npm"
    PNPM = "pnpm"


class Architecture(str, Enum):
    MONOLITH = "Monolith"
    MICROSERVICE = "Microservice"
    LAYERED = "Layered"


class ProjectConfig(BaseModel):
    """프로젝트 설정 스키마"""

    # 기본 정보
    project_name: str = Field(description="프로젝트 이름 snake_case (예: order_service)")
    description: str = Field(description="프로젝트 설명 한 줄")

    # 언어 & 프레임워크
    language: Language = Field(description="프로그래밍 언어")
    version: str = Field(description="언어 버전")
    framework: str = Field(description="프레임워크")
    build_tool: BuildTool = Field(description="빌드 도구")

    # 데이터베이스 & ORM
    database: Database = Field(description="데이터베이스")
    orm: str = Field(description="ORM (예: JPA, SQLAlchemy, Prisma)")

    # 아키텍처 & 기능
    architecture: Architecture = Field(description="아키텍처 패턴")
    features: list[str] = Field(
        description="필요 기능 키워드만 (예: auth, swagger, docker, logging, testing, ci-cd)"
    )


# 사용자 요구사항
user_request = "SpringBoot로 주문 관리 서비스 프로젝트 구성해줘. 인증이랑 swagger 문서화 필요해"

PROMPT = """당신은 시니어 소프트웨어 아키텍트입니다.
사용자의 요구사항을 분석하여 프로젝트 설정을 도출해주세요.

## 요구사항
{request}

## 핵심 원칙
1. **명시된 것은 그대로**: 사용자가 구체적으로 언급한 기술은 반드시 반영
2. **명시되지 않은 것은 인기 스택**: 언급되지 않은 부분은 가장 널리 쓰이는 기술 선택

## 기본 선택 기준 (명시되지 않았을 때)
- Java 프로젝트: SpringBoot + Gradle + JPA + PostgreSQL
- Python 프로젝트: FastAPI + Poetry + SQLAlchemy + PostgreSQL
- TypeScript 프로젝트: Express/NestJS + pnpm + Prisma + PostgreSQL
- 버전: 숫자만 (예: 21, 3.12)
- features: 소문자 키워드만 (auth, swagger, docker, logging, testing, validation)

## 예시
요구사항: "주문 서비스 만들어줘" (추상적)
→ 가장 인기 있는 스택 선택: Java 21 + SpringBoot + Gradle + PostgreSQL

요구사항: "FastAPI랑 MySQL로 주문 서비스 만들어줘" (구체적)
→ 명시된 대로: Python + FastAPI + MySQL
"""

with LMClient() as lm:
    config = lm.respond_structured(
        PROMPT.format(request=user_request),
        ProjectConfig,
    )

print("=" * 50)
print(f"📦 {config.project_name}")
print(f"   {config.description}")
print("=" * 50)
print(f"언어: {config.language.value} {config.version}")
print(f"프레임워크: {config.framework}")
print(f"빌드 도구: {config.build_tool.value}")
print(f"DB: {config.database.value} + {config.orm}")
print(f"아키텍처: {config.architecture.value}")
print(f"기능: {', '.join(config.features)}")
print()
print("JSON 출력:")
print(config.model_dump_json(indent=2))
