import streamlit as st

# MBTI 리스트
mbti_types = [
    'INTJ', 'INTP', 'ENTJ', 'ENTP',
    'INFJ', 'INFP', 'ENFJ', 'ENFP',
    'ISTJ', 'ISFJ', 'ESTJ', 'ESFJ',
    'ISTP', 'ISFP', 'ESTP', 'ESFP'
]

# MBTI별 직업 추천 사전
mbti_jobs = {
    'INTJ': [
        ("데이터 과학자", "논리적이고 전략적인 사고에 강점"),
        ("전략 컨설턴트", "복잡한 문제 해결에 흥미"),
        ("소프트웨어 개발자", "독립적인 분석과 설계 적합")
    ],
    'ENFP': [
        ("마케팅 기획자", "창의력과 대인관계 능력이 뛰어남"),
        ("브랜드 매니저", "트렌드에 민감하고 감성적 소통이 뛰어남"),
        ("교사", "사람들과의 상호작용에서 에너지 얻음")
    ],
    'ISTJ': [
        ("회계사", "정확함과 책임감이 필요한 직업"),
        ("공무원", "체계적이고 안정적인 환경 선호"),
        ("엔지니어", "실용적이고 조직적인 사고")
    ],
    'INFP': [
        ("작가", "감성적이고 자기 표현 욕구가 강함"),
        ("상담사", "다른 사람의 감정을 잘 이해함"),
        ("디자이너", "창의성과 감수성이 풍부함")
    ],
    # 기타 MBTI는 기본 직업 추천
}

default_jobs = [
    ("커뮤니케이션 전문가", "대부분의 MBTI가 적응할 수 있는 유연한 역할"),
    ("프로젝트 매니저", "계획과 협업의 균형이 필요한 직무")
]

# Streamlit 구성
st.set_page_config(page_title="MBTI 직업 추천기", page_icon="💼", layout="centered")
st.title("💼 MBTI 기반 직업 추천기")
st.markdown("당신의 MBTI 유형을 선택하면, 적합한 직업을 추천해드릴게요!")

# MBTI 입력
selected_mbti = st.selectbox("당신의 MBTI는?", mbti_types)

# 직업 추천 출력
st.subheader("🔎 추천 직업 리스트")

if selected_mbti in mbti_jobs:
    for job, desc in mbti_jobs[selected_mbti]:
        st.markdown(f"- **{job}**: {desc}")
else:
    st.markdown("해당 MBTI에 대한 추천이 부족해요. 일반적인 추천을 알려드릴게요!")
    for job, desc in default_jobs:
        st.markdown(f"- **{job}**: {desc}")
