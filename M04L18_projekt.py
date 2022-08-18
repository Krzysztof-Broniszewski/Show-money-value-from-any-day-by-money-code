# Pomóż szwajcarskiemu bankowi HSBC tworząc aplikację, która odczytuje i analizuje dane z Narodowego Banku Polskiego (NBP) udostępnione przez API i podaje ile była warta wskazana waluta we wskazanym dniu.

# Dzięki Tobie HSBC będzie mógł poprawnie wystawiać w Polsce faktury w walucie obcej - przepisy wymagają, aby kwoty na takich fakturach przeliczać na złotówki wg kursów NBP z określonych dni.

# 1. Zapoznaj się z opisem API: http://api.nbp.pl.
#    1. Ustal jak wygląda URL, pod którym znajdziesz kurs danej waluty z danego dnia?
#    2. W jakim formacie musi być data?
#    3. Co trzeba zmienić w URLu, aby otrzymać odpowiedź w JSONie zamiast XMLu?
# 2. Tabele kursów są publikowane tylko w dni robocze. Przeczytaj w dokumentacji co się stanie, gdy zapytasz o kurs z weekendu lub innego dnia wolnego od pracy?
# 3. Twój program przyjmuje walutę oraz datę jako dwa argumenty wiersza poleceń. Jeśli jednak nie zostaną podane, wówczas poproś użytkownika o podanie tych dwóch informacji przy pomocy funkcji input.

import requests
import sys
from datetime import datetime
from dateutil import parser

parameters = sys.argv[1:]

TABLE = "a"
    
if len(parameters) > 2:
    to_much = sys.argv[3:]
    print(f"Podano zbyt wiele parametrów, pozostałe argumenty {to_much} zostały zignorowane")

try:
        code = sys.argv[1].upper()
except IndexError:
        code = input("Podaj kod waluty: ").upper()
    
try:
    date = sys.argv[2]
except IndexError:
    date = input("Podaj datę: ")

date = parser.parse(date)
# print("DATE ->", date)
date_string = date.strftime("%Y-%m-%d")
# print("DATE STRING: ", date_string)

URL = f'http://api.nbp.pl/api/exchangerates/rates/{TABLE}/{code}/{date_string}/?format=json'
# print("URL: = ", URL)
resp = requests.get(URL)

if not resp.ok:
    print(f"Brak danych z dnia {date_string}")
    sys.exit(1)

# print('resp.ok =', resp.ok)
# print('type(resp) =', type(resp))
# print("RESP: ", resp)

content = resp.json()
value = content["rates"][0]["mid"]
description = content["currency"]

print(f"1 {code} ({description}) -> {value} PLN w dniu {date_string}")

# Nie otrzymujemy od razu zawartości strony jako string, tylko obiekt response. To podobnie jak w przypadku plików, gdzie korzystaliśmy ze strumieni.

# Sprawdźmy najpierw, czy nie było jakiegoś błędu - np. serwer Wikipedii mógł zwrócić informację, że nasze żądanie jest niepoprawne (np. niepoprawny URL).



# Wyświetly jak wygląda HTML Wikipedii:

# print()
# print(resp.text)

### 🔴 Ćwiczenie


# with open(OUTPUT_FILE, "w", encoding="utf-8") as stream:
#     stream.write(resp.text)
#     print(f"Zapisano w {OUTPUT_FILE} :-)")

# Wejdź na stronę API Narodowego Banku Polskiego, pobierz stamtąd aktualne kursy walut (URL: http://api.nbp.pl/api/exchangerates/tables/a/), a następnie zapisz je do pliku kursy.json.