prompts = [
    {
        "title": "정하윤 - 디자인 리뷰 회의록 정리 시스템 프롬프트 (v2)",
        "content": "당신은 정하윤입니다. 5년 차 프로덕트 디자이너 출신으로, 현재는 디자인 오퍼레이션 담당자로서 팀 내 디자인 리뷰 회의록 정리를 전담하고 있습니다.\n\n[목표]\n사용자가 제공하는 디자인 리뷰 회의 스크립트를 읽고, 아래 8항목 형식으로 정확하게 요약하는 것이 당신의 유일한 업무입니다.\n\n[전문성 반영]\n디자인 실무 용어(터치 영역, 스테퍼, 반응형, 인터랙션 등)는 풀어서 설명하지 말고 그대로 사용하십시오.\n\n[처리 순서 - 반드시 이 순서를 내부적으로 따르십시오]\n1단계. 입력 확인: 참석자, 리뷰 대상, 스크립트 원문이 모두 존재하는지 먼저 점검하십시오.\n2단계. 발언 분류: 결론이 난 피드백 / 결론이 안 난 피드백 / 발화자 불분명 구간으로 분류하십시오.\n3단계. 항목 작성: 분류를 바탕으로 8항목을 작성하십시오.\n4단계. 자체 검증: 스크립트에 없는 담당자·기한·날짜를 채운 곳이 없는지 확인하고, 있다면 미정으로 수정하십시오.\n\n[안전장치]\n스크립트에 명시되지 않은 정보는 절대 추정해서 채우지 마십시오. 발언자가 불분명한 구간은 화자 불명으로 표시하십시오.",
        "category": "페르소나",
        "favorite": False
    },
    {
        "title": "디자인 리뷰 회의록 8항목 요약 프롬프트",
        "content": "당신은 디자인 리뷰 회의에 참석한 프로덕트 디자이너를 돕는 회의록 정리 도우미입니다.\n아래 회의 스크립트를 읽고, 반드시 아래 8개 항목 형식으로 요약해주세요.\n\n출력 형식 (8항목, 순서대로):\n1. 회의 날짜 / 리뷰 차수\n2. 참석자\n3. 리뷰 대상 (어떤 화면/시안)\n4. 전체 디자인 상태 (승인 / 부분 수정 필요 / 재작업 필요 중 선택)\n5. 피드백별 반영 여부 (반영 확정 / 반려 / 추가 논의 필요로 각각 구분)\n6. Action Items (담당자, 기한 포함)\n7. 이견 / 미합의 지점\n8. 다음 리뷰 일정\n\n규칙:\n- 스크립트에 없는 내용은 지어내지 마세요. 명시되지 않았다면 '미정'이라고 표시하세요.\n- 발언자가 불분명한 구간은 '화자 불명'으로 표시하세요.\n- 결론이 나지 않은 사항은 '추가 논의 필요'로 분류하세요.",
        "category": "텍스트 생성",
        "favorite": False
    },
    {
        "title": "뉴스레터 토픽 추출 프롬프트",
        "content": "다음은 뉴스레터 이메일이야. 이 뉴스레터에서 다루는 토픽(주제)만 bullet point로 추출해줘.\n각 토픽은 한 줄로, 핵심 키워드 위주로 간결하게.\n광고, 구독 안내, 인사말은 무시하고 실제 콘텐츠 주제만 뽑아줘.\n\n이메일 제목: [Subject]\n발신자: [From Name]\n본문: [Body Plain]",
        "category": "자동화",
        "favorite": False
    }
]

def add_prompt():
    print("\n=== 프롬프트 추가 ===")

    title = input("제목: ")
    while title == "":
        print("제목을 입력해주세요.")
        title = input("제목: ")

    content = input("내용: ")
    while content == "":
        print("내용을 입력해주세요.")
        content = input("내용: ")

    categories = ["텍스트 생성", "이미지 생성", "영상 생성", "페르소나", "자동화", "기타"]

    print("\n카테고리 선택:")
    for i in range(len(categories)):
        print(f"{i+1}) {categories[i]}")
    print("직접 입력하려면 카테고리 이름을 그대로 입력하세요.")

    category_input = input("선택: ")

    if category_input in ["1", "2", "3", "4", "5", "6"]:
        category = categories[int(category_input) - 1]
    else:
        category = category_input

    prompts.append({
        "title": title,
        "content": content,
        "category": category,
        "favorite": False
    })

    print(f"\n'{title}' 프롬프트가 추가되었습니다!")

def show_list():
    print("\n=== 프롬프트 목록 ===")
    if len(prompts) == 0:
        print("등록된 프롬프트가 없습니다.")
        return

    for i in range(len(prompts)):
        star = " ⭐" if prompts[i]["favorite"] else ""
        print(f"{i+1}. [{prompts[i]['category']}] {prompts[i]['title']}{star}")

    print(f"\n총 {len(prompts)}개의 프롬프트")

def show_by_category():
    categories = ["텍스트 생성", "이미지 생성", "영상 생성", "페르소나", "자동화", "기타"]

    print("\n=== 카테고리별 조회 ===")
    for i in range(len(categories)):
        print(f"{i+1}) {categories[i]}")

    choice = input("선택: ")

    if choice not in ["1", "2", "3", "4", "5", "6"]:
        print("잘못된 입력입니다.")
        return

    selected_category = categories[int(choice) - 1]

    print(f"\n[{selected_category}] 카테고리 프롬프트:")

    filtered = []
    for p in prompts:
        if p["category"] == selected_category:
            filtered.append(p)

    if len(filtered) == 0:
        print("해당 카테고리에 프롬프트가 없습니다.")
        return

    for i in range(len(filtered)):
        star = " ⭐" if filtered[i]["favorite"] else ""
        print(f"{i+1}. {filtered[i]['title']}{star}")

    print(f"\n총 {len(filtered)}개의 프롬프트")

def search_prompt():
    keyword = input("\n검색어: ")

    results = []
    for p in prompts:
        if keyword in p["title"] or keyword in p["content"]:
            results.append(p)

    print("\n검색 결과:")

    if len(results) == 0:
        print("검색 결과가 없습니다.")
        return

    for i in range(len(results)):
        star = " ⭐" if results[i]["favorite"] else ""
        print(f"{i+1}. [{results[i]['category']}] {results[i]['title']}{star}")

    print(f"\n{len(results)}개의 프롬프트를 찾았습니다.")

def show_detail():
    show_list()

    num = input("\n번호 입력: ")

    if not num.isdigit():
        print("잘못된 번호입니다.")
        return

    index = int(num) - 1

    if index < 0 or index >= len(prompts):
        print("잘못된 번호입니다.")
        return

    p = prompts[index]
    star = "⭐" if p["favorite"] else "표시 안 됨"

    print("─" * 30)
    print(f"제목: {p['title']}")
    print(f"카테고리: {p['category']}")
    print(f"즐겨찾기: {star}")
    print("─" * 30)
    print("내용:")
    print(p["content"])
    print("─" * 30)

def toggle_favorite():
    show_list()

    num = input("\n프롬프트 번호 입력: ")

    if not num.isdigit():
        print("잘못된 번호입니다.")
        return

    index = int(num) - 1

    if index < 0 or index >= len(prompts):
        print("잘못된 번호입니다.")
        return

    p = prompts[index]

    if p["favorite"]:
        p["favorite"] = False
        print(f"\n'{p['title']}' 프롬프트를 즐겨찾기에서 해제했습니다!")
    else:
        p["favorite"] = True
        print(f"\n'{p['title']}' 프롬프트를 즐겨찾기에 추가했습니다!")


def show_favorites():
    favorites = []
    for p in prompts:
        if p["favorite"]:
            favorites.append(p)

    print("\n=== 즐겨찾기 목록 ===")

    if len(favorites) == 0:
        print("즐겨찾기한 프롬프트가 없습니다.")
        return

    for i in range(len(favorites)):
        print(f"{i+1}. [{favorites[i]['category']}] {favorites[i]['title']} ⭐")

    print(f"\n총 {len(favorites)}개의 즐겨찾기")

def show_menu():
    print("\n=== 나만의 프롬프트 관리 ===")
    print("1. 프롬프트 추가")
    print("2. 프롬프트 목록")
    print("3. 카테고리별 조회")
    print("4. 프롬프트 검색")
    print("5. 프롬프트 상세 보기")
    print("6. 즐겨찾기 관리")
    print("7. 즐겨찾기 목록")
    print("0. 종료")

def main():
    while True:
        show_menu()
        choice = input("선택: ")

        if choice == "1":
            add_prompt()
        elif choice == "2":
            show_list()
        elif choice == "3":
            show_by_category()
        elif choice == "4":
            search_prompt()
        elif choice == "5":
            show_detail()
        elif choice == "6":
            toggle_favorite()
        elif choice == "7":
            show_favorites()
        elif choice == "0":
            print("프로그램을 종료합니다.")
            break
        else:
            print("잘못된 입력입니다. 다시 선택해주세요.")

main()