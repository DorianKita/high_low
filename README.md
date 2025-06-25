# high_low
This is a high and low game with flask.

# 🎮 High-Low Game (Flask)

High-Low Game to prosta gra przeglądarkowa stworzona w Pythonie z wykorzystaniem frameworka Flask. Twoim celem jest odgadnięcie liczby wylosowanej przez serwer — znajduje się ona w zakresie od 1 do 9.

Gra została wzbogacona o zabawne gify, które reagują na Twój wybór:

- 🔼 Jeśli liczba jest za wysoka — zobaczysz gif sugerujący, że przesadziłeś.
- 🔽 Jeśli liczba jest za niska — gif da Ci znać, że jeszcze za mało.
- ✅ Jeśli trafisz — otrzymasz gratulacyjny gif!

## 🧩 Jak działa gra?

1. Uruchom serwer Flask.
2. Przejdź w przeglądarce do `http://localhost:5000/`.
3. Na stronie zobaczysz komunikat: **"Guess a number between 0 and 9"**.
4. W pasku adresu wpisz np. `http://localhost:5000/5`, aby zgadnąć liczbę.
5. Serwer porówna Twój wybór z wylosowaną liczbą i odpowie odpowiednim komunikatem i gifem.

## 🚀 Jak uruchomić projekt lokalnie?

### ✅ Wymagania

- Python 3.7+
- Flask

### 🔧 Instalacja

1. **Sklonuj repozytorium:**
   ```bash
   git clone https://github.com/twoj-uzytkownik/nazwa-repozytorium.git
   cd nazwa-repozytorium
   
2. **Zainstaluj zależności z pliku requirements.txt:**
   pip install -r requirements.txt

3. **Uruchom aplikację**
   python app.py

4. **Uruchom przeglądarkę i przejdź pod**
   http://localhost:5000/


**Za każdym uruchomieniem serwera losowana jest nowa liczba, ale nie zmienia się ona między kolejnymi zgłoszeniami, dopóki serwer działa. Ta wersja gry nie posiada resetowania wyboru. Jest to prosty projekt edukacyjny.**
