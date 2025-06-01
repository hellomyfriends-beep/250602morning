import streamlit as st
import random

# MBTI 리스트
mbti_types = [
    'INTJ', 'INTP', 'ENTJ', 'ENTP',
    'INFJ', 'INFP', 'ENFJ', 'ENFP',
    'ISTJ', 'ISFJ', 'ESTJ', 'ESFJ',
    'ISTP', 'ISFP', 'ESTP', 'ESFP'
]

# 궁합 점수 예시 (간단한 버전)
def calculate_compatibility(mbti1, mbti2):
    if mbti1 == mbti2:
        return 95, "같은 유형! 이해도 최고 👍"
    elif mbti1[0] == mbti2[0] and mbti1[1:] != mbti2[1:]:
        return 80, "유사한 성향, 대화 잘 통해요 😊"
    elif mbti1[0] != mbti2[0] and mbti1[1:] == mbti2[1:]:
        return 70, "반대 매력! 서로 배울 점이 많아요 🔄"
    else:
        return random.randint(50, 70), "차이가 있지만 좋은 친구가 될 수 있어요 🌱"

# 추천 활동
def recommend_activity(score):
    if score >= 90:
        return "🎮 같이 게임하거나 여행을 계획해보세요!"
    elif score >= 75:
        return "🍕 맛집 탐방이나 영화 관람 추천!"
    else:
        return "🧩 서로의 취향을 존중하며 새로운 취미를 찾아보세요."

# Streamlit 앱 구성
st.set_page_config(page_title="MBTI 친구 궁합", page_icon="🤝", layout="centered")
st.title("🤝 MBTI 친구 궁합 테스트")
st.markdown("두 사람의 MBTI를 선택하면, 친구로서의 궁합을 알려드릴게요!")

# 사용자 입력
user_mbti = st.selectbox("당신의 MBTI", mbti_types)
friend_mbti = st.selectbox("친구의 MBTI", mbti_types)

# 궁합 계산
if st.button("궁합 확인하기"):
    score, comment = calculate_compatibility(user_mbti, friend_mbti)
    st.subheader(f"💯 궁합 점수: {score}점")
    st.markdown(f"🗣️ {comment}")
    st.markdown(f"✅ 추천 활동: {recommend_activity(score)}")
