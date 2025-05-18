import streamlit as st

# 페이지 설정
st.set_page_config(page_title="✨MBTI 진로 추천✨", page_icon="🎯", layout="centered")

# 스타일 추가
st.markdown("""
<style>
h1, h2 {
    color: #ff6f61;
    text-align: center;
}
.stButton>button {
    background-color: #f9c74f;
    color: black;
    border-radius: 15px;
    padding: 0.5em 1em;
    font-size: 18px;
}
</style>
""", unsafe_allow_html=True)

# 타이틀
st.title("🎓 MBTI로 알아보는 나의 꿈 ✨")
st.write("중학생 친구들을 위한 맞춤 진로 추천 서비스예요! 💡")
st.write("MBTI를 선택하고 나에게 어울리는 직업을 찾아보세요! 🚀")

# MBTI 목록
mbti_list = ["ISTJ", "ISFJ", "INFJ", "INTJ", "ISTP", "ISFP", "INFP", "INTP",
             "ESTP", "ESFP", "ENFP", "ENTP", "ESTJ", "ESFJ", "ENFJ", "ENTJ"]

mbti = st.selectbox("👉 나의 MBTI를 선택해 주세요!", mbti_list)

# 예시 추천 직업 DB
career_data = {
    "INFP": [
        {
            "name": "✈️ 비행기 조종사",
            "desc": "하늘을 나는 비행기를 조종하며 사람들을 안전하게 목적지까지 데려다 주는 일을 합니다.",
            "prep": "신체검사에 통과할 정도로 건강해야 하므로 운동을 열심히 해야 하고, 수학과 과학 공부가 필요해요. 친구들과 협력하고 의사소통하는 능력도 중요해요!"
        },
        {
            "name": "🎨 일러스트레이터",
            "desc": "책, 광고, 게임 등에 들어가는 그림을 그려요. 상상력이 풍부하고 혼자 작업하는 걸 좋아하는 사람에게 잘 맞아요.",
            "prep": "그림을 많이 그리고, 다양한 스타일을 익히는 연습이 필요해요. 미술 수업이나 디자인 도구 사용도 도움이 돼요!"
        }
    ],
    "ESTJ": [
        {
            "name": "⚖️ 판사",
            "desc": "법정에서 법을 바탕으로 올바른 판단을 내리는 일을 해요. 책임감 있고 공정한 성격
