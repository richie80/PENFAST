import streamlit as st

# Titel en introductie
st.title("PEN-FAST Calculator")
st.write("""
De PEN-FAST-regel is een hulpmiddel voor het inschatten van de kans op penicilline-allergie. Vul de vragen in om de score te berekenen.
""")

# Vraag 1: Penicilline-allergie gemeld door patiënt?
pen_allergy = st.checkbox("Penicilline-allergie gemeld door patiënt (PEN)?")

if pen_allergy:
    st.markdown("### Vragen")

    # Vraag: Hoeveel jaar geleden (inclusief onbekend)?
    time_options = ["<1 jaar", "1-5 jaar", ">5 jaar", "Onbekend"]
    time_since_reaction = st.selectbox(
        "Hoe lang geleden vond de reactie plaats? (Inclusief onbekend)",
        time_options
    )

    # Overige vragen
    anaphylaxis = st.checkbox("Anafylaxie of angio-oedeem (A)?")
    severe_cutaneous = st.checkbox("Ernstige cutane reactie (S)?")
    with st.expander("Meer informatie over ernstige cutane reacties (klik hier)"):
        st.markdown("""
        ### Wat valt onder ernstige cutane reacties?
        Ernstige of uitgestelde reacties omvatten:
        - **Stevens-Johnson-syndroom**
        - **Toxische epidermale necrolyse**
        - **Drug reaction with eosinophilia and systemic symptoms (DRESS)**
        - **Acute gegeneraliseerde pustuleuze exantheem (AGEP)**

        **Belangrijk:** Patiënten met een ernstige vertraagde uitslag met slijmvliesbetrokkenheid moeten worden beschouwd als gevallen van ernstige cutane reacties.

        ### Uitsluitingen
        De volgende fenotypes zijn uitgesloten van de derivatie- en validatiecohorten:
        - **Acute interstitiële nefritis**
        - **Geneesmiddelgeïnduceerde leverbeschadiging**
        - **Serumziekte**
        - **Isolated drug fever**

        Deze fenotypes zijn uitgesloten van de derivatie- en validatiecohorten om de nauwkeurigheid van de regel te waarborgen.
        """)

    treatment_needed = st.checkbox("Behandeling nodig voor de reactie (T)?")

    # Punten toekennen
    five_years_points = 2 if time_since_reaction in ["<1 jaar", "1-5 jaar", "Onbekend"] else 0
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
    - **3 punten**: Matige kans (20%).
    - **4-5 punten**: Hoge kans (50%).
    """)

    # Referentie
    st.markdown("""
    ---
    **Referentie:**
    Trubiano JA, Vogrin S, Chua KYL, et al.  
    Development and Validation of a Penicillin Allergy Clinical Decision Rule.  
    *JAMA Intern Med.* 2020;180(5):1–9.  
    [DOI: 10.1001/jamainternmed.2020.0403](https://doi.org/10.1001/jamainternmed.2020.0403)
    """)
else:
    st.warning("De overige vragen zijn alleen relevant als een penicilline-allergie is gemeld door de patiënt.")

# Voeg een GitHub-logo met link toe onderaan de pagina
st.markdown(
    """
    ---
    <div style="text-align: center;">
        <a href="https://github.com/richie80/PENFAST" target="_blank">
            <img src="https://github.githubassets.com/images/modules/logos_page/GitHub-Mark.png" alt="GitHub" width="50">
        </a>
        <p>Bekijk de broncode op GitHub</p>
    </div>
    """,
    unsafe_allow_html=True,
)
