# Git 실전 가이드

처음에는 아래 순서대로 진행합니다. 이 가이드의 `.github` 예시는 **협업 문서 저장소**를 대상으로 합니다. 실제 코드 작업에서는 해당 프로젝트의 저장소 URL을 사용하세요.

기본 협업 흐름은 **branch → PR → review → merge**이며, 마지막 병합은 **일반 Merge commit**을 사용합니다.

## 1. 최초 1회 설정

Git을 설치한 뒤 터미널에서 확인합니다.

```bash
git --version
git config --global user.name "본인 이름"
git config --global user.email "GitHub에 등록한 이메일"
git config --global --get user.name
git config --global --get user.email
```

이름과 이메일은 커밋 작성자 정보이며 로그인 정보가 아닙니다. 이메일 공개가 걱정된다면 GitHub Settings → Emails에서 **본인 계정에 표시된 no-reply 이메일**을 사용합니다. 공용 PC에서는 global 설정 대신 저장소 안에서 `--global`을 빼고 설정합니다.

GitHub 조직 초대를 수락하고 해당 저장소 쓰기 권한이 있는지도 확인합니다. HTTPS 로그인은 Git Credential Manager 등의 브라우저 인증이나 적절한 토큰을 사용합니다. GitHub 계정 비밀번호를 Git의 HTTPS 인증 비밀번호로 사용하지 않습니다. 토큰을 명령어·원격 URL·문서에 붙여 넣지 마세요.

## 2. 저장소 내려받기

```bash
git clone https://github.com/NOMAD-DnA/.github.git
cd .github
git remote -v
git status
```

`clone`은 보통 최초 한 번만 수행합니다. 이미 clone한 저장소는 해당 폴더에서 갱신하면 됩니다. `origin`은 이 원격 저장소에 붙은 기본 별칭입니다.

## 3. 작업 시작: 최신 main에서 새 브랜치

먼저 `git status`로 저장하지 않은 변경이 없는지 확인합니다. 변경이 남아 있다면 커밋하거나 아래 stash 절차로 보관한 뒤 진행합니다.

```bash
git switch main
git pull --ff-only origin main
git switch -c docs/update-workflow
```

`docs/update-workflow`는 예시 이름입니다. 새 작업마다 목적에 맞는 이름을 정합니다. `--ff-only`는 이력이 갈라졌을 때 임의로 병합하지 않고 멈추게 합니다. 이때는 강제로 맞추지 말고 로컬 main에 별도 커밋이 있는지 확인합니다.

## 4. 변경 확인 → add → commit

파일을 수정한 뒤 다음을 실행합니다.

```bash
git status
git diff
git add README.md
git diff --staged
git commit -m "docs: 협업 안내 보완"
```

- `git diff`: 아직 스테이징하지 않은 변경을 확인합니다.
- `git add README.md`: 지정한 파일의 현재 변경을 커밋 대상으로 선택합니다. 실제 수정한 경로로 바꿉니다.
- `git diff --staged`: 이번 커밋에 들어갈 변경을 확인합니다.
- `git commit`: 선택한 변경을 로컬 이력에 기록합니다.

새 파일은 `git diff`에 내용이 나오지 않을 수 있으므로 `git status`와 파일 내용도 확인합니다. 처음에는 `git add .`로 모두 담기보다 파일을 명시하는 습관을 권장합니다. add 후 파일을 다시 수정했다면 새 수정분을 포함하려고 다시 add해야 합니다.

## 5. push로 GitHub에 업로드

처음 올리는 브랜치:

```bash
git push -u origin docs/update-workflow
```

같은 브랜치의 이후 변경:

```bash
git push
```

`-u`는 로컬 브랜치와 원격 브랜치의 추적 관계를 설정합니다. push는 **현재 작업 브랜치를 업로드하는 것**이며 main에 자동 반영되지 않습니다.

## 6. PR 열기와 리뷰 수정

1. GitHub 저장소에서 Compare & pull request 또는 Pull requests → New pull request를 선택합니다.
2. base는 `main`, compare는 본인 작업 브랜치인지 확인합니다.
3. 변경 목적·주요 변경·테스트 결과·관련 이슈를 작성합니다.
4. 개발 중이면 Draft, 검토 준비가 되었으면 리뷰어를 지정합니다.
5. 리뷰 피드백을 반영하고 같은 브랜치에서 add → commit → push합니다.

추가 push는 기존 PR에 자동 반영되므로 리뷰 수정마다 새 PR을 만들 필요는 없습니다.

### 리뷰 후 일반 merge로 병합하기

1. 작성자 외 팀원의 승인, 필요한 CI 통과, 리뷰 대화 해결, 충돌 없음 상태를 확인합니다.
2. GitHub PR에서 **Create a merge commit** 방식을 선택합니다.
3. **Merge pull request**를 누르고 병합 메시지를 확인한 뒤 **Confirm merge**합니다.
4. PR이 **Merged** 상태인지 확인하고 아래 절차로 로컬 main을 갱신합니다.

**Squash and merge / Rebase and merge는 사용하지 않습니다.** 일반 merge는 기존 커밋들을 유지하고 병합 커밋을 추가합니다. 터미널에서 main을 직접 병합·push하여 PR 리뷰 절차를 생략하지 않습니다.

## 7. main 변경을 작업 브랜치에 반영하기

다른 팀원의 작업이 main에 먼저 반영되었거나 PR에 충돌 표시가 나타났을 때 사용합니다. 현재 변경은 먼저 커밋하고, 본인 브랜치 이름으로 바꿔 실행합니다.

```bash
git switch docs/update-workflow
git fetch origin
git merge origin/main
```

충돌이 없다면 빌드·테스트 후 `git push`합니다. 이 가이드에서는 초보자가 공유 이력을 다시 쓰지 않도록 rebase 대신 merge를 기본으로 설명합니다.

### 충돌이 생겼을 때

`git status`로 충돌 파일을 찾고 파일의 표시를 확인합니다.

```text
<<<<<<< HEAD
현재 작업 브랜치의 내용
=======
가져온 브랜치의 내용
>>>>>>> origin/main
```

1. 두 변경의 의도를 확인합니다. 다른 사람의 코드를 이해하지 못하면 작성자와 상의합니다.
2. 필요한 내용을 합쳐 최종 형태로 수정하고 충돌 표시를 모두 제거합니다.
3. 수정한 파일을 저장한 뒤 다음을 실행합니다. 아래 경로는 실제 충돌 파일로 바꿉니다.

```bash
git add README.md
git diff --staged
git merge --continue
git status
```

이후 관련 테스트를 실행하고 `git push`합니다. 도구의 Accept ours/theirs를 의미 확인 없이 선택하면 다른 변경이 누락될 수 있습니다.

**이번 병합을 취소하고 싶다면**, 병합 진행 중에 다음을 실행합니다.

```bash
git merge --abort
```

병합 전 미커밋 변경이 있으면 복구가 복잡해질 수 있으므로 병합 전에 작업을 커밋해 두는 것이 중요합니다.

## 8. 병합 후 정리

GitHub에서 PR이 **Merged** 상태인지 먼저 확인합니다.

```bash
git switch main
git pull --ff-only origin main
git fetch --prune
git branch -d docs/update-workflow
```

원격 브랜치는 GitHub PR 화면에서 Delete branch로 삭제할 수 있습니다. `fetch --prune`은 이미 삭제된 원격 브랜치의 로컬 추적 정보만 정리하며, 로컬 작업 브랜치 자체를 삭제하지 않습니다.

`git branch -d`가 거절되면 PR 병합 여부, 최신 main 반영 여부, 작업 브랜치의 추가 미반영 커밋을 확인합니다. 강제 삭제하지 말고 확신이 없으면 브랜치를 남겨 두세요. 다음 작업은 갱신된 main에서 새 브랜치를 만듭니다.

## 9. 자주 만나는 문제

### push가 non-fast-forward로 거절됨

원격의 같은 브랜치에 로컬에 없는 커밋이 있을 수 있습니다. 본인 작업 브랜치에서 변경을 먼저 커밋하고 다음을 실행합니다.

```bash
git fetch origin
git merge origin/docs/update-workflow
```

충돌을 해결하고 테스트한 뒤 다시 push합니다. 위 브랜치명은 본인 브랜치로 바꿉니다. 단순 권한 오류·브랜치 보호 오류는 이 방법으로 해결되지 않으므로 오류 메시지를 구분합니다. **거절을 해결하려고 force push하지 않습니다.**

### Permission denied / 403 / Repository not found

URL, 조직 초대 수락 여부, 로그인한 계정, 저장소 권한, 조직의 인증 정책을 확인합니다. 공개 저장소가 보이는 것과 push 권한이 있는 것은 별개입니다. 오류 공유 시 토큰이나 자격증명은 제거합니다.

### 브랜치를 바꾸려는데 로컬 변경 때문에 실패함

현재 작업을 커밋하거나 임시 보관합니다.

```bash
git stash push -u -m "작업 브랜치 전환 전 임시 보관"
git stash list
```

원래 작업 브랜치로 돌아온 뒤:

```bash
git stash pop
```

`-u`는 아직 추적되지 않은 파일도 포함하지만 ignore된 파일까지 담지는 않습니다. stash는 로컬 임시 보관이며 원격 백업이 아닙니다. pop 과정에서도 충돌이 생길 수 있습니다.

### 실수로 main에서 파일을 수정함

아직 커밋하지 않았다면 새 작업 브랜치를 만들고 그 브랜치에서 커밋합니다.

```bash
git switch -c fix/my-change
```

main에 이미 커밋했거나 push했다면 상태에 따라 복구 방식이 달라집니다. 먼저 `git status`, `git log --oneline -5`로 상태를 확인하고 담당자와 복구 방법을 정합니다. `reset --hard`나 force push로 급하게 지우지 않습니다.

## 10. 되돌리기는 범위를 구분하기

| 상태 | 방법 | 주의 |
| --- | --- | --- |
| add만 취소 | `git restore --staged README.md` | 작업 파일 내용은 유지 |
| 미커밋 파일 수정 폐기 | `git restore README.md` | 스테이징 영역 기준으로 파일을 복원하므로 미스테이징 수정이 사라짐 |
| 공유된 일반 커밋 취소 | 작업 브랜치에서 `git revert 커밋SHA` 후 PR | 기존 이력을 지우지 않고 반대 변경을 새 커밋으로 기록 |

경로와 SHA는 실제 대상으로 바꿉니다. restore는 복구하기 어려운 변경 폐기가 될 수 있으니 먼저 diff를 확인합니다. merge 커밋을 되돌리는 경우에는 부모 선택 등 추가 판단이 필요하므로 일반 revert 예시를 그대로 적용하지 않습니다.

## 11. 매번 확인할 체크리스트

**커밋 전:** 현재 브랜치 확인 / diff 확인 / 필요한 파일만 add / 비밀정보 확인  
**PR 전:** 최신 main과 호환 / 빌드·테스트 / 변경 목적·검증·미검증 항목 작성  
**병합 전:** 리뷰 완료 / 필수 수정 해결 / 설정된 CI 확인 / 충돌 없음  
**병합 후:** main 갱신 / 이슈·문서 확인 / 다음 작업은 새 브랜치

## 공식 참고 자료

- [Git 다운로드](https://git-scm.com/downloads)
- [GitHub Flow](https://docs.github.com/en/get-started/using-github/github-flow)
- [GitHub 인증 방식](https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/about-authentication-to-github)
- [git merge](https://git-scm.com/docs/git-merge)
- [git restore](https://git-scm.com/docs/git-restore)
