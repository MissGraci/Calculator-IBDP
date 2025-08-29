import streamlit as st

st.set_page_config(page_title="IBDP Grade Calculator – Mrs Graci", layout="centered")

# ======================
# Escolha de Grupo e Matéria
# ======================
groups = {
    "Group 1: Studies in Language and Literature": [
        "Language A: Literature",
        "Language A: Language and Literature",
        "Language A: Literature and Performance",
    ],
    "Group 2: Language Acquisition": [
        "Classical languages",
        "Language ab initio",
        "Language B",
    ],
    "Group 3: Individuals and Societies": [
        "Business management",
        "Economics",
        "History",
        "Psychology",
        "Geography",
        "Digital society",
        "Global politics",
        "Philosophy",
        "Social and cultural anthropology",
        "World religions",
    ],
    "Group 4: Sciences": [
        "Biology",
        "Chemistry",
        "Physics",
        "Computer science",
        "Design technology",
        "ESS",
        "Sports, exercise and health science",
    ],
    "Group 5: Mathematics": [
        "Analysis and approaches (AA)",
        "Applications and interpretation (AI)",
    ],
    "Group 6: The Arts": [
        "Music",
        "Visual Arts",
        "Dance",
        "Film",
        "Theatre",
    ]
}

st.markdown(
    "<h1 style='text-align: center; color: #1d427c;'>🎓 IBDP Grade Calculator</h1>",
    unsafe_allow_html=True
)

# Selectors
group = st.selectbox("Choose your IB Group:", list(groups.keys()))
subject = st.selectbox("Choose your Subject:", groups[group])
level = st.selectbox("Choose Level:", ["SL", "HL"])

st.write(f"📌 You selected: **{group} → {subject} ({level})**")

# ======================
# Definição dos Boundaries
# ======================
boundaries_dict = {
    "Computer science": {
        "SL": [
            (0, 14, 1, 30, 49),
            (15, 29, 2, 50, 59),
            (30, 43, 3, 60, 69),
            (44, 53, 4, 70, 79),
            (54, 63, 5, 80, 89),
            (64, 73, 6, 90, 95),
            (74, 100, 7, 96, 100),
        ],
        "HL": [
            (0, 14, 1, 30, 49),
            (15, 29, 2, 50, 59),
            (30, 40, 3, 60, 69),
            (41, 51, 4, 70, 79),
            (52, 61, 5, 80, 89),
            (62, 72, 6, 90, 95),
            (73, 100, 7, 96, 100),
        ],
    },
    # TODO: adicionar Biology, Chemistry, Math, etc.
}

# ======================
# Input de notas
# ======================
score = st.number_input("Your marks", min_value=0, step=1, format="%d")
total = st.number_input("Total marks possible", min_value=0, step=1, format="%d")

if total > 0 and subject.lower() in boundaries_dict:
    percentage = (score / total) * 100
    st.info(f"Your percentage: **{percentage:.2f}%**")

    boundaries = boundaries_dict[subject.lower()][level]

    ib_grade, gpa_range, gpa_exact = None, None, None

    for low, high, ib, pasb_low, pasb_high in boundaries:
        if low <= percentage <= high:
            ib_grade = ib
            gpa_range = f"{pasb_low}–{pasb_high}"
            gpa_exact = pasb_low + (percentage - low) / (high - low) * (pasb_high - pasb_low)
            break

    if ib_grade is not None:
        st.divider()
        col1, col2, col3 = st.columns(3)

        with col1:
            st.metric("IB Grade", ib_grade)
        with col2:
            st.metric("PASB GPA Range", gpa_range)
        with col3:
            st.metric("Converted PASB Value", f"{gpa_exact:.2f}")
    else:
        st.warning("⚠️ Percentage is outside the defined boundaries.")
elif total > 0:
    st.error("⚠️ Boundaries not yet defined for this subject.")
