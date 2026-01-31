import os

import lmstudio as lms
from dotenv import load_dotenv

load_dotenv()


class LMClient:
    """LM Studio 클라이언트 래퍼 클래스"""

    def __init__(self, model_name: str | None = None):
        # 우선순위: 인자 > 환경변수 > 자동선택
        self.model_name = model_name or os.getenv("LM_MODEL_NAME")
        self._model = None

    def __enter__(self):
        if self.model_name:
            self._model = lms.llm(self.model_name)
        else:
            self._model = lms.llm()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self._model = None
        return False

    def respond(self, prompt: str) -> str:
        """프롬프트에 대한 응답 생성"""
        if self._model is None:
            raise RuntimeError("LMClient must be used within a context manager")
        return self._model.respond(prompt)

    def complete(self, prompt: str) -> str:
        """텍스트 완성"""
        if self._model is None:
            raise RuntimeError("LMClient must be used within a context manager")
        return self._model.complete(prompt)

    @staticmethod
    def list_models() -> list[str]:
        """로드된 모델 목록 반환"""
        loaded = lms.list_loaded_models()
        return [model.identifier for model in loaded]

    @staticmethod
    def print_models():
        """로드된 모델 목록 출력"""
        models = LMClient.list_models()
        if not models:
            print("❌ 로드된 모델이 없습니다.")
            return
        print(f"📦 로드된 모델 ({len(models)}개):")
        for i, name in enumerate(models, 1):
            print(f"  {i}. {name}")
