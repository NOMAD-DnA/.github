# NOMAD-DnA 협업 가이드

> LIG The SSEN Embedded School 4기 · Team NOMAD  
> 함께 설계하고, 구현하고, 검증하기 위한 Git · GitHub 사용 안내입니다.

## 처음이라면 여기부터

1. [Git 실전 가이드](docs/GIT_GUIDE.md)에서 최초 설정과 작업 흐름을 따라 합니다.
2. [협업 규칙](CONTRIBUTING.md)에서 브랜치·커밋·이슈·PR 작성 기준을 확인합니다.
3. 저장소 관리자는 [운영 설정 체크리스트](docs/REPOSITORY_SETUP.md)를 확인합니다.

기본 운영 기준은 **이슈 기반 작업 → PR 리뷰 → 승인 1명 이상 → 검사 통과 → Squash 병합**입니다. 이 저장소의 CI와 템플릿, 설정 점검 방법은 [운영 안내](docs/REPOSITORY_SETUP.md)를 확인합니다.

## 작업 흐름 한눈에 보기

이슈 작성 → 최신 main 확인 → 작업 브랜치 생성 → 수정·테스트 → commit → push → PR → 리뷰·수정 → merge → 최신 main으로 다음 작업

| 개념 | 의미 | 어디에 반영되나요? |
| --- | --- | --- |
| `clone` | 저장소를 처음 내려받기 | 내 컴퓨터 |
| `add` | 다음 커밋에 넣을 변경 선택 | 내 컴퓨터의 스테이징 영역 |
| `commit` | 선택한 변경을 설명과 함께 기록 | 내 컴퓨터의 현재 브랜치 |
| `push` | 로컬 커밋을 GitHub에 업로드 | 원격의 해당 브랜치 |
| Pull Request(PR) | 변경 설명과 리뷰를 포함한 병합 요청 | GitHub |
| `merge` | 브랜치의 변경을 다른 브랜치에 통합 | 병합 대상 브랜치 |
| `fetch` | 원격 변경 이력만 가져오기 | 작업 파일은 그대로 유지 |
| `pull` | 원격 변경을 가져와 현재 브랜치에 통합 | 내 컴퓨터의 현재 브랜치 |

**commit은 업로드가 아니고, push는 main 병합이 아닙니다.** 작업 브랜치를 push한 뒤 PR을 열어 리뷰받습니다.

## 가장 중요한 약속

- main은 실행·검증 가능한 기준 상태로 유지하고, 변경은 작업 브랜치와 PR로 제안합니다.
- 하나의 이슈·PR에는 하나의 목적을 담습니다.
- 커밋 전 변경 내용을 확인하고, PR에는 테스트 결과와 미검증 항목을 적습니다.
- 비밀번호·토큰·개인정보·민감한 프로젝트 자료는 올리지 않습니다.
- 충돌이나 push 거절이 발생하면 강제로 덮어쓰지 않고 원인을 먼저 확인합니다.

## 이 저장소의 역할

- `profile/README.md`: GitHub 조직 홈에 표시되는 기존 팀 소개입니다.
- `README.md`: 협업 문서의 시작점입니다.
- `CONTRIBUTING.md`: 조직 공통 기여·협업 지침입니다.
- `docs/`: 상세 명령어와 관리자 설정 안내입니다.

공개 `.github` 저장소의 `CONTRIBUTING.md`는 자체 기여 지침이 없는 조직 저장소에 기본 안내로 사용될 수 있습니다. 각 프로젝트의 빌드·실행·시험 방법은 **해당 저장소 README**에 작성하고, 프로젝트별 별도 규칙이 있으면 함께 확인합니다.

## 새 프로젝트를 시작할 때

[프로젝트 README 작성 틀](docs/PROJECT_README_TEMPLATE.md)에 목표·담당·환경·빌드·검증 방법을 기록하세요. 프로젝트별 담당자와 명령어는 실제 확인 후 작성합니다.

## 공식 참고 자료

- [GitHub Flow](https://docs.github.com/en/get-started/using-github/github-flow)
- [조직 공통 커뮤니티 파일](https://docs.github.com/en/communities/setting-up-your-project-for-healthy-contributions/creating-a-default-community-health-file)
