# 🤖 AI Engine Project

## 프로젝트 개요
두 개의 애플리케이션을 지원하는 공통 AI 엔진:
1. **IWL (IdeaWorkLab)** - 아이디어 워크플로우 플랫폼
2. **한자 수업 앱** - 한자 학습 애플리케이션

## 팀 구성 (Tab 2)
| Session | Name | Tool | Role |
|---------|------|------|------|
| 2-1 | 🌟 Gemini - AI Engine | Gemini | 데이터 처리 & LLM 통합 |
| 2-2 | codex | Codex | 백엔드 개발 |
| 2-3 | 🔧 Claude - Integration | Claude | 시스템 통합 (PM 아님!) |

**중요**: PM은 Tab 1-1에만 있습니다. Tab 2-3 Claude는 Integration Engineer입니다.

## 프로젝트 구조
```
ai-engine-project/
├── core/              # 공통 AI 처리 로직
│   ├── llm/          # LLM 통합 (Claude, GPT, Gemini)
│   ├── memory/       # 컨텍스트 관리
│   └── reasoning/    # 추론 엔진
├── adapters/         # 앱별 어댑터
│   ├── iwl/         # IWL 전용 로직
│   └── hanja/       # 한자 앱 전용 로직
└── api/             # 공통 API 엔드포인트
```

## 작업 프로세스
1. **시그널 시스템**: [ACK] → [START] → [DONE] PR#
2. **GitHub Flow**: Issue → Branch → PR → Review → Merge
3. **팀 협업**: PM(Tab 1) → 팀원(Tab 2) → 실행

## 기술 스택
- **Backend**: Python 3.9+, FastAPI
- **LLM Integration**: OpenAI, Anthropic, Google AI
- **Database**: PostgreSQL / MongoDB
- **Cache**: Redis
- **Queue**: RabbitMQ / Celery

## PM 연락처
- **위치**: Tab 1-1
- **역할**: 프로젝트 매니저 & 조율