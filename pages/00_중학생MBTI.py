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

# 이름 입력
name = st.text_input("😀 이름을 입력해 주세요")

# MBTI 설명 및 선택
st.markdown("MBTI는 사람들이 세상을 바라보고, 결정하는 방식의 성격 유형이에요. 아래에서 나에게 가장 잘 맞는 것을 골라보세요!")
mbti_types = [
    "INTJ", "INTP", "ENTJ", "ENTP",
    "INFJ", "INFP", "ENFJ", "ENFP",
    "ISTJ", "ISFJ", "ESTJ", "ESFJ",
    "ISTP", "ISFP", "ESTP", "ESFP"
]
selected = st.selectbox("👉 나의 MBTI를 선택하세요 👈", mbti_types)

# 중학생 눈높이에 맞춘 직업 추천 (간단한 설명 포함)
recommendations = {
    "INTJ": ["🔬 과학자", "💻 컴퓨터 전문가"],
    "INFP": ["📚 동화 작가", "🎵 음악 선생님"],
    "ESFP": ["🎤 가수", "🏝️ 여행 안내자"],
    # 나머지 유형들도 같은 방식으로 간단한 직업 2개씩만 넣음
}

job_descriptions = {
    "🔬 과학자": "실험하고 연구해서 세상의 비밀을 밝혀내는 사람이에요. 과학, 수학을 열심히 공부하면 좋아요.",
    "💻 컴퓨터 전문가": "컴퓨터로 프로그램을 만들거나 문제를 해결해요. 컴퓨터 과목과 논리력을 키우면 좋아요.",
    "📚 동화 작가": "어린이들이 좋아할 만한 재미있는 이야기를 쓰는 사람이에요. 국어 공부를 열심히 해보세요.",
    "🎵 음악 선생님": "아이들에게 노래와 악기를 가르쳐주는 사람이에요. 음악을 좋아하고 연습도 많이 해야 해요.",
    "🎤 가수": "노래로 사람들에게 기쁨을 주는 사람이에요. 음악과 자신감을 키워보세요.",
    "🏝️ 여행 안내자": "사람들에게 멋진 여행지를 소개해주는 사람이에요. 지리와 외국어를 공부하면 도움이 돼요."
}

if name and selected:
    st.markdown(f"## 🌟 {name} 학생의 MBTI는 **{selected}**! 🌟")
    st.markdown("### 어울리는 직업을 소개할게요!")

    for job in recommendations.get(selected, []):
        if st.button(job, key=job):
            desc = job_descriptions.get(job, "자세한 설명은 준비 중이에요.")
            st.markdown(f"**{job}**\n\n{desc}")

# 푸터
st.markdown("---")
st.markdown("**✨진로 탐색을 응원합니다! 중학생 여러분, 파이팅!💪✨**")

