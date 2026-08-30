# 나만의 프롬프트 관리 프로그램

GitHub 저장소: https://github.com/9um9n99/prompt-manager

파편화된 AI 프롬프트를 체계적으로 관리하기 위한 Python 콘솔 프로그램입니다.
제목, 내용, 카테고리, 즐겨찾기 여부, 조회수를 하나의 프롬프트 데이터로 저장하고, 메뉴 번호를 입력해 추가, 목록 조회, 카테고리별 조회, 검색, 상세 보기, 즐겨찾기 기능을 사용할 수 있습니다.

## 실행 환경

- Python 3.10 이상 권장
- 별도 외부 패키지 설치 없음
- macOS 터미널 또는 VSCode 터미널에서 실행 가능
- 로컬 확인 환경: Python 3.12.14 (Homebrew로 설치)에서 실행 확인

Git 환경 확인 명령어:

```bash
python3 --version
git --version
git config user.name
git config user.email
```

## 실행 방법

저장소를 클론한 뒤 프로젝트 폴더에서 실행합니다.

```bash
git clone https://github.com/9um9n99/prompt-manager.git
cd prompt-manager
python3 main.py
```

메뉴가 표시되면 원하는 기능의 번호를 입력합니다.

## 기능 목록

| 번호 | 기능 | 설명 |
|---|---|---|
| 1 | 프롬프트 추가 | 제목, 내용, 카테고리를 입력해 새 프롬프트를 등록합니다 |
| 2 | 프롬프트 목록 | 등록된 모든 프롬프트를 번호와 함께 출력합니다 |
| 3 | 카테고리별 조회 | 선택한 카테고리에 속한 프롬프트만 출력합니다 |
| 4 | 프롬프트 검색 | 제목과 내용에서 키워드를 검색합니다 |
| 5 | 프롬프트 상세 보기 | 특정 프롬프트의 전체 내용을 확인합니다 |
| 6 | 즐겨찾기 관리 | 프롬프트를 즐겨찾기에 추가하거나 해제합니다 |
| 7 | 즐겨찾기 목록 | 즐겨찾기한 프롬프트만 모아서 확인합니다 |
| 8 | 조회수 Top 목록 | 상세 조회 횟수가 높은 순서대로 출력합니다 |
| 0 | 종료 | 프로그램을 종료합니다 |

## 기본 데이터

프로그램 시작 시 이전 미션에서 작성한 프롬프트 3개가 기본으로 등록되어 있습니다.

- 정하윤 - 디자인 리뷰 회의록 정리 시스템 프롬프트
- 디자인 리뷰 회의록 8항목 요약 프롬프트
- 뉴스레터 토픽 추출 프롬프트

## 데이터 구조

프롬프트는 리스트 안에 딕셔너리를 넣는 방식으로 관리합니다.

```python
prompts = [
    {
        "title": "프롬프트 제목",
        "content": "프롬프트 내용",
        "category": "카테고리",
        "favorite": False,
        "view_count": 0
    }
]
```

리스트는 여러 프롬프트를 추가한 순서대로 보관하고 반복 처리하기 쉽다는 장점이 있지만, 각 항목의 의미를 이름으로 바로 알기는 어렵습니다. 딕셔너리는 `title`, `content`, `category`처럼 속성 이름을 붙여 데이터를 읽기 쉽게 관리할 수 있다는 장점이 있지만, 여러 개의 프롬프트를 순서대로 모아 다루는 용도로는 리스트보다 불편합니다.

그래서 이 프로젝트에서는 전체 프롬프트 묶음은 리스트로 관리하고, 각 프롬프트 한 개의 세부 정보는 딕셔너리로 관리하는 리스트 안의 딕셔너리 구조를 사용했습니다.

## 카테고리 설계

기본 카테고리는 `DEFAULT_CATEGORIES` 상수에 한 번만 정의했습니다.

- 텍스트 생성
- 이미지 생성
- 영상 생성
- 페르소나
- 자동화
- 기타

프롬프트를 추가할 때는 기본 카테고리 중 하나를 번호로 선택하거나 `직접 입력`을 선택해 새 카테고리를 만들 수 있습니다. 사용자가 직접 만든 카테고리도 이후 카테고리별 조회 메뉴에 함께 표시됩니다.

## 입력 검증

- 제목, 내용, 검색어, 직접 입력 카테고리는 빈 값으로 둘 수 없습니다.
- 이미 등록된 제목을 다시 입력하면 중복 제목으로 처리하고 다른 제목을 다시 입력하게 합니다.
- 카테고리는 화면에 표시된 번호만 선택할 수 있습니다.
- 목록 번호를 입력하는 기능에서는 숫자인지 확인하고, 실제 목록 범위 안에 있는지도 확인합니다.
- 메뉴에 없는 번호나 문자를 입력하면 안내 문구를 출력한 뒤 다시 메뉴로 돌아갑니다.

## 검색 방식

검색은 프롬프트 제목과 내용 전체를 대상으로 합니다. 검색어와 비교 대상 문자열을 모두 소문자로 바꾼 뒤 비교하므로 `test`, `TEST`, `Test`처럼 대소문자가 달라도 같은 결과를 찾을 수 있습니다.

## 함수 역할

| 함수 | 역할 |
|---|---|
| `get_input()` | 빈 값이 들어오지 않도록 반복해서 입력을 받습니다 |
| `title_exists()` | 새 제목이 기존 제목과 중복되는지 확인합니다 |
| `get_all_categories()` | 기본 카테고리와 사용자가 만든 카테고리를 합쳐 반환합니다 |
| `select_category()` | 카테고리 번호 선택과 직접 입력을 처리합니다 |
| `add_prompt()` | 새 프롬프트를 입력받아 리스트에 추가합니다 |
| `show_list()` | 전체 프롬프트 목록을 출력합니다 |
| `show_by_category()` | 선택한 카테고리의 프롬프트만 출력합니다 |
| `search_prompt()` | 제목과 내용에서 검색어를 찾습니다 |
| `show_detail()` | 선택한 프롬프트의 상세 내용을 출력하고 조회수를 증가시킵니다 |
| `toggle_favorite()` | 즐겨찾기 상태를 추가 또는 해제합니다 |
| `show_favorites()` | 즐겨찾기한 프롬프트만 출력합니다 |
| `show_top_viewed()` | 조회수 기준으로 프롬프트를 정렬해 출력합니다 |
| `show_menu()` | 메인 메뉴를 출력합니다 |
| `main()` | 프로그램을 계속 실행하는 전체 반복문을 담당합니다 |

## 반복문 설계

프로그램은 `main()` 함수의 `while True` 반복문으로 계속 실행됩니다. 사용자가 `0`을 입력하면 `break`로 반복문을 종료합니다.

입력 검증이 필요한 곳에서도 반복문을 사용했습니다. 예를 들어 제목이 비어 있거나, 카테고리 번호가 범위를 벗어나거나, 중복 제목이 입력되면 바로 실패시키지 않고 올바른 값을 다시 입력받습니다.

## 저장 방식과 영속화 설계

현재 버전은 과제 요구사항에 맞춰 데이터를 파일에 저장하지 않습니다. 프로그램 실행 중 추가한 프롬프트와 즐겨찾기 상태는 메모리의 `prompts` 리스트에 유지되지만, 프로그램을 종료하면 초기화됩니다.

나중에 영속화 기능을 추가한다면 JSON 파일을 사용하는 방식이 적합합니다. 이유는 현재 데이터가 리스트와 딕셔너리 구조라서 JSON의 배열과 객체 구조로 자연스럽게 저장할 수 있고, 별도 데이터베이스 없이도 Python 기본 모듈 `json`으로 읽고 쓸 수 있기 때문입니다.

예상 확장 방식:

- 시작할 때 `prompts.json` 파일이 있으면 읽어서 `prompts`에 불러오기
- 프롬프트 추가, 즐겨찾기 변경, 조회수 변경 시 JSON 파일에 저장하기
- 파일이 없거나 손상된 경우 기본 프롬프트 3개로 시작하기

## Git 작업 기준

기능 단위로 작게 커밋하는 것을 기준으로 작업했습니다. 예시는 다음과 같습니다.

- 기본 데이터 추가
- 메뉴 뼈대 구현
- 프롬프트 추가 기능 구현
- 목록 보기 기능 구현
- 카테고리별 조회 기능 구현
- 검색 기능 구현
- 상세 보기 기능 구현
- 즐겨찾기 기능 구현
- README 문서 보완
- 버그 수정

커밋 이력은 아래 명령어로 확인할 수 있습니다.

```bash
git log --oneline --graph --all
```

## 저장소 업로드 및 원격 확인 증빙

GitHub 원격 저장소 주소는 다음과 같습니다.

- https://github.com/9um9n99/prompt-manager

로컬 저장소가 원격 저장소와 연결되어 있음을 보여주는 캡처는 저장소 안 `screenshots/repository-remote-evidence.png`에서 확인할 수 있습니다. 이 이미지는 `git remote -v`, `git branch -vv` 실행 결과와 GitHub 저장소 페이지 화면을 담고 있습니다.

```bash
git remote -v
git branch -vv
```

## 공개 샘플 저장소 클론 증빙

이 항목은 위의 사용자 본인 저장소 클론과 별개입니다. 공개 샘플 저장소를 직접 클론하고 구조를 확인한 기록입니다.

- 사용한 공개 샘플 저장소: https://github.com/octocat/Hello-World
- 클론 출력과 `ls -la` 결과는 저장소 안 `screenshots/sample-repo-clone-and-list.png`에서 확인할 수 있습니다.

```bash
mkdir -p ~/Desktop/codyssey-sample-clone-check
cd ~/Desktop/codyssey-sample-clone-check
git clone https://github.com/octocat/Hello-World.git
cd Hello-World
ls -la
```

## 브랜치 전략

기본 작업 브랜치는 `main`입니다. 기능을 보완할 때는 별도 브랜치를 만든 뒤 작업하고, 완료 후 `main`으로 병합합니다.

이번 보완 작업에서는 다음 흐름을 사용했습니다.

```bash
git switch -c feature/prompt-list-improvements
git add main.py
git commit -m "Improve prompt list input handling"
git switch main
git merge --no-ff feature/prompt-list-improvements -m "Merge prompt list improvements"
```

`--no-ff` 옵션을 사용하면 병합 커밋이 남아 브랜치에서 작업한 기록을 `git log --oneline --graph --all` 결과에서 확인하기 쉽습니다.

## 병합 충돌 해결 절차

브랜치를 병합할 때 같은 파일의 같은 줄을 서로 다르게 수정하면 충돌이 날 수 있습니다. 충돌이 발생하면 아래 순서로 해결합니다.

1. `git status`로 충돌 파일을 확인합니다.
2. 충돌 파일을 열어 `<<<<<<<`, `=======`, `>>>>>>>` 표시를 찾습니다.
3. 남길 코드를 직접 선택하고 충돌 표시를 모두 삭제합니다.
4. 프로그램을 실행해 문제가 없는지 확인합니다.
5. `git add 파일명`으로 해결한 파일을 등록합니다.
6. `git commit`으로 병합을 완료합니다.

## 제출 전 증빙 체크리스트

- VSCode에서 `main.py`를 연 화면
- `python3 --version` 실행 결과
- `git --version` 실행 결과
- `git config user.name` 실행 결과
- `git config user.email` 실행 결과
- `git clone https://github.com/9um9n99/prompt-manager.git` 실행 결과
- 클론 후 `ls` 또는 `tree`로 `main.py`, `README.md`, `.gitignore`가 보이는 화면
- `screenshots/repository-remote-evidence.png`: GitHub 저장소 페이지 또는 `git remote -v`, `git branch -vv` 실행 결과
- `screenshots/sample-repo-clone-and-list.png`: 공개 샘플 저장소 `octocat/Hello-World` 클론 출력과 `ls -la` 결과
- `python3 main.py` 실행 후 메인 메뉴 화면
- 프롬프트 추가 화면
- 전체 목록 화면
- 카테고리별 조회 화면
- 검색 결과 화면
- 상세 보기 화면
- 즐겨찾기 추가/해제 화면
- `git log --oneline --graph --all` 실행 결과

## 참고 사항

- 추가한 프롬프트와 즐겨찾기 상태는 프로그램 실행 중에만 유지되며, 종료 시 초기화됩니다.
- 기본 프롬프트 3개는 이전 Codyssey 미션에서 실제로 작성한 프롬프트를 사용했습니다.
