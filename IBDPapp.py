import streamlit as st

st.set_page_config(page_title="IBDP Grade Calculator – Mrs Graci", layout="centered")

# ======================
# Definição dos grupos e matérias
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

papers = ["Paper 1", "Paper 2", "Paper 3", "Solution", "Final grade"]

# ======================
# Interface
# ======================
st.markdown("<h1 style='text-align: center; color: #1d427c;'>🎓 IBDP Grade Calculator</h1>", unsafe_allow_html=True)

group = st.selectbox("Choose your IB Group:", list(groups.keys()))
subject = st.selectbox("Choose your Subject:", groups[group])
level = st.selectbox("Choose Level:", ["SL", "HL"])
paper = st.selectbox("Choose what you want to calculate:", papers)

st.write(f"📌 You selected: **{group} → {subject} ({level}) – {paper}**")

# ======================
# Boundaries (somente para Computer Science como exemplo)
# ======================
boundaries_dict = {
    "Computer science": {
        "SL": {
            "Final grade": [
                (0, 13, 1, 30, 49),
                (14, 28, 2, 50, 59),
                (29, 39, 3, 60, 69),
                (40, 49, 4, 70, 79),
                (50, 59, 5, 80, 89),
                (60, 69, 6, 90, 95),
                (70, 100, 7, 96, 100),
            ],
            "Paper 1": [
                (0, 11, 1, 30, 49),
                (12, 23, 2, 50, 59),
                (24, 35, 3, 60, 69),
                (36, 45, 4, 70, 79),
                (46, 54, 5, 80, 89),
                (55, 64, 6, 90, 95),
                (65, 100, 7, 96, 100),
            ],
            "Paper 2": [
                (0, 10, 1, 30, 49),
                (11, 20, 2, 50, 59),
                (21, 24, 3, 60, 69),
                (25, 31, 4, 70, 79),
                (32, 37, 5, 80, 89),
                (38, 44, 6, 90, 95),
                (45, 65, 7, 96, 100),
            ],
            "Paper 3": [
                (0, 5, 1, 30, 49),
                (6, 11, 2, 50, 59),
                (12, 14, 3, 60, 69),
                (15, 17, 4, 70, 79),
                (18, 19, 5, 80, 89),
                (20, 22, 6, 90, 95),
                (23, 30, 7, 96, 100),
            ],
            "Solution": [
                (0, 4, 1, 30, 49),
                (5, 9, 2, 50, 59),
                (10, 14, 3, 60, 69),
                (15, 18, 4, 70, 79),
                (19, 22, 5, 80, 89),
                (23, 26, 6, 90, 95),
                (27, 34, 7, 96, 100),
            ],
        },
        "HL": {
            "Final grade": [
                (0, 14, 1, 30, 49),
                (15, 29, 2, 50, 59),
                (30, 40, 3, 60, 69),
                (41, 51, 4, 70, 79),
                (52, 61, 5, 80, 89),
                (62, 72, 6, 90, 95),
                (73, 100, 7, 96, 100),
            ],
            "Paper 1": [
                (0, 11, 1, 30, 49),
                (12, 23, 2, 50, 59),
                (24, 35, 3, 60, 69),
                (36, 45, 4, 70, 79),
                (46, 54, 5, 80, 89),
                (55, 64, 6, 90, 95),
                (65, 100, 7, 96, 100),
            ],
            "Paper 2": [
                (0, 10, 1, 30, 49),
                (11, 20, 2, 50, 59),
                (21, 24, 3, 60, 69),
                (25, 31, 4, 70, 79),
                (32, 37, 5, 80, 89),
                (38, 44, 6, 90, 95),
                (45, 65, 7, 96, 100),
            ],
            "Paper 3": [
                (0, 5, 1, 30, 49),
                (6, 11, 2, 50, 59),
                (12, 14, 3, 60, 69),
                (15, 17, 4, 70, 79),
                (18, 19, 5, 80, 89),
                (20, 22, 6, 90, 95),
                (23, 30, 7, 96, 100),
            ],
            "Solution": [
                (0, 4, 1, 30, 49),
                (5, 9, 2, 50, 59),
                (10, 14, 3, 60, 69),
                (15, 18, 4, 70, 79),
                (19, 22, 5, 80, 89),
                (23, 26, 6, 90, 95),
                (27, 34, 7, 96, 100),
            ],
        }
    }
}

# ======================
# Input de notas
# ======================
score = st.number_input("Your marks", min_value=0, step=1, format="%d")
total = st.number_input("Total marks possible", min_value=0, step=1, format="%d")

if total > 0:
    if subject.lower() == "computer science":
        percentage = (score / total) * 100
        st.info(f"Your percentage: **{percentage:.2f}%**")

        boundaries = boundaries_dict[level][paper]

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
    else:
        st.error("⚠️ Boundaries not yet defined for this subject.")
else:
    st.info("ℹ️ Please enter your marks and total to calculate results.")
