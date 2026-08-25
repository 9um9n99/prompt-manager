prompts = [
    {
        "title": "케이스 스터디 스토리라인 구성",
        "content": "당신은 시니어 프로덕트 디자이너이자 포트폴리오 멘토입니다. 제가 진행한 프로젝트의 배경/문제/과정/결과를 입력하면, Problem-Process-Result 구조로 케이스 스터디 초안을 작성해주세요. 채용 담당자가 3초 안에 프로젝트의 임팩트를 파악할 수 있도록 첫 문장을 강렬하게 만들어주세요.",
        "category": "텍스트 생성",
        "favorite": False
    },
    {
        "title": "신입 지원자 페르소나 관점 리뷰",
        "content": "당신은 15년 경력의 UX 채용 담당자입니다. 제가 공유하는 포트폴리오 프로젝트 설명을 이 페르소나의 시각으로 읽고, (1)가장 먼저 눈에 띄는 강점 (2)의사결정 과정이 불명확한 부분 (3)추가로 궁금한 질문 3가지를 제시해주세요.",
        "category": "페르소나",
        "favorite": False
    },
    {
        "title": "디자인 결정 근거 정리",
        "content": "당신은 디자인 리드입니다. 제가 내린 디자인 결정과 그 이유를 두서없이 입력하면, '왜 이렇게 디자인했는가'를 논리적으로 설명하는 문단으로 정리해주세요. 포트폴리오 면접에서 구두로 설명할 수 있는 수준의 명확한 근거를 포함해주세요.",
        "category": "기타",
        "favorite": False
    }
]

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
            print("프롬프트 추가 기능 (아직 미구현)")
        elif choice == "2":
            print("프롬프트 목록 기능 (아직 미구현)")
        elif choice == "3":
            print("카테고리별 조회 기능 (아직 미구현)")
        elif choice == "4":
            print("프롬프트 검색 기능 (아직 미구현)")
        elif choice == "5":
            print("상세 보기 기능 (아직 미구현)")
        elif choice == "6":
            print("즐겨찾기 관리 기능 (아직 미구현)")
        elif choice == "7":
            print("즐겨찾기 목록 기능 (아직 미구현)")
        elif choice == "0":
            print("프로그램을 종료합니다.")
            break
        else:
            print("잘못된 입력입니다. 다시 선택해주세요.")

main()