"""LM Studio 연결 테스트"""
import lmstudio as lms

# 1. 서버 연결 확인
print("🔍 LM Studio 서버 확인 중...")
api_host = lms.Client.find_default_local_api_host()

if api_host:
    print(f"✅ 서버 발견: {api_host}")
else:
    print("❌ LM Studio 서버를 찾을 수 없습니다.")
    print("   → LM Studio 앱을 실행하고 모델을 로드해주세요.")
    exit(1)

# 2. 간단한 응답 테스트
print("\n🤖 모델 응답 테스트...")
model = lms.llm()
response = model.respond("안녕! 한 문장으로 자기소개 해줘.")
print(f"응답: {response}")
