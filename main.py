
import streamlit as st

# -------------------------------
# 페이지 기본 설정
# -------------------------------
st.set_page_config(
    page_title="MBTI 단짝 포켓몬 찾기",
    page_icon="🌙",
    layout="wide"
)

# -------------------------------
# 전체 디자인 CSS
# -------------------------------
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Gowun+Dodum&display=swap');

html, body, [class*="css"] {
    font-family: 'Gowun Dodum', sans-serif;
}

.stApp {
    background: linear-gradient(135deg, #111827 0%, #201b35 55%, #29213f 100%);
    color: #F5F3FF;
}

.block-container {
    max-width: 1100px;
    padding-top: 2.5rem;
    padding-bottom: 3rem;
}

h1, h2, h3, p, label, span {
    color: #F5F3FF;
}

.main-title {
    text-align: center;
    font-size: 42px;
    font-weight: bold;
    color: #FFE69A;
    margin-bottom: 8px;
}

.subtitle {
    text-align: center;
    font-size: 18px;
    color: #D6D0EA;
    margin-bottom: 28px;
}

.section-title {
    color: #FFE69A;
    font-size: 23px;
    font-weight: bold;
    margin-top: 20px;
    margin-bottom: 12px;
}

.info-card {
    background: rgba(43, 37, 66, 0.92);
    border: 1px solid #55476F;
    border-radius: 18px;
    padding: 20px;
    margin: 10px 0;
    box-shadow: 0 5px 18px rgba(0, 0, 0, 0.18);
}

.pokemon-name {
    color: #FFE69A;
    font-size: 30px;
    font-weight: bold;
    text-align: center;
}

.pokemon-english {
    color: #C7BFE0;
    font-size: 17px;
    text-align: center;
}

.type-badge {
    display: inline-block;
    background: #51436C;
    color: #FFE69A;
    padding: 7px 15px;
    border-radius: 20px;
    margin: 4px;
    font-size: 15px;
}

.small-note {
    color: #BEB6D3;
    font-size: 14px;
    text-align: center;
}

div.stButton > button {
    background: #302743;
    color: #F5F3FF;
    border: 1px solid #6A5887;
    border-radius: 14px;
    min-height: 48px;
    font-size: 17px;
    font-weight: bold;
    transition: 0.2s;
}

div.stButton > button:hover {
    background: #51416D;
    color: #FFE69A;
    border: 1px solid #FFE69A;
    transform: translateY(-2px);
}

div.stButton > button:focus {
    color: #FFE69A;
    border-color: #FFE69A;
}

div[data-testid="stImage"] {
    display: flex;
    justify-content: center;
}

hr {
    border-color: #55476F;
}

[data-testid="stAlert"] {
    background: #302743;
    color: #F5F3FF;
    border-radius: 12px;
}

footer {
    visibility: hidden;
}
</style>
""", unsafe_allow_html=True)

# -------------------------------
# 포켓몬 데이터
# -------------------------------
POKEMON_DATA = {
    "ISTJ": {
        "name": "거북왕", "english": "Blastoise", "id": 9,
        "types": ["물"],
        "traits": "책임감이 강하고 신중하며, 맡은 일을 끝까지 해내는 타입!",
        "reason": "거북왕은 강력한 물대포를 활용하며 안정적으로 싸우는 포켓몬이야. 차분하고 믿음직한 ISTJ처럼 계획적으로 행동하고 자신의 역할을 충실히 해내는 모습이 잘 어울려."
    },
    "ISFJ": {
        "name": "해피너스", "english": "Blissey", "id": 242,
        "types": ["노말"],
        "traits": "다정하고 배려심이 깊으며, 주변 사람을 잘 챙기는 타입!",
        "reason": "해피너스는 다른 포켓몬을 보살피고 도와주는 포켓몬이야. 주변 사람의 마음을 세심하게 살피고 조용히 도움을 주는 ISFJ와 닮았어."
    },
    "INFJ": {
        "name": "루기아", "english": "Lugia", "id": 249,
        "types": ["에스퍼", "비행"],
        "traits": "깊이 생각하고, 조용하지만 자신만의 신념이 뚜렷한 타입!",
        "reason": "루기아는 강력한 힘을 가졌지만 쉽게 그 힘을 드러내지 않는 포켓몬이야. 깊은 생각과 내면의 신념을 중요하게 여기는 INFJ의 분위기와 잘 어울려."
    },
    "INTJ": {
        "name": "디아루가", "english": "Dialga", "id": 483,
        "types": ["강철", "드래곤"],
        "traits": "분석적이고 독립적이며, 목표를 세우고 전략적으로 움직이는 타입!",
        "reason": "시간을 다루는 전설의 포켓몬 디아루가는 압도적인 존재감과 냉철한 분위기를 지니고 있어. 장기적인 계획을 세우고 효율적인 방법을 찾는 INTJ와 잘 어울려."
    },
    "ISTP": {
        "name": "핫삼", "english": "Scizor", "id": 212,
        "types": ["벌레", "강철"],
        "traits": "실용적이고 침착하며, 직접 해보면서 해결책을 찾는 타입!",
        "reason": "핫삼은 강력한 집게와 빠른 움직임을 활용하는 포켓몬이야. 복잡한 설명보다 직접 경험하고 문제를 해결하는 ISTP의 실용적인 모습과 닮았어."
    },
    "ISFP": {
        "name": "마릴", "english": "Marill", "id": 183,
        "types": ["물", "페어리"],
        "traits": "부드럽고 감수성이 풍부하며, 자신만의 취향을 소중히 여기는 타입!",
        "reason": "마릴은 귀엽고 편안한 분위기를 가진 포켓몬이야. 자신의 감정과 취향을 소중히 여기고 자연스러운 방식으로 세상을 즐기는 ISFP와 잘 어울려."
    },
    "INFP": {
        "name": "세레비", "english": "Celebi", "id": 251,
        "types": ["에스퍼", "풀"],
        "traits": "상상력이 풍부하고 따뜻하며, 자신만의 가치관을 중요하게 여기는 타입!",
        "reason": "세레비는 숲과 자연을 지키는 신비로운 포켓몬이야. 따뜻한 마음과 풍부한 상상력으로 자신만의 세계를 만들어 가는 INFP의 모습과 닮았어."
    },
    "INTP": {
        "name": "폴리곤", "english": "Porygon", "id": 137,
        "types": ["노말"],
        "traits": "호기심이 많고 논리적이며, 새로운 원리를 탐구하는 것을 좋아하는 타입!",
        "reason": "폴리곤은 인공적으로 만들어진 독특한 포켓몬이야. 원리와 구조를 분석하고 새로운 아이디어를 탐구하는 INTP의 지적인 호기심과 잘 어울려."
    },
    "ESTP": {
        "name": "갸라도스", "english": "Gyarados", "id": 130,
        "types": ["물", "비행"],
        "traits": "대담하고 행동력이 뛰어나며, 새로운 상황에도 빠르게 적응하는 타입!",
        "reason": "갸라도스는 강력한 힘과 압도적인 존재감을 가진 포켓몬이야. 망설이기보다 직접 행동하고 예상치 못한 상황에서도 과감하게 도전하는 ESTP와 잘 어울려."
    },
    "ESFP": {
        "name": "루차불", "english": "Hawlucha", "id": 701,
        "types": ["격투", "비행"],
        "traits": "활발하고 표현력이 풍부하며, 사람들과 함께 즐기는 것을 좋아하는 타입!",
        "reason": "루차불은 화려한 기술과 자신감 넘치는 모습을 보여 주는 포켓몬이야. 주변 분위기를 밝게 만들고 순간을 즐기는 ESFP의 에너지와 잘 어울려."
    },
    "ENFP": {
        "name": "파치리스", "english": "Pachirisu", "id": 417,
        "types": ["전기"],
        "traits": "밝고 호기심이 많으며, 새로운 가능성을 발견하는 것을 좋아하는 타입!",
        "reason": "파치리스는 작고 귀여우면서도 활발한 에너지를 가진 포켓몬이야. 새로운 경험을 즐기고 주변에 긍정적인 분위기를 전하는 ENFP와 닮았어."
    },
    "ENTP": {
        "name": "조로아크", "english": "Zoroark", "id": 571,
        "types": ["악"],
        "traits": "재치 있고 창의적이며, 색다른 관점으로 문제를 바라보는 타입!",
        "reason": "조로아크는 환상을 이용하는 독특한 능력을 가진 포켓몬이야. 정해진 방식에만 얽매이지 않고 기발한 아이디어로 새로운 해결책을 찾는 ENTP와 잘 어울려."
    },
    "ESTJ": {
        "name": "엠페르트", "english": "Empoleon", "id": 395,
        "types": ["물", "강철"],
        "traits": "체계적이고 결단력이 있으며, 목표를 향해 주도적으로 움직이는 타입!",
        "reason": "엠페르트는 위엄 있는 모습과 강한 리더십이 돋보이는 포켓몬이야. 계획을 세우고 책임 있게 일을 이끌어 가는 ESTJ의 모습과 잘 어울려."
    },
    "ESFJ": {
        "name": "이어롭", "english": "Lopunny", "id": 428,
        "types": ["노말"],
        "traits": "친절하고 사교적이며, 주변 사람들과의 조화를 중요하게 생각하는 타입!",
        "reason": "이어롭은 우아하고 세련된 모습이 특징인 포켓몬이야. 다른 사람과 원만하게 어울리고 주변의 분위기를 살피는 ESFJ의 다정한 모습과 잘 어울려."
    },
    "ENFJ": {
        "name": "메가니움", "english": "Meganium", "id": 154,
        "types": ["풀"],
        "traits": "따뜻하고 공감 능력이 뛰어나며, 다른 사람에게 긍정적인 영향을 주는 타입!",
        "reason": "메가니움은 꽃의 향기로 주변을 편안하게 만드는 포켓몬이야. 다른 사람을 격려하고 함께 성장하도록 돕는 ENFJ의 따뜻한 리더십과 닮았어."
    },
    "ENTJ": {
        "name": "레쿠쟈", "english": "Rayquaza", "id": 384,
        "types": ["드래곤", "비행"],
        "traits": "자신감이 넘치고 목표 지향적이며, 큰 그림을 보며 행동하는 타입!",
        "reason": "레쿠쟈는 하늘을 지키는 강력한 전설의 포켓몬이야. 큰 목표를 향해 과감하게 나아가고 어려운 상황에서도 주도권을 잡는 ENTJ와 잘 어울려."
    }
}

# -------------------------------
# MBTI 궁합 데이터
# -------------------------------
COMPATIBILITY = {
    "ISTJ": ("ESFP", "서로 다른 매력을 통해 새로운 경험과 안정감을 주고받을 수 있어!"),
    "ISFJ": ("ESTP", "한쪽은 세심하게 살피고 다른 한쪽은 과감하게 행동하며 서로를 보완할 수 있어!"),
    "INFJ": ("ENTP", "깊이 있는 생각과 기발한 아이디어가 만나 흥미로운 대화를 나눌 수 있어!"),
    "INTJ": ("ENFP", "계획적인 사고와 자유로운 상상력이 만나 서로의 시야를 넓혀 줄 수 있어!"),
    "ISTP": ("ESFJ", "실용적인 문제 해결과 따뜻한 배려가 만나 서로에게 힘이 되어 줄 수 있어!"),
    "ISFP": ("ENFJ", "감수성과 따뜻한 공감이 만나 편안하게 마음을 나눌 수 있어!"),
    "INFP": ("ENTJ", "풍부한 상상력과 추진력이 만나 서로의 꿈을 실현하는 데 도움을 줄 수 있어!"),
    "INTP": ("ESFJ", "논리적인 생각과 사람을 향한 관심이 만나 서로 다른 강점을 배울 수 있어!"),
    "ESTP": ("ISFJ", "활동적인 에너지와 세심한 배려가 만나 서로의 부족한 부분을 채울 수 있어!"),
    "ESFP": ("ISTJ", "밝은 에너지와 안정적인 계획이 만나 즐거움과 믿음을 함께 얻을 수 있어!"),
    "ENFP": ("INTJ", "자유로운 발상과 체계적인 계획이 만나 새로운 가능성을 만들어 갈 수 있어!"),
    "ENTP": ("INFJ", "창의적인 아이디어와 깊이 있는 통찰력이 만나 의미 있는 대화를 나눌 수 있어!"),
    "ESTJ": ("ISFP", "체계적인 실행력과 유연한 감각이 만나 균형을 이룰 수 있어!"),
    "ESFJ": ("ISTP", "따뜻한 소통과 침착한 문제 해결이 만나 서로를 든든하게 도울 수 있어!"),
    "ENFJ": ("ISFP", "따뜻한 공감과 섬세한 감성이 만나 서로를 이해하고 응원할 수 있어!"),
    "ENTJ": ("INFP", "목표를 향한 추진력과 창의적인 상상력이 만나 서로에게 좋은 자극이 될 수 있어!")
}

# -------------------------------
# 제목
# -------------------------------
st.markdown(
    '<div class="main-title">🌙 MBTI 단짝 포켓몬 찾기 ✨</div>',
    unsafe_allow_html=True
)
st.markdown(
    '<div class="subtitle">나와 닮은 포켓몬을 만나고, 특별한 단짝도 찾아보자!</div>',
    unsafe_allow_html=True
)

# -------------------------------
# MBTI 선택
# -------------------------------
st.markdown(
    '<div class="section-title">💜 1. 나의 MBTI를 선택해 줘!</div>',
    unsafe_allow_html=True
)

mbti_list = [
    "ISTJ", "ISFJ", "INFJ", "INTJ",
    "ISTP", "ISFP", "INFP", "INTP",
    "ESTP", "ESFP", "ENFP", "ENTP",
    "ESTJ", "ESFJ", "ENFJ", "ENTJ"
]

if "selected_mbti" not in st.session_state:
    st.session_state.selected_mbti = None

for row in range(4):
    cols = st.columns(4)
    for col_index in range(4):
        mbti = mbti_list[row * 4 + col_index]
        with cols[col_index]:
            button_label = (
                f"🌟 {mbti} 선택됨"
                if st.session_state.selected_mbti == mbti
                else mbti
            )
            if st.button(button_label, key=f"mbti_{mbti}", use_container_width=True):
                if st.session_state.selected_mbti != mbti:
                    st.session_state.selected_mbti = mbti
                    st.balloons()
                else:
                    st.session_state.selected_mbti = mbti

# -------------------------------
# 선택 결과
# -------------------------------
selected = st.session_state.selected_mbti

if selected:
    pokemon = POKEMON_DATA[selected]
    compatible_mbti, compatible_reason = COMPATIBILITY[selected]

    st.markdown("---")
    st.markdown(
        f'<div class="section-title">✨ 2. {selected}와 닮은 포켓몬</div>',
        unsafe_allow_html=True
    )

    st.markdown('<div class="info-card">', unsafe_allow_html=True)

    image_url = (
        "https://raw.githubusercontent.com/PokeAPI/sprites/master/"
        f"sprites/pokemon/{pokemon['id']}.png"
    )

    left, right = st.columns([1, 2])

    with left:
        st.image(image_url, width=220)

    with right:
        st.markdown(
            f'<div class="pokemon-name">{pokemon["name"]}</div>',
            unsafe_allow_html=True
        )
        st.markdown(
            f'<div class="pokemon-english">{pokemon["english"]}</div>',
            unsafe_allow_html=True
        )

        types_html = "".join(
            f'<span class="type-badge">{t} 타입</span>'
            for t in pokemon["types"]
        )
        st.markdown(
            f'<div style="text-align:center; margin-top:12px;">{types_html}</div>',
            unsafe_allow_html=True
        )

        st.markdown("### 💫 성격 특징")
        st.write(pokemon["traits"])

    st.markdown("### 💌 너와 닮은 이유")
    st.write(pokemon["reason"])

    st.markdown("</div>", unsafe_allow_html=True)

    # -------------------------------
    # 단짝 MBTI
    # -------------------------------
    st.markdown(
        '<div class="section-title">💛 3. 나의 단짝 MBTI</div>',
        unsafe_allow_html=True
    )

    partner = POKEMON_DATA[compatible_mbti]

    st.markdown('<div class="info-card">', unsafe_allow_html=True)

    c1, c2 = st.columns([1, 2])

    with c1:
        partner_image = (
            "https://raw.githubusercontent.com/PokeAPI/sprites/master/"
            f"sprites/pokemon/{partner['id']}.png"
        )
        st.image(partner_image, width=180)

    with c2:
        st.markdown(
            f'<div class="pokemon-name">{compatible_mbti}</div>',
            unsafe_allow_html=True
        )
        st.markdown(
            f'<div class="pokemon-english">{partner["name"]} '
            f'({partner["english"]})</div>',
            unsafe_allow_html=True
        )
        st.write(compatible_reason)

    st.markdown(
        '<p class="small-note">MBTI 궁합은 재미를 위한 참고 정보야. '
        '실제 관계는 서로를 이해하고 존중하는 마음이 더 중요해! 💜</p>',
        unsafe_allow_html=True
    )

    st.markdown("</div>", unsafe_allow_html=True)

    # -------------------------------
    # 다시 선택하기
    # -------------------------------
    if st.button("🔄 다른 MBTI로 다시 찾기", use_container_width=True):
        st.session_state.selected_mbti = None
        st.rerun()

else:
    st.markdown("""
    <div class="info-card" style="text-align:center;">
        <p style="font-size:20px; color:#FFE69A;">
            🌌 아직 MBTI를 선택하지 않았어!
        </p>
        <p style="color:#D6D0EA;">
            위에서 나의 MBTI를 누르면<br>
            나와 닮은 포켓몬과 단짝을 만날 수 있어.
        </p>
    </div>
    """, unsafe_allow_html=True)

# -------------------------------
# 하단 안내
# -------------------------------
st.markdown("---")
st.markdown(
    '<p class="small-note">🌙 MBTI 단짝 포켓몬 찾기 · 재미로 즐기는 성격 테스트 ✨</p>',
    unsafe_allow_html=True
)
