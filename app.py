import streamlit as st
from boundaries import boundaries_dict   # importa tudo do boundaries.py

st.set_page_config(page_title="IBDP Grade Calculator – Mrs Graci", layout="centered")

# ======================
# Grupos e matérias (menus)
# ======================
groups = {
    "Group 1: Studies in Language and Literature": [
        "Language A: Literature",
        "Language A: Language and Literature",
        "Language A: Literature and Performance",
    ],
    "Group 4: Sciences": [
        "Computer Science",
        # você pode adicionar outras depois (Biology, Chemistry, etc.)
    ]
}

# labels bonitos ↔ chaves internas
DISPLAY_LABELS = {
    "paper 1": "Paper 1",
    "paper 2": "Paper 2",
    "paper 3": "Paper 3",
    "individual oral": "Individual Oral",
    "hl essay": "HL Essay",
    "written assessment": "Written Assessment",
    "internal assessment": "Internal Assessment",
    "solution": "Solution",
    "ia": "IA",
    "final grade": "Final Grade",
}
REVERSE_LABELS = {v: k for k, v in DISPLAY_LABELS.items()}

COMPONENT_ORDER = [
    "paper 1", "paper 2", "paper 3",
    "written assessment", "internal assessment",
    "individual oral", "hl essay",
    "solution", "ia",
    "final grade",
]

# ======================
# UI
# ======================
st.markdown("<h1 style='text-align: center; color: #1d427c;'>🎓 IBDP Grade Calculator</h1>", unsafe_allow_html=True)

colA, colB = st.columns(2)
with colA:
    group = st.selectbox("Choose your IB Group:", list(groups.keys()))
with colB:
    subject = st.selectbox("Choose your Subject:", groups[group])

level = st.selectbox("Choose Level:", ["SL", "HL"])

# ======================
# Componentes dinâmicos
# ======================
def available_components(subject_name: str, level_name: str):
    s = subject_name.lower()
    if s in boundaries_dict and level_name in boundaries_dict[s]:
        comps = list(boundaries_dict[s][level_name].keys())
        return sorted(comps, key=lambda x: COMPONENT_ORDER.index(x) if x in COMPONENT_ORDER else 999)
    return []

components = available_components(subject, level)

if not components:
    st.warning("⚠️ Boundaries not available for this subject/level yet.")
    st.stop()

display_options = [DISPLAY_LABELS.get(c, c.title()) for c in components]
paper_display = st.selectbox("Choose the component:", display_options)
paper_key = REVERSE_LABELS.get(paper_display, paper_display.lower())

st.write(f"📌 You selected: **{group} → {subject} ({level}) – {paper_display}**")

# ======================
# Inputs
# ======================
score = st.number_input("Your marks", min_value=0, step=1, format="%d")
total = st.number_input("Total marks possible", min_value=0, step=1, format="%d")

# ======================
# Cálculo
# ======================
if total > 0:
    subj_key = subject.lower()

    if subj_key in boundaries_dict and level in boundaries_dict[subj_key] and paper_key in boundaries_dict[subj_key][level]:
        percentage = (score / total) * 100
        st.info(f"Your percentage: **{percentage:.2f}%**")

        boundaries = boundaries_dict[subj_key][level][paper_key]

        ib_grade, gpa_range, gpa_exact = None, None, None
        for low, high, ib, pasb_low, pasb_high in boundaries:
            if low <= percentage <= high:
                ib_grade = ib
                gpa_range = f"{pasb_low}–{pasb_high}"
                gpa_exact = pasb_low + (percentage - low) / (high - low) * (pasb_high - pasb_low) if high > low else float(pasb_low)
                break

        if ib_grade is not None:
            st.divider()
            c1, c2, c3 = st.columns(3)
            with c1:
                st.metric("IB Grade", ib_grade)
            with c2:
                st.metric("PASB GPA Range", gpa_range)
            with c3:
                st.metric("Converted PASB Value", f"{gpa_exact:.2f}")
        else:
            st.warning("⚠️ Percentage is outside the defined boundaries.")
    else:
        st.error("⚠️ Boundaries not defined for this subject/level/component.")
else:
    st.info("ℹ️ Please enter your marks and total to calculate results.")
