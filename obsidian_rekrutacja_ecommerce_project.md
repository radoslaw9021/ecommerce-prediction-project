# 🧠 Rekrutacyjne Q&A – projekt e-commerce

> 📘 Format do nauki w Obsidian + przykłady + szybkie wyjaśnienia

---

## ❓ Co sprawdziłeś w danych na etapie eksploracji?

**✅ Odpowiedź:**  
Sprawdziłem:
- braki (`NaN`) – bo jak klient bez ID, to jak pizza bez sera 🍕  
- statystyki (`describe`) – żeby wiedzieć, co jest „normą” a co szaleństwem,
- kraje (`value_counts`) – skąd klienci kupują (spoiler: głównie UK 🇬🇧),
- błędne lub anulowane faktury (`InvoiceNo.startswith("C")`) – czyli kto się rozmyślił 😅

---

## ❓ Dlaczego stworzyłeś `TotalPrice`?

**✅ Odpowiedź:**  
Bo `Quantity * UnitPrice = $$$`.  
Chciałem wiedzieć, ile każda transakcja warta była w kasie 🛒

📎 Przykład:  
12 kubków po 3 funty = 36 funtów → to już coś!

---

## ❓ Co to jest analiza RFM?

**✅ Odpowiedź:**  
To jak 3 pytania, które każdy marketer powinien zadać klientowi:

- **R** – Jak dawno kupowałeś? (Recency)  
- **F** – Jak często to robisz? (Frequency)  
- **M** – ILE wydajesz? (Monetary)

📎 Przykład z życia:  
Kasia kupiła 3x w tym miesiącu za 500 zł – to raczej VIP niż zagubiony turysta 😄

---

## ❓ Skąd wziąłeś etykietę `Top Spender`?

**✅ Odpowiedź:**  
Podzieliłem klientów na tercyle według ich wydatków i uznałem, że górne 33% to Top Spenders 💸

📎 Metoda:  
`rfm["Monetary"] >= quantile(0.67)` → `1`  
Reszta → `0`

---

## ❓ Dlaczego użyłeś Random Forest?

**✅ Odpowiedź:**  
Bo działa dobrze „od ręki”, nie wymaga dużo strojenia i daje `feature_importance_`.

📎 Przykład:
To jak leśna rada drzew 🏕️ – każde drzewo głosuje, a większość decyduje!

---

## ❓ Jak oceniasz swój model?

**✅ Odpowiedź:**  
Patrzę na:
- `precision` (ile trafień było celnych 🎯),
- `recall` (czy wykryłem większość Top Spenderów),
- `f1` (święty kompromis)

---

## ❓ Co to jest confusion matrix?

**✅ Odpowiedź:**  
Tablica: ile razy trafiłem, ile razy się pomyliłem.
Idealnie – dużo w lewym górnym i prawym dolnym rogu.

---

## ❓ Jak wyglądał test A/B?

**✅ Odpowiedź:**  
Dwie grupy:
- A: klienci bez rabatu
- B: klienci z rabatem 🎁

Zmierzyłem średnią zakupów → zrobiłem test t-Studenta → sprawdziłem `p-value`.

📎 Jeśli `p < 0.05` → kampania działa!

---

## ❓ Jakie założenia ma t-test?

**✅ Odpowiedź:**  
- próbki niezależne (czyli A i B nie to samo),
- dane normalne (lub próbka duża – CLT ratuje),
- wariancje podobne (czyli nikt nie szaleje z ekstremami)

---

## ❓ Co byś zrobił lepiej?

**✅ Odpowiedź:**  
- Spróbowałbym modelu XGBoost 💥  
- Poszukałbym lepszych cech (np. trend, sezonowość)  
- Może oversampling jak `SMOTE`, jeśli klasy niezbalansowane

---

🎯 **Notatka do siebie:**  
Wszystko to umiesz powiedzieć własnymi słowami → to najważniejsze na rozmowie!
