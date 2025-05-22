import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# ✅ Wczytywanie danych
@st.cache_data
def load_data():
    return pd.read_csv("data/rfm.csv")

df = load_data()

# 🧩 Tytuł i opis ogólny
st.title("📊 Segmentacja klientów na podstawie analizy RFM")

st.markdown("""
Projekt analizuje dane klientów platformy e-commerce na podstawie metryk:

- **Recency**: ile dni temu klient ostatnio kupował  
- **Frequency**: jak często kupował  
- **Monetary**: ile wydał łącznie  

Te trzy cechy pozwalają przypisać klientów do segmentów.

ℹ️ **Uwaga:**  
Wartości `Recency = 1` oznaczają, że klient zrobił zakupy **niedawno**.  
Wartości `Recency = 2` wskazują, że klient jest **nieaktywny** i kupował dawno temu.  
Dane zostały wcześniej zaklasyfikowane do przedziałów (np. kwantyle), co ułatwia analizę.
""")

# 📊 Wykres: Recency vs Frequency
st.subheader("📈 Rozkład klientów: Recency vs Frequency")
fig1, ax1 = plt.subplots()
sns.scatterplot(data=df, x="Recency", y="Frequency", ax=ax1)
ax1.set_title("Recency vs Frequency")
st.pyplot(fig1)

# ℹ️ Wyjaśnienie: Recency vs Frequency
with st.expander("ℹ️ Uwaga: Interpretacja wykresu Recency vs Frequency", expanded=False):
    st.markdown("""
    **Recency (Ostatnia aktywność):**
    - `Recency = 1`: klient kupował **niedawno** (aktywny).
    - `Recency = 2`: klient kupował **dawno temu** (nieaktywny).

    **Frequency (Częstotliwość zakupów):**
    - Większa wartość oznacza więcej transakcji.

    **Co pokazuje wykres?**
    - Klienci w lewym górnym rogu (Recency=1, wysoka Frequency) to **lojalni klienci**.
    - Prawy dolny róg (Recency=2, niska Frequency) to klienci zagrożeni odejściem.
    - Wykres pomaga rozpoznać segmenty klientów i ocenić ich wartość.
    """)

# 📊 Wykres: Monetary vs Frequency
st.subheader("📈 Rozkład klientów: Monetary vs Frequency")
fig2, ax2 = plt.subplots()
sns.scatterplot(data=df, x="Monetary", y="Frequency", ax=ax2)
ax2.set_title("Monetary vs Frequency")
st.pyplot(fig2)

# 📋 Tabela danych
st.subheader("📋 Przykładowe dane RFM")
st.dataframe(df.head(10))

# 🧠 Wnioski z analizy
st.markdown("""
---

## 🧠 Wnioski z analizy

- Klienci, którzy ostatnio kupowali (**Recency = 1**) zwykle kupują częściej.
- Klienci z wysokim **Monetary** mają też wyższą aktywność (**Frequency**).
- Dane sugerują istnienie kilku segmentów klientów — warto je dalej analizować.

---

### 📚 Typ analizy

- 🔍 To analiza **uczenia nienadzorowanego** – nie przewidujemy wartości, tylko grupujemy.
- Może być używana w marketingu, lojalności klienta i optymalizacji komunikacji.
""")
