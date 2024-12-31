import streamlit as st

# Titel en introductie
st.title("PEN-FAST Calculator")
st.write("""
Een hulpmiddel om de kans op penicilline-allergie te berekenen op basis van de PEN-FAST-regel.
Vul de vragen in en krijg direct een score en interpretatie.
""")

# Inputvragen
st.subheader("Vragen")
severe_symptoms = st.selectbox(
    "Heeft de patiënt ernstige symptomen gehad (zoals anafylaxie)?",
    ["Ja", "Nee"]
)
time_since_reaction = st.selectbox(
    "Hoeveel jaar geleden was de reactie?",
    ["<1 jaar", "1-5 jaar", ">5 jaar"]
)
immediate_reaction = st.selectbox(
    "Trad de reactie op binnen 1 uur na inname van penicilline?",
    ["Ja", "Nee"]
)

# Scoreberekening
score = 0
if severe_symptoms == "Ja":
    score += 2
if time_since_reaction == "<1 jaar":
    score += 2
elif time_since_reaction == "1-5 jaar":
    score += 1
if immediate_reaction == "Ja":
    score += 1

# Resultaat
st.subheader("Resultaat")
st.write(f"Je PEN-FAST-score is: **{score}**")

# Interpretatie van de score
if score >= 3:
    st.warning("Hoge kans op penicilline-allergie. Overweeg verder onderzoek.")
elif score == 2:
    st.info("Matige kans op penicilline-allergie. Overleg met een arts.")
else:
    st.success("Lage kans op penicilline-allergie.")

# Educatie
st.subheader("Wat betekent de score?")
st.write("""
- **0-1**: Lage kans op allergie. Het is waarschijnlijk veilig om penicilline te gebruiken.
- **2**: Matige kans. Overleg met een arts of allergoloog.
- **≥3**: Hoge kans. Overweeg allergietesten en verdere evaluatie.
""")
