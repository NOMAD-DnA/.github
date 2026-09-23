# 저장소 운영 설정과 점검

## 적용 범위

이 저장소는 조직 소개, 공통 협업 안내와 템플릿을 관리합니다. 코드 저장소를 새로 만들면 프로젝트별 설정을 따로 적용해야 합니다.

## 운영 기준

- main 변경은 PR로 제안합니다.
- 작성자 외 쓰기 권한이 있는 팀원 최소 1명이 승인합니다.
- 추가 변경으로 기존 승인이 무효화되면 재리뷰합니다.
- 리뷰 대화를 해결하고 docs-check 검사를 통과한 뒤 Create a merge commit 방식으로 병합합니다.
- 작성자는 승인·검사 상태를 확인한 뒤 병합합니다. 부재 시 리뷰어와 병합 담당자를 정합니다.
- main 강제 push와 삭제를 제한합니다. 병합된 작업 브랜치 자동 삭제 설정은 변경하지 않으며, 필요하면 병합 확인 후 수동 정리합니다.

위 기준의 실제 강제 여부는 GitHub Settings → Rules → Rulesets와 General에서 확인합니다. 문서와 설정은 별개이며, 설정 변경 PR/작업의 완료 기록을 함께 확인하세요.

## 병합 방식

협업 순서는 **branch → PR → review → merge**입니다. GitHub Settings → General → Pull Requests에서 **Allow merge commits**를 켜고 **Allow squash merging / Allow rebase merging**는 끕니다. PR에서는 **Create a merge commit** 방식으로 병합합니다.

일반 merge와 충돌하는 **Require linear history** 규칙은 사용하지 않습니다. PR·리뷰·검사 요구사항은 병합 방식과 별도로 유지합니다. 이 설정은 저장소별 설정이므로 다른 코드 저장소에도 별도로 적용해야 합니다.

## 추가된 파일

| 파일 | 역할 |
| --- | --- |
| [.github/PULL_REQUEST_TEMPLATE.md](../.github/PULL_REQUEST_TEMPLATE.md) | PR 작성 시 변경 목적·검증·리뷰 항목 제공 |
| [.github/ISSUE_TEMPLATE/](../.github/ISSUE_TEMPLATE/) | 작업 요청·버그 신고·설계 논의 양식 |
| [.github/workflows/docs.yml](../.github/workflows/docs.yml) | PR과 main push에서 문서 검사 |
| [.editorconfig](../.editorconfig) | UTF-8, 들여쓰기, 줄바꿈 기본값 |
| [.gitattributes](../.gitattributes) | Git의 텍스트 줄바꿈 규칙 |
| [.gitignore](../.gitignore) | 인증정보·로컬 설정·Python 임시 파일 제외 |
| [프로젝트 README 작성 틀](PROJECT_README_TEMPLATE.md) | 새 코드 저장소의 환경·구성·검증 안내 |

## 문서 CI

GitHub Actions의 **Documentation checks / docs-check** 작업이 다음을 검사합니다.

- UTF-8, LF, 파일 끝 줄바꿈
- 제목의 기본 공백, 코드 블록 닫힘, 코드 예시 바깥의 충돌 표시
- 일반 Markdown 인라인 링크의 로컬 파일 존재 여부
- 이 저장소 main을 가리키는 절대 GitHub 파일 링크의 실제 대상
- 검사기 자체의 회귀 테스트

외부 웹사이트 연결, 링크의 #앵커, HTML 링크, 참조형 링크, Markdown 전체 문법은 검사하지 않습니다. Notion 접근 권한이나 프로젝트 코드·장치의 정상 작동도 보장하지 않습니다.

Python 3.9 이상에서 저장소 루트에서 실행합니다.

```bash
python -m unittest discover -s tests -v
python scripts/check_docs.py
```

워크플로는 contents: read 권한만 사용하며 checkout 자격증명을 남기지 않습니다. PR 코드는 pull_request 이벤트의 GitHub 호스팅 러너에서 검사하고, 비밀정보가 필요한 검사는 수행하지 않습니다.

## 다른 저장소에 적용할 때

- 공개 .github 저장소의 지원 대상 공통 기여 지침·이슈·PR 템플릿은 자체 파일이 없는 조직 저장소에서 기본값으로 사용될 수 있습니다.
- 기본 파일이 각 저장소 clone에 자동으로 복사되는 것은 아닙니다.
- Ruleset, CI 워크플로, .gitignore, .editorconfig, .gitattributes는 새 코드 저장소에 자동 적용되지 않습니다.
- CODEOWNERS도 조직 공통 기본 파일로 상속되지 않습니다. 담당 모듈과 쓰기 권한을 확인한 뒤 각 저장소에 추가합니다.
- .gitignore는 이미 추적 중인 비밀정보를 제거하지 않습니다. 유출되면 먼저 키를 폐기·재발급합니다.

## 팀 확인이 필요한 정보

- 프로젝트의 구체적인 목표·범위·현재 단계
- 팀원별 담당 모듈과 CODEOWNERS 대상
- 코드 저장소 이름과 실제 빌드·실행·시험 명령
- 실제 보드·센서·툴체인 버전과 대용량 데이터 저장 위치

확인되지 않은 내용을 임의로 작성하지 않습니다. 합의 후 [프로젝트 README 작성 틀](PROJECT_README_TEMPLATE.md)을 채우고 Overview에 요약합니다.

## 공식 참고

- [조직 공통 커뮤니티 파일](https://docs.github.com/en/communities/setting-up-your-project-for-healthy-contributions/creating-a-default-community-health-file)
- [Ruleset](https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/managing-rulesets/about-rulesets)
