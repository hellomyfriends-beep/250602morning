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
    # 다른 MBTI는 default로 처리
}

# 기본 밈 리스트
default_memes = [
    ("memes/default_1.jpg", "오늘도 열심히 살아보자!"),
    ("memes/default_2.jpg", "당신은 특별해요 ✨"),
]

# -------------------------------
# 2. Streamlit 앱 구성
# -------------------------------
st.set_page_config(page_title="MBTI 밈 추천기", page_icon="🎭", layout="centered")
st.title("🔮 MBTI로 보는 오늘의 밈")
st.markdown("당신의 MBTI 유형을 선택하면, 성격에 맞는 밈을 보여드릴게요!")

# 사용자 MBTI 입력
selected_mbti = st.selectbox("👉 당신의 MBTI 유형은?", mbti_types)

# 밈 선택
if selected_mbti in meme_data:
    meme = random.choice(meme_data[selected_mbti])
else:
    meme = random.choice(default_memes)

image_path, description = meme

# 이미지와 설명 보여주기
if os.path.exists(image_path):
    st.image(image_path, use_container_width=True)
    st.markdown(f"**💬 {description}**")
else:
    st.error("❗ 이미지 파일을 찾을 수 없습니다. memes 폴더를 확인해주세요.")
