import streamlit as st

# 페이지 설정
st.set_page_config(
    page_title="✨ MBTI 진로 추천 ✨",
    page_icon="🚀",
    layout="centered",
)

# 커스텀 CSS로 화려하게 꾸미기
st.markdown("""
<style>
body {
    background: linear-gradient(135deg, #f6d365 0%, #fda085 100%);
}
header {
    background-color: rgba(255, 255, 255, 0.5);
    border-radius: 10px;
    padding: 10px;
}
.stButton>button {
    background-color: #ff7f50;
    color: white;
    font-weight: bold;
    border-radius: 20px;
    padding: 8px 24px;
}
</style>
""" , unsafe_allow_html=True)

# 제목과 설명
st.markdown("# 🎉 나의 MBTI로 알아보는 ✨직업 추천✨ 🎉")
st.markdown("---")

# MBTI 선택
mbti_types = [
    "INTJ", "INTP", "ENTJ", "ENTP",
    "INFJ", "INFP", "ENFJ", "ENFP",
    "ISTJ", "ISFJ", "ESTJ", "ESFJ",
    "ISTP", "ISFP", "ESTP", "ESFP"
]
selected = st.selectbox("👉 나의 MBTI를 선택하세요 👈", mbti_types)

# MBTI별 직업 추천 맵
recommendations = {
    "INTJ": ["🔬 연구원", "💻 데이터 사이언티스트", "📊 전략 컨설턴트"],
    "INTP": ["🧠 철학자", "🔧 개발자", "📐 시스템 아키텍트"],
    "ENTJ": ["👔 기업가", "🏦 금융 분석가", "📈 프로젝트 매니저"],
    "ENTP": ["💡 스타트업 창업가", "🎤 마케팅 전략가", "🤖 혁신 연구원"],
    "INFJ": ["🌱 심리 상담가", "✍️ 작가", "🎨 아트 디렉터"],
    "INFP": ["📚 작가", "🎭 배우", "🎵 음악가"],
    "ENFJ": ["🗣️ 교육 코치", "🤝 HR 매니저", "🌟 리더십 컨설턴트"],
    "ENFP": ["🎉 이벤트 플래너", "🎥 크리에이터", "🗺️ 여행 작가"],
    "ISTJ": ["📂 회계사", "🔒 보안 전문가", "🏛️ 공무원"],
    "ISFJ": ["🩺 간호사", "🏥 의료 코디네이터", "📚 사서"],
    "ESTJ": ["🛠️ 운영 관리자", "🏢 컨설턴트", "🚚 물류 관리자"],
    "ESFJ": ["🍎 교사", "🤗 사회 복지사", "👗 패션 컨설턴트"],
    "ISTP": ["🔧 엔지니어", "🚗 정비사", "🎮 게임 개발자"],
    "ISFP": ["🎨 아티스트", "📷 사진작가", "🌿 조경사"],
    "ESTP": ["⚡ 영업 사원", "🏀 스포츠 코치", "🚀 파일럿"],
    "ESFP": ["🎤 가수", "💃 무용가", "🏝️ 여행 가이드"]
}

# 추천 결과 보여주기
if selected:
    st.markdown(f"## 🎯 **{selected}**님을 위한 추천 직업 🎯")
    for job in recommendations.get(selected, []):
        st.markdown(f"- {job}")
    st.balloons()  # 풍선 효과🎈

# 푸터
st.markdown("---")
st.markdown("**✨진로 탐색을 응원합니다!🚀✨**")
