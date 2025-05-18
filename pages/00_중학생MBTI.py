import streamlit as st

# MBTI 진로 추천 데이터 (중학생용: 이미지, 링크, 장점, 보완점 포함)
career_recommendations = {
    "ISTJ": {
        "summary": "책임감이 강하고 계획적인 성격이에요.",
        "jobs": [
            {
                "name": "회계사",
                "desc": "숫자를 정확하게 계산하는 일을 해요.",
                "prep": "1. 수학 교과서를 꼼꼼히 공부해요.\n2. 용돈기입장을 써보며 계산 습관을 길러요.\n3. 가상의 가게를 만들고 수입과 지출을 정리해보세요.",
                "image": "https://cdn.career.go.kr/images/upload/job/120200.jpg",
                "video": "https://www.career.go.kr/cloud/w/interview/jobView?seq=105825&listT=1",  # 예시: 회계사 관련 영상
                "link": "https://www.career.go.kr/cloud/w/job/view?seq=206",
                "strength": "꼼꼼하고 책임감이 강한 성격에 잘 맞아요.",
                "improve": "조금 더 유연하게 생각하는 연습을 해보면 좋아요."
            },
            {
                "name": "경찰관",
                "desc": "사람들의 안전을 지키는 일을 해요.",
                "prep": "1. 체력 단련을 위해 운동을 꾸준히 해요.\n2. 뉴스나 책을 통해 법과 질서에 대해 배워요.\n3. 학교나 지역의 질서 유지 활동에 참여해보세요.",
                "image": "https://cdn.career.go.kr/images/upload/job/112700.jpg",
                "video": "https://www.career.go.kr/cloud/w/interview/jobView?seq=109034&listT=1",  # 예시: 경찰관 관련 영상
                "link": "https://www.career.go.kr/cloud/w/job/view?seq=359",
                "strength": "정직하고 규칙을 잘 지키는 성격에 잘 맞아요.",
                "improve": "다른 사람의 입장에서 생각하는 연습을 해보세요."
            }
        ]
    },
    "ISFJ": {
        "summary": "친절하고 다른 사람을 돕는 것을 좋아해요.",
        "jobs": [
            {
                "name": "간호사",
                "desc": "환자들을 정성껏 돌보는 일을 해요.",
                "prep": "1. 생물 과학 과목을 재미있게 공부해요.\n2. 친구나 가족을 도와주는 경험을 쌓아보세요.\n3. 응급처치에 대해 간단히 알아보세요.",
                "image": "https://cdn.career.go.kr/images/upload/job/112100.jpg",
                "video": "https://www.career.go.kr/cloud/w/interview/jobView?seq=105861&listT=1",  # 예시: 간호사 관련 영상
                "link": "https://www.career.go.kr/cloud/w/job/view?seq=354",
                "strength": "배려심이 많고 섬세한 성격에 잘 맞아요.",
                "improve": "긴장 상황에서 침착하게 대응하는 연습이 필요해요."
            },
            {
                "name": "초등학교 교사",
                "desc": "어린이들을 가르치고 성장하도록 도와줘요.",
                "prep": "1. 발표와 글쓰기 능력을 키워요.\n2. 어린이와 잘 어울리는 방법을 익혀요.\n3. 책을 읽고 내용을 쉽게 설명하는 연습을 해보세요.",
                "image": "https://cdn.career.go.kr/images/upload/job/132100.jpg",
                "video": "https://www.career.go.kr/cloud/w/interview/jobView?seq=117911&listT=1",  # 예시: 초등학교 교사 관련 영상
                "link": "https://www.career.go.kr/cloud/w/job/view?seq=410",
                "strength": "성실하고 책임감 있는 성격에 잘 맞아요.",
                "improve": "자신의 생각을 명확하게 표현하는 연습이 필요해요."
            }
        ]
    },
    "INFJ": {
        "summary": "조용하지만 마음이 따뜻하고 깊어요.",
        "jobs": [
            {
                "name": "상담전문가",
                "desc": "사람들의 고민을 듣고 도와주는 일을 해요.",
                "prep": "1. 친구 이야기를 잘 들어주는 습관을 가져요.\n2. 감정을 글로 정리해보며 표현해보세요.\n3. 사람의 심리에 대한 책을 읽어보세요.",
                "image": "https://cdn.career.go.kr/images/upload/job/112900.jpg",
                "video": "https://www.career.go.kr/cloud/w/interview/jobView?seq=109027&listT=1",  # 예시: 상담사 관련 영상
                "link": "https://www.career.go.kr/cloud/w/job/view?seq=380",
                "strength": "남을 깊이 이해하려는 마음이 있어서 잘 어울려요.",
                "improve": "처음 보는 사람과도 자연스럽게 대화하는 연습이 필요해요."
            },
            {
                "name": "작가",
                "desc": "이야기나 감정을 글로 표현하는 일을 해요.",
                "prep": "1. 매일 일기를 쓰며 생각을 정리해요.\n2. 다양한 책을 읽고 감상을 적어보세요.\n3. 글쓰기 대회나 블로그에 글을 써보세요.",
                "image": "https://cdn.career.go.kr/images/upload/job/112300.jpg",
                "video": "https://www.career.go.kr/cloud/w/interview/jobView?seq=105721&listT=1",  # 예시: 작가 관련 영상
                "link": "https://www.career.go.kr/cloud/w/job/view?seq=260",
                "strength": "상상력과 공감 능력이 뛰어나서 글을 잘 쓸 수 있어요.",
                "improve": "비판적인 피드백을 잘 받아들이는 연습이 필요해요."
            }
        ]
    },
    "INTJ": {
        "summary": "계획을 세우고 문제를 해결하는 걸 좋아해요.",
        "jobs": [
            {
                "name": "과학자",
                "desc": "새로운 이론을 연구하고 실험을 해요.",
                "prep": "1. 과학 실험 키트를 활용해 관찰을 해보세요.\n2. 탐구 노트를 만들어 궁금한 것을 정리해보세요.\n3. 과학 다큐멘터리나 책을 자주 접해보세요.",
                "image": "https://cdn.career.go.kr/images/upload/job/121300.jpg",
                "video": "https://www.career.go.kr/cloud/w/interview/jobView?seq=117903&listT=1",  # 예시: 과학자 관련 영상
                "link": "https://www.work.go.kr/consltJobCarpa/srch/jobDic/jobDicDtlInfo.do?pageType=keyWord&jobCode=2111&jobSeq=28&txtKeyword=%EC%83%9D%EB%AA%85%EA%B3%B5%ED%95%99%EC%9E%90&txtNumber=&pageIndex=1",
                "strength": "혼자 집중해서 탐구하는 데 강한 성격이에요.",
                "improve": "다른 사람과 아이디어를 나누는 연습이 필요해요."
            },
            {
                "name": "프로그래머",
                "desc": "컴퓨터 프로그램을 만들고 코드를 작성해요.",
                "prep": "1. 엔트리나 스크래치 같은 쉬운 코딩을 시작해보세요.\n2. 퍼즐 게임이나 논리 문제를 자주 풀어보세요.\n3. 간단한 앱이나 게임 만들기를 도전해보세요.",
                "image": "https://cdn.career.go.kr/images/upload/job/133101.jpg",
                "video": "https://www.career.go.kr/cloud/w/interview/jobView?seq=105869&listT=1",  # 예시: 프로그래머 관련 영상
                "link": "https://www.career.go.kr/cloud/w/job/view?seq=834",
                "strength": "논리적이고 분석적인 사고에 강한 성격이에요.",
                "improve": "팀과 함께 일하는 연습을 조금씩 해보세요."
            }
        ]
    },
    "ISTP": {
        "summary": "논리적이고 도구나 기계 다루는 걸 좋아해요.",
        "jobs": [
            {
                "name": "기계 정비사",
                "desc": "자동차나 기계 장비를 수리하고 점검해요.",
                "prep": "1. 자전거나 장난감을 분해하고 조립해보세요.\n2. 공구 사용법을 안전하게 배워보세요.\n3. 기술 관련 영상이나 DIY 키트를 활용해보세요.",
                "image": "https://cdn.career.go.kr/images/upload/job/133204.jpg",
                "video": "https://www.career.go.kr/cloud/w/interview/jobView?seq=105850&listT=1",  # 예시: 기계 정비사 관련 영상
                "link": "https://www.work.go.kr/consltJobCarpa/srch/jobDic/jobDicDtlInfo.do?pageType=jobDicSrchByJobCl&jobCode=7531&jobSeq=6",
                "strength": "실용적이고 조용히 문제를 해결하는 데 능숙해요.",
                "improve": "여럿이 함께 일할 때 의사소통하는 연습이 필요해요."
            },
            {
                "name": "응급 구조사",
                "desc": "위급한 상황에서 사람을 구조하고 도와줘요.",
                "prep": "1. 체력을 키우고 응급처치법을 배워보세요.\n2. 구조 활동에 대한 책이나 사례를 읽어보세요.\n3. 재난안전 캠프나 소방서 체험에 참여해보세요.",
                "image": "https://cdn.career.go.kr/images/upload/job/112500.jpg",
                "video": "https://www.youtube.com/watch?v=6hiLrSJTXEY",  # 예시: 응급 구조사 관련 영상
                "link": "https://www.career.go.kr/cloud/w/job/view?seq=397",
                "strength": "침착하고 순간 판단이 빠른 성격에 잘 맞아요.",
                "improve": "감정을 드러내는 표현을 조금 더 해보는 것도 좋아요."
            }
        ]
    },
    "ISFP": {
        "summary": "감성적이고 예술이나 자연을 좋아해요.",
        "jobs": [
            {
                "name": "플로리스트",
                "desc": "꽃을 이용해 아름다운 장식을 만들어요.",
                "prep": "1. 꽃 이름과 특징을 외워보세요.\n2. 색깔과 모양을 조화롭게 배치해보세요.\n3. 꽃집이나 화훼 농장 체험을 해보세요.",
                "image": "https://cdn.career.go.kr/images/upload/job/132901.jpg",
                "video": "https://www.career.go.kr/cloud/w/interview/jobView?seq=10694&listT=1",  # 예시: 플로리스트 관련 영상
                "link": "https://www.career.go.kr/cloud/w/job/view?seq=316",
                "strength": "아름다움을 느끼고 표현하는 능력이 뛰어나요.",
                "improve": "계획을 세우고 마감에 맞추는 연습이 필요해요."
            },
            {
                "name": "그래픽 디자이너",
                "desc": "그림, 글자, 사진을 조합해 멋진 이미지를 만들어요.",
                "prep": "1. 다양한 디자인을 관찰하고 따라 그려보세요.\n2. 색과 형태에 대한 감각을 키워보세요.\n3. 무료 디자인 프로그램을 활용해 포스터를 만들어보세요.",
                "image": "https://cdn.career.go.kr/images/upload/job/132905.jpg",
                "video": "https://www.career.go.kr/cloud/w/interview/jobView?seq=105728&listT=1",  # 예시: 그래픽 디자이너 관련 영상
                "link": "https://www.career.go.kr/cloud/w/job/view?seq=458",
                "strength": "감성적이고 예술적인 감각이 풍부한 성격이에요.",
                "improve": "자신의 작품을 설명하는 연습이 필요해요."
            }
        ]
    },
    "INFP": {
        "summary": "상상력이 풍부하고 감정을 잘 표현해요.",
        "jobs": [
            {
                "name": "아동 문학 작가",
                "desc": "아이들을 위한 동화나 소설을 써요.",
                "prep": "1. 다양한 동화를 읽고 감상문을 써보세요. \n2. 동화책을 따라 그리거나 줄거리를 새롭게 써보세요.\n3. 상상 속 이야기를 일기장에 적어보세요.",
                "image": "https://cdn.career.go.kr/images/upload/job/112300.jpg",
                "video": "https://www.youtube.com/watch?v=URk4H8MhjyA",  # 예시: 아동 문학 작가 관련 영상
                "link": "https://www.work.go.kr/consltJobCarpa/srch/jobInfoSrch/summaryExmpl.do?jobNm=411102",
                "strength": "따뜻한 감성과 공감 능력이 잘 어울려요.",
                "improve": "글을 끝까지 완성하는 끈기를 기르면 더 좋아요."
            },
            {
                "name": "심리상담사",
                "desc": "사람의 마음을 이해하고 도와주는 일을 해요.",
                "prep": "1. 친구나 가족 이야기를 공감하며 들어보세요.\n2. 감정 표현 연습을 일기로 해보세요.\n3. 사람의 마음에 관한 책을 읽어보세요.",
                "image": "https://cdn.career.go.kr/images/upload/job/112900.jpg",
                "video": "https://www.career.go.kr/cloud/w/interview/jobView?seq=109027&listT=1",  # 예시: 심리상담사 관련 영상
                "link": "https://www.career.go.kr/cloud/w/job/view?seq=380",
                "strength": "다른 사람의 감정을 잘 이해할 수 있어요.",
                "improve": "때로는 논리적으로 상황을 판단하는 연습도 필요해요."
            }
        ]
    },
    "INTP": {
        "summary": "궁금한 게 많고 탐구하는 걸 좋아해요.",
        "jobs": [
            {
                "name": "발명가",
                "desc": "새로운 아이디어로 세상에 없는 물건을 만들어요.",
                "prep": "1. 생활 속 불편한 점을 관찰해보세요.\n2. 직접 만들 수 있는 아이디어를 스케치해보세요.\n3. 창의력 대회나 과학탐구 활동에 참여해보세요.",
                "image": "https://cdn.career.go.kr/images/upload/job/121901.jpg",
                "video": "https://www.youtube.com/watch?v=8c92sGfxs6c",  # 예시: 발명가 관련 영상
                "link": "https://www.career.go.kr/cloud/w/job/view?seq=1433",
                "strength": "새롭고 창의적인 생각을 잘 떠올리는 성격이에요.",
                "improve": "아이디어를 실제로 만들어보는 실천력이 필요해요."
            },
            {
                "name": "빅데이터 분석가",
                "desc": "많은 정보를 모아 분석하고 정리해요.",
                "prep": "1. 차트와 그래프를 읽는 연습을 해보세요.\n2. 간단한 엑셀이나 데이터 정리 활동을 해보세요.\n3. 뉴스에서 통계자료를 관찰해보세요.",
                "image": "https://cdn.career.go.kr/images/upload/job/122400.jpg",
                "video": "https://www.career.go.kr/cloud/w/interview/jobView?seq=116168&listT=1",  # 예시: 빅데이터 분석가 관련 영상
                "link": "https://www.career.go.kr/cloud/w/job/view?seq=10032",
                "strength": "논리적으로 생각하고 문제를 해결하는 데 능해요.",
                "improve": "긴 시간 집중하는 습관을 들이는 것이 중요해요."
            }
        ]
    },
    "ESTP": {
        "summary": "활동적이고 새로운 것을 도전하는 걸 좋아해요.",
        "jobs": [
            {
                "name": "소방관",
                "desc": "화재나 위험한 상황에서 사람들을 구조해요.",
                "prep": "1. 체력을 키우기 위해 매일 운동을 해보세요.\n2. 소방 관련 체험관을 방문해보세요.\n3. 응급처치법과 안전수칙을 배워보세요.",
                "image": "https://cdn.career.go.kr/images/upload/job/112500.jpg",
                "video": "https://www.youtube.com/shorts/vfHievV0_J8",  # 예시: 소방관 관련 영상
                "link": "https://www.career.go.kr/cloud/w/job/view?seq=10032",
                "strength": "위기 상황에 빠르게 대처하고 용감해요.",
                "improve": "계획을 세우고 차분히 실행하는 습관을 들여보세요."
            },
            {
                "name": "운동선수",
                "desc": "운동을 통해 실력을 겨루고 대회에 나가요.",
                "prep": "1. 좋아하는 운동을 정해서 꾸준히 연습해보세요.\n2. 스포츠 경기나 시합을 관찰해보세요.\n3. 팀워크를 기르는 연습도 중요해요.",
                "image": "https://cdn.career.go.kr/images/upload/job/134100.jpg",
                "video": "https://www.youtube.com/shorts/wLSKYm23XAQ",  # 예시: 운동선수 관련 영상
                "link": "https://www.career.go.kr/cloud/w/job/view?seq=336",
                "strength": "에너지가 넘치고 활동적인 성격에 잘 맞아요.",
                "improve": "장기적인 목표를 세우고 인내하는 연습도 필요해요."
            }
        ]
    },
    "ESFP": {
        "summary": "사람들과 어울리기를 좋아하고 밝고 즐거운 성격이에요.",
        "jobs": [
            {
                "name": "연예인 (배우/가수)",
                "desc": "무대에서 노래하거나 연기해요.",
                "prep": "1. 다양한 감정을 표현해보는 연습을 해보세요.\n2. 연극이나 음악회에 자주 참여해보세요.\n3. 발표나 공연을 통해 자신감을 키워보세요.",
                "image": "https://cdn.career.go.kr/images/upload/job/134300.jpg",
                "video": "https://www.youtube.com/watch?v=4LKJzSRRDsU",  # 예시: 연예인 관련 영상
                "link": "https://www.career.go.kr/cloud/w/job/view?seq=280",
                "strength": "사람들과 함께할 때 에너지가 넘쳐요.",
                "improve": "규칙적인 연습과 꾸준함이 필요해요."
            },
            {
                "name": "아나운서",
                "desc": "TV나 라디오에서 뉴스를 전하거나 프로그램을 진행해요.",
                "prep": "1. 또박또박 말하는 연습을 매일 해보세요.\n2. 친구들과 인터뷰 놀이를 해보세요.\n3. 뉴스나 방송을 보며 따라 말해보세요.",
                "image": "https://cdn.career.go.kr/images/upload/job/133401.jpg",
                "video": "https://www.career.go.kr/cloud/w/interview/jobView?seq=109049&listT=2",  # 예시: 아나운서 관련 영상
                "link": "https://www.career.go.kr/cloud/w/job/view?seq=271",
                "strength": "밝은 에너지와 사교성이 뛰어난 성격에 잘 맞아요.",
                "improve": "전문적인 정보를 정확하게 전달하는 훈련이 필요해요."
            }
        ]
    },
    "ENFP": {
        "summary": "창의적이고 열정이 넘치며 사람들과 어울리기를 좋아해요.",
        "jobs": [
            {
                "name": "광고 기획자",
                "desc": "새롭고 기발한 아이디어로 광고를 만드는 일을 해요.",
                "prep": "1. 재미있는 광고를 보고 아이디어를 모아보세요.\n2. 나만의 광고 콘셉트를 만들어보세요.\n3. 친구들과 발표하면서 표현력을 키워보세요.",
                "image": "https://cdn.career.go.kr/images/upload/job/133701.jpg",
                "video": "https://www.youtube.com/watch?v=xFrNHVZWkLM",  # 예시: 광고 기획자 관련 영상
                "link": "https://www.career.go.kr/cloud/w/job/view?seq=283",
                "strength": "아이디어가 풍부하고 사람들을 잘 이끄는 성격에 잘 맞아요.",
                "improve": "한 가지 일에 끝까지 집중하는 연습이 필요해요."
            },
            {
                "name": "사회운동가",
                "desc": "더 나은 세상을 만들기 위해 활동해요.",
                "prep": "1. 사회 문제에 관심을 가져보세요.\n2. 뉴스나 다큐멘터리를 보며 생각을 정리해보세요.\n3. 글이나 발표로 자신의 생각을 표현해보세요.",
                "image": "https://cdn.career.go.kr/images/upload/job/123100.jpg",
                "video": "https://www.career.go.kr/cloud/w/interview/jobView?seq=10687&listT=2",  # 예시: 사회운동가 관련 영상
                "link": "https://www.career.go.kr/cloud/w/job/view?seq=934",
                "strength": "열정과 긍정적인 에너지가 넘치는 성격이에요.",
                "improve": "현실적인 계획을 세우고 꾸준히 실천하는 것이 필요해요."
            }
        ]
    },
    "ENTP": {
        "summary": "재치 있고 새로운 아이디어를 떠올리는 걸 좋아해요.",
        "jobs": [
            {
                "name": "발명가",
                "desc": "새롭고 유용한 발명품을 만들어내요.",
                "prep": "1. 불편한 점을 찾아 해결 방법을 상상해보세요.\n2. 스케치북에 아이디어를 그리고 설명해보세요.\n3. 과학 동아리나 발명대회에 참가해보세요.",
                "image": "https://cdn.career.go.kr/images/upload/job/121901.jpg",
                "video": "https://www.youtube.com/shorts/Pz1kG_0mMDk",  # 예시: 발명가 관련 영상
                "link": "https://www.career.go.kr/cloud/w/job/view?seq=1433",
                "strength": "호기심이 많고 창의력이 뛰어난 성격이에요.",
                "improve": "실행에 옮기기 위해 계획 세우는 연습이 필요해요."
            },
            {
                "name": "벤처 기업가",
                "desc": "새로운 사업 아이디어로 회사를 만들어 운영해요.",
                "prep": "1. 주변의 문제를 해결할 아이디어를 적어보세요.\n2. 친구들과 창업 놀이를 해보세요.\n3. 다양한 직업을 조사해보며 창업 아이템을 떠올려보세요.",
                "image": "https://cdn.career.go.kr/images/upload/job/121400.jpg",
                "video": "https://www.career.go.kr/cloud/w/interview/jobView?seq=109054&listT=2",  # 예시: 벤처 기업가 관련 영상
                "link": "https://www.career.go.kr/cloud/w/job/view?seq=238",
                "strength": "말을 잘하고 도전적인 성격에 잘 맞아요.",
                "improve": "팀원들과 협력하고 꾸준히 실행하는 자세가 필요해요."
            }
        ]
    },
    "ESTJ": {
        "summary": "책임감이 강하고 체계적으로 일하는 걸 좋아해요.",
        "jobs": [
            {
                "name": "군인",
                "desc": "나라를 지키기 위해 훈련하고 작전을 수행해요.",
                "prep": "1. 체력을 기르기 위해 꾸준히 운동해보세요.\n2. 규칙적인 생활 습관을 들여보세요.\n3. 리더십 활동을 통해 팀워크를 배워보세요.",
                "image": "https://cdn.career.go.kr/images/upload/job/111200.jpg",
                "video": "https://www.youtube.com/watch?v=9xHQGd1klsI",  # 예시: 군인 관련 영상
                "link": "https://www.career.go.kr/cloud/w/job/view?seq=407",
                "strength": "책임감 있고 규칙을 잘 지키는 성격이에요.",
                "improve": "가끔은 유연하게 생각하는 연습도 필요해요."
            },
            {
                "name": "공무원",
                "desc": "국가와 사회를 위해 행정 업무를 해요.",
                "prep": "1. 사회나 역사 공부에 흥미를 가져보세요.\n2. 뉴스와 신문을 꾸준히 읽어보세요.\n3. 행정 체험이나 모의 토론 활동에 참여해보세요.",
                "image": "https://cdn.career.go.kr/images/upload/job/111100.jpg",
                "video": "https://www.career.go.kr/cloud/w/interview/jobView?seq=116353&listT=2",  # 예시: 공무원 관련 영상
                "link": "https://www.career.go.kr/cloud/w/job/view?seq=362",
                "strength": "체계적이고 조직적인 성격에 잘 맞아요.",
                "improve": "새로운 변화에 유연하게 대응하는 훈련이 필요해요."
            }
        ]
    },
    "ESFJ": {
        "summary": "친절하고 사람들과 잘 어울려요.",
        "jobs": [
            {
                "name": "초등학교 교사",
                "desc": "어린이들에게 지식과 인성을 가르쳐요.",
                "prep": "1. 책을 많이 읽고 독서록을 써보세요.\n2. 친구를 도와주거나 발표 활동을 해보세요.\n3. 봉사활동을 통해 배려심을 길러보세요.",
                "image": "https://cdn.career.go.kr/images/upload/job/132100.jpg",
                "video": "https://www.youtube.com/shorts/AhzfFKDcabY",  # 예시: 초등학교 교사 관련 영상
                "link": "https://www.career.go.kr/cloud/w/job/view?seq=410",
                "strength": "다른 사람을 잘 도와주고 협력하는 데 능해요.",
                "improve": "자기 주도적으로 문제를 해결하는 연습도 필요해요."
            },
            {
                "name": "간호사",
                "desc": "환자의 건강을 돌보는 일을 해요.",
                "prep": "1. 생물이나 건강 관련 책을 읽어보세요.\n2. 응급처치법을 배워보고 실습해보세요.\n3. 병원 체험 활동에 참여해보세요.",
                "image": "https://cdn.career.go.kr/images/upload/job/112100.jpg",
                "video": "https://www.career.go.kr/cloud/w/interview/jobView?seq=105861&listT=2",  # 예시: 간호사 관련 영상
                "link": "https://www.career.go.kr/cloud/w/job/view?seq=354",
                "strength": "섬세하고 배려심 많은 성격에 잘 맞아요.",
                "improve": "긴급 상황에서 침착하게 대처하는 능력을 길러야 해요."
            }
        ]
    },
    "ENFJ": {
        "summary": "사람을 이끄는 능력이 뛰어나고 따뜻한 리더예요.",
        "jobs": [
            {
                "name": "진로상담사",
                "desc": "학생이나 성인의 진로를 함께 고민하고 조언해줘요.",
                "prep": "1. 다양한 직업을 조사해보고 정리해보세요.\n2. 친구의 고민을 들어주고 조언을 해보세요.\n3. 상담 기술에 대한 책을 읽어보세요.",
                "image": "https://cdn.career.go.kr/images/upload/job/112900.jpg",
                "video": "https://www.youtube.com/shorts/Fwtsixmdb_8",  # 예시: 진로상담사 관련 영상
                "link": "https://www.career.go.kr/cloud/w/interview/jobView?seq=10677&listT=1",
                "strength": "공감능력과 리더십이 조화를 이루는 성격이에요.",
                "improve": "상대방을 경청하는 자세를 유지하려는 연습이 필요해요."
            },
            {
                "name": "교사",
                "desc": "학생을 가르치고 함께 성장하는 직업이에요.",
                "prep": "1. 친구나 동생에게 배운 내용을 설명해보세요.\n2. 글쓰기와 말하기 연습을 꾸준히 해보세요.\n3. 다양한 교육 영상이나 수업 영상을 시청해보세요.",
                "image": "https://cdn.career.go.kr/images/upload/job/132100.jpg",
                "video": "https://www.youtube.com/watch?v=CV7cuH4oMys",  # 예시: 교사 관련 영상
                "link": "https://www.career.go.kr/cloud/w/job/view?seq=1089",
                "strength": "사람을 도와주는 데 보람을 느끼는 성격이에요.",
                "improve": "가끔은 자신의 생각을 솔직하게 표현하는 용기가 필요해요."
            }
        ]
    },
    "ENTJ": {
        "summary": "리더십이 강하고 큰 목표를 향해 나아가는 걸 좋아해요.",
        "jobs": [
            {
                "name": "CEO(대표이사)",
                "desc": "회사를 이끄는 총 책임자로, 계획을 세우고 팀을 운영해요.",
                "prep": "1. 창업 이야기를 담은 책이나 영상을 찾아보세요.\n2. 친구들과 함께 모의 회사 만들기를 해보세요.\n3. 문제 해결 게임이나 전략 보드게임을 해보세요.",
                "image": "https://cdn.career.go.kr/images/upload/job/121400.jpg",
                "video": "https://www.youtube.com/watch?v=D9lRfa46SJk",  # 예시: CEO 관련 영상
                "link": "https://www.career.go.kr/cloud/w/job/view?seq=238",
                "strength": "목표 지향적이고 전략적인 사고에 강해요.",
                "improve": "다른 사람의 의견을 경청하고 조율하는 태도도 중요해요."
            },
            {
                "name": "변호사",
                "desc": "법을 이용해 사람들의 문제를 해결해주는 일을 해요.",
                "prep": "1. 뉴스에서 법 관련 사건을 찾아보고 분석해보세요.\n2. 토론 활동에 참여해 자신의 의견을 표현해보세요.\n3. 논리적인 글쓰기 연습을 해보세요.",
                "image": "https://cdn.career.go.kr/images/upload/job/111300.jpg",
                "video": "https://www.youtube.com/watch?v=YURGaCyw7Jw",  # 예시: 변호사 관련 영상
                "link": "https://www.career.go.kr/cloud/w/job/view?seq=375",
                "strength": "논리적이고 결단력 있는 성격에 딱 맞아요.",
                "improve": "공감 능력을 키우기 위한 노력도 중요해요."
            }
        ]
    }
}

# Streamlit 앱 실행
def main():
    st.set_page_config(page_title="✨ MBTI 진로 추천 ✨", page_icon="🎓")
    st.title("🌟 MBTI로 알아보는 나에게 딱 맞는 직업!")

    name = st.text_input("이름을 입력해 주세요")
    mbti = st.selectbox("자신의 MBTI를 선택해 주세요", list(career_recommendations.keys()))

    if name and mbti:
        st.markdown(f"### 🧑‍🏫 {name}님의 MBTI 성향")
        st.write(career_recommendations[mbti]["summary"])

        st.markdown("### 💡 추천 직업과 준비 방법")
        for job in career_recommendations[mbti]["jobs"]:
            st.markdown(f"#### 🛠️ {job['name']}")
            # st.image(job["image"], caption=f"{job['name']} 예시")
            st.write(f"📌 직업 설명: {job['desc']}")
            st.write(f"✅ 잘 맞는 이유: {job['strength']}")
            st.write(f"🔧 보완하면 좋은 점: {job['improve']}")
            st.markdown(f"🎒 준비 방법:\n{job['prep']}")
            st.markdown(f"▶️ [직업 소개 영상 보기]({job['video']})")
            st.markdown(f"🔗 [자세히 보기]({job['link']})")

if __name__ == "__main__":
    main()
