
import streamlit as st

st.set_page_config(
    page_title="MBTI 단짝 포켓몬 찾기",
    page_icon="⚡",
    layout="centered"
)

POKEMON_DATA = {
    "ISTJ": {
        "ko": "거북왕", "en": "Blastoise", "id": 9,
        "types": "물 (Water)",
        "traits": "침착하고 든든하며, 강력한 물대포로 팀을 지켜 주는 포켓몬이야.",
        "reason": "계획을 세우고 맡은 일을 꾸준히 해내는 ISTJ와 듬직한 거북왕은 잘 어울려.\n차분하게 상황을 살피며 책임감 있게 행동하는 모습이 닮았어.",
        "match": "ESFP",
        "match_reason": "서로 다른 매력으로 일상에 활기를 더하고 새로운 경험을 함께 즐길 수 있어."
    },
    "ISFJ": {
        "ko": "해피너스", "en": "Blissey", "id": 242,
        "types": "노말 (Normal)",
        "traits": "상냥하고 다정하며, 다른 포켓몬을 보살피는 것을 좋아해.",
        "reason": "주변 사람을 세심하게 챙기는 ISFJ는 해피너스의 따뜻한 마음과 닮았어.\n친구가 힘들 때 곁에서 도와주는 든든한 단짝이 될 것 같아.",
        "match": "ESFP",
        "match_reason": "따뜻한 배려와 밝은 에너지가 만나 즐겁고 편안한 관계를 만들 수 있어."
    },
    "INFJ": {
        "ko": "루기아", "en": "Lugia", "id": 249,
        "types": "에스퍼 / 비행 (Psychic / Flying)",
        "traits": "신비로운 분위기를 지녔고, 강력한 힘을 조용히 다루는 전설의 포켓몬이야.",
        "reason": "깊이 생각하고 자신이 소중하게 여기는 가치를 지키는 INFJ와 잘 어울려.\n차분하면서도 다른 존재를 배려하는 이미지가 닮았어.",
        "match": "ENFP",
        "match_reason": "깊은 생각과 새로운 아이디어를 함께 나누며 서로의 시야를 넓힐 수 있어."
    },
    "INTJ": {
        "ko": "디아루가", "en": "Dialga", "id": 483,
        "types": "강철 / 드래곤 (Steel / Dragon)",
        "traits": "시간을 다루는 전설의 포켓몬으로, 강인하고 위엄 있는 모습이 특징이야.",
        "reason": "장기적인 목표를 세우고 전략적으로 생각하는 INTJ와 닮은 점이 있어.\n미래를 내다보며 차근차근 계획하는 이미지가 잘 어울려.",
        "match": "ENTP",
        "match_reason": "서로의 독창적인 생각을 발전시키며 새로운 가능성을 찾을 수 있어."
    },
    "ISTP": {
        "ko": "핫삼", "en": "Scizor", "id": 212,
        "types": "벌레 / 강철 (Bug / Steel)",
        "traits": "빠른 움직임과 단단한 집게를 지녔으며, 민첩하게 대응하는 포켓몬이야.",
        "reason": "직접 살펴보고 실용적인 해결책을 찾는 ISTP와 핫삼은 잘 어울려.\n필요한 순간에 침착하고 정확하게 움직이는 모습이 닮았어.",
        "match": "ESTJ",
        "match_reason": "실전 대처 능력과 체계적인 계획을 서로에게 배울 수 있어."
    },
    "ISFP": {
        "ko": "마릴", "en": "Marill", "id": 183,
        "types": "물 / 페어리 (Water / Fairy)",
        "traits": "동글동글한 외모와 밝은 성격이 매력적인 포켓몬이야.",
        "reason": "자기만의 감성과 자유로운 분위기를 소중히 여기는 ISFP와 잘 어울려.\n마릴처럼 편안하고 다정한 매력으로 친구에게 즐거움을 줄 수 있어.",
        "match": "ENFJ",
        "match_reason": "서로의 감정을 존중하고 잘하는 점을 발견하며 응원해 줄 수 있어."
    },
    "INFP": {
        "ko": "세레비", "en": "Celebi", "id": 251,
        "types": "에스퍼 / 풀 (Psychic / Grass)",
        "traits": "숲과 자연을 상징하며, 시간을 넘어 여행하는 신비로운 포켓몬이야.",
        "reason": "상상력이 풍부하고 자신만의 소중한 가치를 중요하게 생각하는 INFP와 닮았어.\n자연을 아끼고 희망을 전하는 세레비의 이미지가 잘 어울려.",
        "match": "ENFJ",
        "match_reason": "서로의 꿈을 격려하고 마음을 이해하며 함께 성장할 수 있어."
    },
    "INTP": {
        "ko": "폴리곤", "en": "Porygon", "id": 137,
        "types": "노말 (Normal)",
        "traits": "디지털 공간을 위해 만들어진 포켓몬으로, 독특하고 기술적인 특징이 있어.",
        "reason": "새로운 원리와 지식을 탐구하는 INTP의 호기심과 잘 어울려.\n폴리곤처럼 색다른 관점으로 세상을 관찰하는 단짝이 될 것 같아.",
        "match": "ENTJ",
        "match_reason": "분석적인 아이디어를 구체적인 계획으로 발전시키는 데 서로 도움을 줄 수 있어."
    },
    "ESTP": {
        "ko": "갸라도스", "en": "Gyarados", "id": 130,
        "types": "물 / 비행 (Water / Flying)",
        "traits": "강력한 힘과 대담한 모습으로 잘 알려진 포켓몬이야.",
        "reason": "새로운 상황에 빠르게 반응하고 과감하게 도전하는 ESTP와 닮았어.\n갸라도스처럼 에너지가 넘치고 어려운 순간에도 물러서지 않는 이미지야.",
        "match": "ISFJ",
        "match_reason": "서로 다른 장점을 배우며 새로운 상황에도 유연하게 대처할 수 있어."
    },
    "ESFP": {
        "ko": "루차불", "en": "Hawlucha", "id": 701,
        "types": "격투 / 비행 (Fighting / Flying)",
        "traits": "화려한 기술과 개성 있는 모습이 돋보이는 포켓몬이야.",
        "reason": "활기차고 함께하는 순간을 즐기는 ESFP와 루차불은 잘 어울려.\n자신만의 매력을 표현하고 주변 분위기를 신나게 만들어 줄 것 같아.",
        "match": "ISFJ",
        "match_reason": "밝은 에너지와 세심한 배려가 만나 좋은 균형을 이룰 수 있어."
    },
    "ENFP": {
        "ko": "파치리스", "en": "Pachirisu", "id": 417,
        "types": "전기 (Electric)",
        "traits": "작고 재빠르며, 전기를 모으는 활발한 다람쥐 포켓몬이야.",
        "reason": "호기심이 많고 새로운 경험을 즐기는 ENFP와 잘 어울려.\n파치리스처럼 통통 튀는 에너지와 사랑스러운 매력으로 주변을 밝게 해 줘.",
        "match": "INFJ",
        "match_reason": "새로운 아이디어와 깊은 대화를 함께 나누며 서로를 이해할 수 있어."
    },
    "ENTP": {
        "ko": "조로아크", "en": "Zoroark", "id": 571,
        "types": "악 (Dark)",
        "traits": "환영을 만들어 내는 능력과 영리한 모습이 특징이야.",
        "reason": "독창적인 생각과 재치 있는 문제 해결을 즐기는 ENTP와 닮았어.\n조로아크처럼 예상 밖의 아이디어로 새로운 가능성을 찾아낼 것 같아.",
        "match": "INTJ",
        "match_reason": "서로의 전략과 아이디어를 발전시키며 새로운 방법을 발견할 수 있어."
    },
    "ESTJ": {
        "ko": "엠페르트", "en": "Empoleon", "id": 395,
        "types": "물 / 강철 (Water / Steel)",
        "traits": "당당한 모습과 강인한 부리를 지녔으며, 위엄 있는 포켓몬이야.",
        "reason": "목표를 분명히 하고 책임감 있게 일을 이끄는 ESTJ와 잘 어울려.\n엠페르트처럼 원칙을 지키며 맡은 일을 힘차게 해내는 모습이 닮았어.",
        "match": "ISTP",
        "match_reason": "계획을 세우는 능력과 실전 대처 능력이 서로에게 도움이 될 수 있어."
    },
    "ESFJ": {
        "ko": "이어롭", "en": "Lopunny", "id": 428,
        "types": "노말 (Normal)",
        "traits": "우아하고 민첩한 움직임이 특징인 포켓몬이야.",
        "reason": "사람들과 잘 어울리고 주변을 챙기는 ESFJ와 이어롭은 잘 어울려.\n친근한 매력으로 친구들과 조화를 이루는 모습을 떠올릴 수 있어.",
        "match": "ISFP",
        "match_reason": "서로를 배려하고 각자의 취향을 존중하며 편안한 관계를 만들 수 있어."
    },
    "ENFJ": {
        "ko": "메가니움", "en": "Meganium", "id": 154,
        "types": "풀 (Grass)",
        "traits": "꽃의 향기로 주변을 편안하게 해 주는 온화한 포켓몬이야.",
        "reason": "다른 사람을 격려하고 함께 성장하는 데 관심이 많은 ENFJ와 닮았어.\n메가니움처럼 따뜻한 기운으로 친구에게 힘을 줄 수 있어.",
        "match": "INFP",
        "match_reason": "서로의 감정을 존중하고 각자의 꿈을 응원하며 성장할 수 있어."
    },
    "ENTJ": {
        "ko": "레쿠쟈", "en": "Rayquaza", "id": 384,
        "types": "드래곤 / 비행 (Dragon / Flying)",
        "traits": "하늘 높이 살아가는 강력한 전설의 포켓몬이야.",
        "reason": "큰 목표를 세우고 적극적으로 앞으로 나아가는 ENTJ와 잘 어울려.\n레쿠쟈처럼 강한 존재감과 추진력을 지닌 이미지가 닮았어.",
        "match": "INTP",
        "match_reason": "추진력과 창의적인 분석을 결합해 새로운 아이디어를 발전시킬 수 있어."
    }
}

# 따뜻한 크림색과 노란색 디자인
st.markdown("""
<style>
.stApp {
    background: #fff8e8;
    color: #55452e;
}
.block-container {
    max-width: 900px;
    padding-top: 2rem;
    padding-bottom: 3rem;
}
.hero {
    background: linear-gradient(135deg, #fffdf5, #ffedb8);
    border: 2px solid #edcf83;
    border-radius: 28px;
    padding: 28px 20px;
    text-align: center;
    box-shadow: 0 7px 0 #ead8aa;
    margin-bottom: 25px;
}
.hero-label {
    display: inline-block;
    background: #ffe5a0;
    border-radius: 999px;
    padding: 7px 14px;
    font-weight: bold;
}
.hero h1 {
    color: #986419;
    font-size: clamp(2rem, 5vw, 3rem);
    margin: 17px 0 10px;
}
.hero p {
    color: #78684f;
    font-size: 1.08rem;
    line-height: 1.8;
}
div.stButton > button {
    background: #fff0c7;
    color: #67491b;
    border: 1.5px solid #e6c878;
    border-radius: 14px;
    min-height: 3rem;
    font-size: 1.05rem;
    font-weight: 750;
}
div.stButton > button:hover {
    background: #ffe29a;
    border-color: #d7a83e;
    color: #67491b;
}
.result-card {
    background: #fffdf7;
    border: 2px solid #edcf83;
    border-radius: 24px;
    padding: 22px;
    box-shadow: 0 7px 0 #ead8aa;
    margin-top: 22px;
}
.result-title {
    color: #986419;
    font-size: 2rem;
    font-weight: 850;
}
.info-panel {
    background: #fff4d6;
    border-radius: 16px;
    padding: 16px 18px;
    margin: 12px 0;
    border: 1px solid #f0dca7;
}
.info-panel h3 {
    color: #79551d;
    font-size: 1.12rem;
    margin: 0 0 8px;
}
.info-panel p {
    font-size: 1rem;
    line-height: 1.85;
    margin: 0;
    white-space: pre-line;
}
.match-pill {
    display: inline-block;
    background: #ffe3a0;
    color: #765018;
    padding: 8px 14px;
    border-radius: 12px;
    font-weight: 800;
    font-size: 1.1rem;
}
.footer-note {
    text-align: center;
    color: #9a896c;
    font-size: 0.85rem;
    line-height: 1.7;
    margin-top: 25px;
}
</style>
""", unsafe_allow_html=True)

st.markdown("""
<div class="hero">
  <div class="hero-label">✨ MY POKÉMON PARTNER ✨</div>
  <h1>MBTI 단짝 포켓몬 찾기!</h1>
  <p>내 성격과 잘 어울리는 포켓몬은 누구일까?<br>
  MBTI를 고르고 나만의 단짝을 만나 봐!</p>
  <div style="font-size: 2.5rem;">⚡ 🌸 💧 🌿</div>
</div>
""", unsafe_allow_html=True)

st.subheader("🌼 나의 MBTI를 선택해 줘!")
st.caption("아래 16가지 유형 중 하나를 눌러 봐.")

if "selected_mbti" not in st.session_state:
    st.session_state.selected_mbti = None

if "celebrate_next" not in st.session_state:
    st.session_state.celebrate_next = False

mbti_types = [
    "ISTJ", "ISFJ", "INFJ", "INTJ",
    "ISTP", "ISFP", "INFP", "INTP",
    "ESTP", "ESFP", "ENFP", "ENTP",
    "ESTJ", "ESFJ", "ENFJ", "ENTJ"
]

# 4열로 16가지 MBTI 버튼 만들기
for row_start in range(0, 16, 4):
    cols = st.columns(4)
    for col, mbti in zip(cols, mbti_types[row_start:row_start + 4]):
        with col:
            if st.button(mbti, key=f"button_{mbti}",
                         use_container_width=True):
                st.session_state.selected_mbti = mbti
                st.session_state.celebrate_next = True

selected = st.session_state.selected_mbti

if selected:
    data = POKEMON_DATA[selected]

    # 포켓몬을 새로 선택한 순간 축하 효과 실행
    if st.session_state.celebrate_next:
        st.balloons()
        st.toast("단짝 포켓몬을 찾았어!", icon="🎉")
        st.session_state.celebrate_next = False

    st.markdown(f"""
    <div class="result-card">
      <div style="font-weight: bold; color: #79551d;">
        🎉 단짝 포켓몬 발견! · {selected}
      </div>
      <div class="result-title">
        {data['ko']} <span style="font-size: 1.15rem;">({data['en']})</span>
      </div>
    </div>
    """, unsafe_allow_html=True)

    # PokeAPI 공개 스프라이트 이미지
    image_url = (
        "https://raw.githubusercontent.com/PokeAPI/sprites/master/"
        f"sprites/pokemon/{data['id']}.png"
    )

    left, right = st.columns([1, 1.2], gap="large")

    with left:
        st.image(
            image_url,
            caption=f"{data['ko']} ({data['en']})",
            use_container_width=True
        )

    with right:
        st.markdown(f"""
        <div class="info-panel">
          <h3>💧 포켓몬 타입</h3>
          <p>{data['types']}</p>
        </div>
        <div class="info-panel">
          <h3>⭐ 포켓몬 특징</h3>
          <p>{data['traits']}</p>
        </div>
        """, unsafe_allow_html=True)

    st.markdown(f"""
    <div class="info-panel">
      <h3>💛 너와 잘 어울리는 이유</h3>
      <p>{data['reason']}</p>
    </div>
    <div class="info-panel">
      <h3>🤝 잘 맞을 것 같은 MBTI</h3>
      <div class="match-pill">{data['match']}</div>
      <p style="margin-top: 10px;">{data['match_reason']}</p>
    </div>
    """, unsafe_allow_html=True)

    if st.button("↩ 다시 고르기", use_container_width=True):
        st.session_state.selected_mbti = None
        st.session_state.celebrate_next = False
        st.rerun()
else:
    st.info("👆 MBTI 버튼을 누르면 단짝 포켓몬이 나타나!")

st.markdown("""
<div class="footer-note">
  포켓몬 이미지 출처: PokeAPI 공개 스프라이트 저장소<br>
  MBTI와 포켓몬의 조합은 재미를 위한 창작 콘텐츠입니다.
</div>
""", unsafe_allow_html=True)
