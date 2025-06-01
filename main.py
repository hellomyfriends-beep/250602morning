import streamlit as st
from PIL import Image
import random
import os

# -------------------------------
# 1. MBTI와 밈 이미지 매핑 설정
# -------------------------------
mbti_types = [
    'INTJ', 'INTP', 'ENTJ', 'ENTP',
    'INFJ', 'INFP', 'ENFJ', 'ENFP',
    'ISTJ', 'ISFJ', 'ESTJ', 'ESFJ',
    'ISTP', 'ISFP', 'ESTP', 'ESFP'
]

# 밈 데이터 예시 (이미지 경로와 설명)
meme_data = {
    "INTJ": [("memes/intj_1.jpg", "계획 없는 삶은 INTJ에게 재앙 😅")],
    "ENFP": [("memes/enfp_1.jpg", "또 새로운 프로젝트를 시작해버린 ENFP")],
    "INFP": [("memes/infp_1.jpg", "머릿속은 판타지 소설 중 🧚‍♀️")],
    # 기타 MBTI 유형은 랜덤 디폴트로 처리
}

default_memes = [
    ("memes/default_1.jpg", "오늘도 열심히 살아보자!"),
    ("memes/default_2.jpg", "당신은 특별해요 ✨"),
]

# -------------------------------
# 2. Streamlit 앱 구성
# -------------------------------
st.title("🔮 MBTI로 보는 오늘의 밈")

selected_mbti = st.selectbox("당신의 MBTI 유형을 선택하세요:", mbti_types)

st.markdown("💡 선택한 MBTI에 맞는 밈을 보여드립니다!")

# 해당 MBTI에 맞는 밈 가져오기
if selected_mbti in meme_data:
    meme = random.choice(meme_data[selected_mbti])
else:
    meme = random.choice(default_memes)

image_path, description = meme

# 이미지와 설명 보여주기
st.image(image_path, use_column_width=True)
st.markdown(f"**💬 {description}**")
