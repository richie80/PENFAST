Hier is een voorstel voor een **README**-tekst die je kunt gebruiken op GitHub voor de bovenstaande applicatie:

---

# PEN-FAST Calculator

Deze repository bevat de code voor een interactieve **PEN-FAST Calculator**, een hulpmiddel om de kans op penicilline-allergie in te schatten. De tool implementeert de officiële PEN-FAST-regel, zoals beschreven in het artikel van Trubiano et al. in *JAMA Internal Medicine* (2020). 

De PEN-FAST-regel biedt een snelle en eenvoudige manier om patiënten met een gemelde penicilline-allergie te screenen op basis van klinische criteria. Deze applicatie maakt gebruik van **Streamlit** voor een gebruiksvriendelijke webinterface.

---

## Functionaliteiten
- **Interactieve vragen**: Gebruikers kunnen antwoorden invoeren op basis van de PEN-FAST-regel.
- **Automatische scoreberekening**: De calculator berekent de totale PEN-FAST-score en geeft een interpretatie van het resultaat.
- **Extra informatie**: Uitgebreide toelichting over de criteria en uitsluitingen, inclusief een sectie over ernstige cutane reacties.
- **Referentie naar de bron**: De originele publicatie van de PEN-FAST-regel is opgenomen als referentie.

---

## Belangrijke Opmerking
Deze tool is ontwikkeld als hulpmiddel en is bedoeld voor gebruik door zorgprofessionals en geïnformeerde gebruikers. Hoewel een allergoloog naar de inhoud heeft gekeken, is dit hulpmiddel niet bedoeld als vervanging voor medisch advies of klinische beoordeling. **Bij twijfel of onzekerheid wordt nadrukkelijk geadviseerd om een allergoloog te raadplegen.**

De ontwikkelaars en bijdragers aan deze applicatie zijn niet verantwoordelijk voor klinische beslissingen of uitkomsten die voortvloeien uit het gebruik van deze tool.

---

## Hoe te gebruiken
1. Clone de repository:
   ```bash
   git clone https://github.com/jouwgebruikersnaam/pen-fast-calculator.git
   ```
2. Installeer de benodigde Python-pakketten:
   ```bash
   pip install -r requirements.txt
   ```
3. Start de applicatie:
   ```bash
   streamlit run pen_fast_app.py
   ```
4. Open de applicatie in je browser op `http://localhost:8501`.

---

## Referentie
Trubiano JA, Vogrin S, Chua KYL, et al.  
Development and Validation of a Penicillin Allergy Clinical Decision Rule.  
*JAMA Intern Med.* 2020;180(5):1–9.  
[DOI: 10.1001/jamainternmed.2020.0403](https://doi.org/10.1001/jamainternmed.2020.0403)

---

## Licentie
Deze applicatie wordt verstrekt onder de MIT-licentie. Zie het bestand `LICENSE` voor meer informatie.

---

Laat weten als je aanvullingen of wijzigingen wilt! 😊
