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
    margin: 5px 0;
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
    ...
    "ESFP": ["🎤 가수", "💃 무용가", "🏝️ 여행 가이드"]
}

# (추가) 직업별 상세 설명 딕셔너리
job_descriptions = {
    "🔬 연구원": "과학 연구를 통해 새로운 발견을 추구하는 직업입니다.",
    "💻 데이터 사이언티스트": "데이터 분석과 모델링을 통해 인사이트를 도출합니다.",
    "📊 전략 컨설턴트": "기업의 전략 수립과 문제 해결을 지원합니다.",
    # ... 나머지 직업에 대해서도 설명을 추가해주세요
}

# 추천 결과와 클릭 이벤트 처리
if selected:
    st.markdown(f"## 🎯 **{selected}**님을 위한 추천 직업 🎯")

    # 여기에 클릭 가능한 버튼을 생성하고
    for job in recommendations.get(selected, []):
        if st.button(job, key=job):  # 클릭 시
            # 여기에 클릭했을 때 설명을 보여주는 코드를 추가
            description = job_descriptions.get(job, "상세 설명이 준비 중입니다.")
            st.markdown(f"**{job}**: {description}")
    st.balloons()  # 풍선 효과🎈

# 푸터
st.markdown("---")
st.markdown("**✨진로 탐색을 응원합니다!🚀✨**")
