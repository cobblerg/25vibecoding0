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
st.markdown("중학생 친구들을 위한 맞춤 진로 추천 서비스예요! 💡<br>MBTI를 선택하고 나에게 어울리는 직업을 찾아보세요! 🚀", unsafe_allow_html=True)

# MBTI 목록
mbti_list = ["ISTJ", "ISFJ", "INFJ", "INTJ", "ISTP", "ISFP", "INFP", "INTP",
             "ESTP", "ESFP", "ENFP", "ENTP", "ESTJ", "ESFJ", "ENFJ", "ENTJ"]

mbti = st.selectbox("👉 나의 MBTI

