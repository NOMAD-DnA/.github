<div align="center">

# NOMAD-DnA

### 함께 설계하고, 구현하고, 검증하는 임베디드 프로젝트 팀

**LIG The SSEN Embedded School 4기 · Team NOMAD**

아이디어와 결정은 문서로, 구현과 검증은 코드로 기록합니다.  
작은 변경을 함께 리뷰하며, 안정적이고 재현 가능한 결과물을 만들어갑니다.

[프로젝트 Notion](https://app.notion.com/p/LIG-3da8c89402ea807c8a54c03691d0179c) · [팀 저장소](https://github.com/orgs/NOMAD-DnA/repositories) · [Git 실전 가이드](https://github.com/NOMAD-DnA/.github/blob/main/docs/GIT_GUIDE.md) · [협업 규칙](https://github.com/NOMAD-DnA/.github/blob/main/CONTRIBUTING.md)

</div>

---

## 🧭 처음 합류했다면

**환경을 준비하고 → 작업을 정하고 → 작은 PR부터 시작하세요.**

1. **팀의 방향 확인하기**  
   [프로젝트 Notion](https://app.notion.com/p/LIG-3da8c89402ea807c8a54c03691d0179c)에서 프로젝트 맥락과 기록을 확인합니다. 접근 권한이 없다면 팀에 요청하세요.
2. **개발 환경 준비하기**  
   [Git 실전 가이드](https://github.com/NOMAD-DnA/.github/blob/main/docs/GIT_GUIDE.md)를 따라 Git 설정과 인증을 준비하고, 작업할 저장소의 README에서 빌드·실행 방법을 확인합니다.
3. **작업 범위 맞추기**  
   해당 저장소에 이슈를 작성하고 담당자·작업 범위·완료 조건을 정합니다.
4. **브랜치에서 작업하고 리뷰받기**  
   최신 main에서 작업 브랜치를 만들고, 변경과 검증 결과를 PR로 공유합니다.

## 📚 필요한 문서 바로 찾기

| 문서 | 이런 때 확인하세요 |
| :--- | :--- |
| **[Git 실전 가이드](https://github.com/NOMAD-DnA/.github/blob/main/docs/GIT_GUIDE.md)** | 최초 설정, clone·commit·push, 충돌 해결, stash, 되돌리기가 필요할 때 |
| **[팀 협업 규칙](https://github.com/NOMAD-DnA/.github/blob/main/CONTRIBUTING.md)** | 브랜치 이름, 커밋 메시지, 이슈·PR 작성, 리뷰·병합 기준을 확인할 때 |
| **[운영 설정 체크리스트](https://github.com/NOMAD-DnA/.github/blob/main/docs/REPOSITORY_SETUP.md)** | 저장소 권한, main 보호, 병합 방식, CI 설정을 점검할 때 |
| **[협업 가이드 전체 안내](https://github.com/NOMAD-DnA/.github/blob/main/README.md)** | Git 기본 개념과 공통 문서의 구성을 한 번에 살펴볼 때 |

## 🤝 우리는 이렇게 협업합니다

**branch → PR → review → merge**

작업 브랜치에서 변경을 올리고, PR 리뷰 후 **일반 Merge commit**으로 병합합니다. Squash merge와 Rebase merge는 사용하지 않습니다.

| 단계 | 할 일 | 남길 기록 |
| :--- | :--- | :--- |
| **01 · 작업 정의** | 이슈에서 문제와 범위를 맞춥니다. | 배경 · 담당자 · 완료 조건 |
| **02 · 구현** | 최신 main에서 작업 브랜치를 만들고 작은 단위로 commit·push합니다. | 목적이 분명한 변경 이력 |
| **03 · 검증과 리뷰** | PR을 열고 테스트 결과와 리뷰 요청 사항을 공유합니다. | 검증 결과 · 미검증 항목 · 피드백 |
| **04 · 병합과 정리** | 리뷰와 필요한 검사를 확인한 뒤 병합하고 main을 갱신합니다. | 완료된 이슈 · 최신 문서 |

> **commit은 내 컴퓨터에 기록, push는 GitHub에 업로드, PR은 리뷰와 병합 요청입니다.**  
> 작업 브랜치를 push해도 main에 자동으로 합쳐지지는 않습니다.

### 매번 지키는 다섯 가지

- **main은 기준 상태로 유지합니다.** 변경은 작업 브랜치와 PR로 제안합니다.
- **하나의 작업에는 하나의 목적을 담습니다.** 작은 변경일수록 리뷰와 문제 추적이 쉽습니다.
- **검증 결과를 구체적으로 남깁니다.** 실행한 테스트와 실행하지 못한 테스트를 구분합니다.
- **결정의 이유를 기록합니다.** 채팅에서 합의한 내용도 이슈·PR·문서에 요약합니다.
- **민감정보를 올리지 않습니다.** 토큰·비밀번호·개인정보와 비공개 자료의 포함 여부를 확인합니다.

## 🛠️ 작업 전 짧은 참고

<details>
<summary><strong>브랜치와 커밋은 어떻게 이름 짓나요?</strong></summary>

브랜치는 작업 목적에 맞게 영문 소문자와 하이픈으로 작성합니다.

| 작업 | 브랜치 예시 | 커밋 메시지 예시 |
| :--- | :--- | :--- |
| 기능 추가 | `feat/sensor-parser` | `feat: 센서 데이터 파서 추가` |
| 오류 수정 | `fix/timeout-handling` | `fix: 통신 타임아웃 처리 수정` |
| 문서 정리 | `docs/setup-guide` | `docs: 개발 환경 설정 안내 추가` |
| 구조 개선 | `refactor/driver-interface` | `refactor: 드라이버 인터페이스 정리` |
| 테스트 추가 | `test/parser-cases` | `test: 빈 입력 검증 케이스 추가` |

연결된 이슈가 있다면 `feat/12-sensor-parser`처럼 **실제 이슈 번호**를 포함할 수 있습니다. 예시 번호를 그대로 사용하지 마세요.

</details>

<details>
<summary><strong>PR에는 무엇을 적어야 하나요?</strong></summary>

- **목적:** 어떤 문제를 해결했는가?
- **변경:** 어떤 기능·파일·인터페이스가 바뀌었는가?
- **검증:** 어떤 환경에서 무엇을 실행했고, 결과는 어떠한가?
- **제약:** 아직 확인하지 못한 부분과 위험 요소는 무엇인가?
- **연결:** 관련 이슈와 특히 리뷰받고 싶은 부분은 무엇인가?

임베디드·펌웨어 변경은 보드/장치, 툴체인·펌웨어 버전, 실행 명령과 시험 조건을 함께 기록합니다. 단위 테스트 통과와 실제 장치 검증 완료는 구분합니다.

</details>

<details>
<summary><strong>충돌이나 push 오류가 나면 어떻게 하나요?</strong></summary>

먼저 `git status`와 오류 메시지를 확인합니다. 다른 팀원의 변경을 강제로 덮어쓰지 않습니다.

- **충돌:** 두 변경의 의도를 확인하고 합친 뒤 다시 검증합니다.
- **push 거절:** 원격 변경, 인증·권한, 브랜치 보호 중 어떤 문제인지 구분합니다.
- **되돌리기:** 미커밋 변경과 이미 공유한 커밋은 복구 방법이 다릅니다.
- **도움 요청:** 오류 메시지와 현재 브랜치·작업 상태를 공유하되 인증정보는 제거합니다.

상황별 명령어는 [Git 실전 가이드](https://github.com/NOMAD-DnA/.github/blob/main/docs/GIT_GUIDE.md)를 참고하세요. `force push`나 `reset --hard`부터 실행하지 않습니다.

</details>

---

### 새 프로젝트 준비

[프로젝트 README 작성 틀](https://github.com/NOMAD-DnA/.github/blob/main/docs/PROJECT_README_TEMPLATE.md)에 목표·담당 모듈·개발 환경·시험 절차를 정리하세요. 구체적인 프로젝트 소개와 팀원 역할은 합의된 정보를 바탕으로 갱신합니다.

### 운영 안내

기본 운영 기준은 **PR → 작성자 외 승인 1명 이상 → 검사 통과 → 일반 Merge commit 병합**입니다. [운영 안내](https://github.com/NOMAD-DnA/.github/blob/main/docs/REPOSITORY_SETUP.md)에서 템플릿·문서 CI와 설정 점검 방법을 확인하세요.

이 `.github` 저장소는 조직 소개와 공통 협업 지침을 관리합니다. **프로젝트별 설치·빌드·실행·테스트 방법은 해당 저장소 README**를 기준으로 확인하세요.

<div align="center">

**함께 만들고, 함께 검증하고, 다음 사람이 이어갈 수 있도록 기록합니다.**

</div>
