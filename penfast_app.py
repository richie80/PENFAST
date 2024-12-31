import streamlit as st

# Titel en introductie
st.title("PEN-FAST Calculator")
st.write("""
De PEN-FAST-regel is een hulpmiddel voor het inschatten van de kans op penicilline-allergie. Vul de vragen in om de score te berekenen.
""")

# Vraag 1: Penicilline-allergie gemeld door patiënt?
pen_allergy = st.checkbox("Penicilline-allergie gemeld door patiënt (PEN)?")

# Als deze vraag met "Ja" wordt beantwoord, toon de overige vragen
if pen_allergy:
    st.markdown("### Vragen")

    # Overige vragen
    five_years_or_less = st.checkbox("Reactie binnen vijf jaar of minder geleden (F)?")
    anaphylaxis = st.checkbox("Anafylaxie of angio-oedeem (A)?")
    severe_cutaneous = st.checkbox("Ernstige cutane reactie (S)?")
    treatment_needed = st.checkbox("Behandeling nodig voor de reactie (T)?")

    # Punten toekennen
    five_years_points = 2 if five_years_or_less else 0
    anaphylaxis_points = 2 if anaphylaxis or severe_cutaneous else 0
    treatment_points = 1 if treatment_needed else 0

    # Totale score berekenen
    total_points = five_years_points + anaphylaxis_points + treatment_points

    # Weergave van score
    st.subheader("Totale Score")
    st.write(f"De totale PEN-FAST-score is: **{total_points}**")

    # Interpretatie
    st.subheader("Interpretatie van de score")
    if total_points == 0:
        st.success("Zeer lage kans op positieve penicillinetest (<1%).")
    elif 1 <= total_points <= 2:
        st.info("Lage kans op positieve penicillinetest (5%).")
    elif total_points == 3:
        st.warning("Matige kans op positieve penicillinetest (20%).")
    else:
        st.error("Hoge kans op positieve penicillinetest (50%).")

    # Extra uitleg
    st.markdown("""
    ### Uitleg van de PEN-FAST-score
    - **0 punten**: Zeer lage kans (<1%) op allergie.
    - **1-2 punten**: Lage kans (5%) op allergie.
    - **3 punten**: Matige kans (20%) op allergie.
    - **4-5 punten**: Hoge kans (50%) op allergie.
    """)
else:
    st.warning("De overige vragen zijn alleen relevant als een penicilline-allergie is gemeld door de patiënt.")
