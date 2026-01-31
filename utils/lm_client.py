import lmstudio as lms


class LMClient:
    """LM Studio 클라이언트 래퍼 클래스"""

    def __init__(self, model_name: str | None = None):
        self.model_name = model_name
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
