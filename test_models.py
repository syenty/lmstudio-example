"""로드된 모델 확인"""
import lmstudio as lms

# 로드된 모델 목록 확인
loaded_models = lms.list_loaded_models()

print(f"📦 로드된 모델 수: {len(loaded_models)}\n")

for i, model in enumerate(loaded_models, 1):
    print(f"{i}. {model}")
