# 🧠 Pytania i odpowiedzi rekrutacyjne – projekt e-commerce

---

### ❓ Co sprawdziłeś w danych na etapie eksploracji?

**✅ Odpowiedź:**  
Sprawdziłem obecność braków danych (`isnull().sum()`), statystyki opisowe (`describe()`), rozkład krajów (`value_counts()`), oraz wykryłem zwroty (`Quantity < 0`) i anulowane transakcje (`InvoiceNo` zaczynające się od 'C'). Usunąłem też transakcje bez `CustomerID`.

---

### ❓ Dlaczego stworzyłeś kolumnę `TotalPrice`?

**✅ Odpowiedź:**  
By oszacować wartość każdej transakcji (ilość * cena jednostkowa). Jest to kluczowa zmienna do segmentacji klientów i wyliczenia metryki `Monetary` w analizie RFM.

---

### ❓ Co to jest analiza RFM i dlaczego jej użyłeś?

**✅ Odpowiedź:**  
RFM to metoda segmentacji klientów na podstawie:
- Recency – ile dni od ostatniego zakupu,
- Frequency – ile razy klient kupował,
- Monetary – ile wydał.

Użyłem jej, by zbudować profile klientów oraz wykorzystać je jako cechy wejściowe do modelu predykcyjnego.

---

### ❓ Na czym polegała Twoja etykieta `Top Spender`?

**✅ Odpowiedź:**  
Zbudowałem ją na podstawie wartości `Monetary`. Klienci z górnego 33% pod względem wydatków zostali zakwalifikowani jako `Top Spender` (`IsTopSpender = 1`), reszta jako 0.

---

### ❓ Dlaczego wybrałeś Random Forest jako model?

**✅ Odpowiedź:**  
To solidny, łatwy do interpretacji model. Dobrze radzi sobie z nieliniowościami i nie wymaga standaryzacji danych. Dodatkowo umożliwia analizę ważności cech (`feature_importance_`).

---

### ❓ Jak interpretujesz wynik `classification_report`?

**✅ Odpowiedź:**  
Zwracam uwagę na precision (jakość predykcji pozytywnej klasy), recall (ile trafnych przypadków wykryto) oraz F1-score (średnia harmoniczna precision i recall). W zależności od zastosowania – np. kampanii marketingowej – mogę preferować recall lub precision.

---

### ❓ Co pokazuje confusion matrix?

**✅ Odpowiedź:**  
Ile obserwacji zostało poprawnie i błędnie zaklasyfikowanych jako Top lub nie-Top Spender. Pomaga zrozumieć, gdzie model się myli.

---

### ❓ Co to jest test A/B i jak go przeprowadziłeś?

**✅ Odpowiedź:**  
Podzieliłem dane na dwie grupy: A (kontrolna) i B (np. z rabatem). Porównałem rozkłady wartości zakupów i użyłem testu t-Studenta (`ttest_ind`), by sprawdzić, czy różnica średnich jest istotna statystycznie (p < 0.05).

---

### ❓ Jakie założenia musi spełniać t-test?

**✅ Odpowiedź:**  
Niezależność prób, rozkład normalny (lub duża próba dzięki CLT), zbliżona wariancja (homoskedastyczność). Przy dużych próbkach i symulacjach, wpływ odchyleń od tych założeń jest często minimalny.

---

### ❓ Co byś zrobił, gdyby model miał słabe wyniki?

**✅ Odpowiedź:**  
Sprawdziłbym jakość cech (feature engineering), zbalansowanie klas, spróbował innych modeli (np. XGBoost), oraz dobrał hiperparametry (`GridSearchCV`). Można też zwiększyć dane uczące lub lepiej oczyścić dane wejściowe.
