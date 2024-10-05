# %%
import pandas as pd
import mysql.connector

# %%
# připojit k databázi - db object pro referenci na připojení
db = mysql.connector.connect(
  host="localhost", # server - u nás na PC localhost, jinak např. https://svatky.adresa.info/
  user="root", # přihlášení
  password="root",
  database="vs_zkouska" # výběr schématu/db -> odpovídá sql: use nase_db;
)
# cursor -> object, přes který provádím sql příkazy pomocí execute
cursor = db.cursor()

# %%
sql = f"show columns from student;"
cursor.execute(sql)
vysledek = cursor.fetchall()

# %%
vysledek

# %% [markdown]
# ### Naplnit daty

# %%
from faker import Faker
from random import randint

# %%
fake = Faker()
kolik = 100
lide = []
for i in range(kolik):
    full_name = fake.name()
    jmeno = full_name.split(" ")[0]
    prijmeni = full_name.split(" ")[-1]
    vek = randint(19, 28)
    lide.append([jmeno, prijmeni, vek])

# %%
def vygeneruj_nahodne_lidi(pocet, vek_od=18, vek_do=28):
    """
    vezme na vstupu počet lidí k vygenerování a vrátí list, kde jednotlivé prvky jsou listy se 3 hodnotami
    a to jméno, příjmení a věk
    """
    # z knihovny faker vytvoř generátor náhodných lidí
    fake = Faker()
    # list pro ukládání lidí
    lide = []
    # zopakuj pocet krát generování člověka
    for i in range(pocet):
        # dej mi plné jméno náhodného člověka
        full_name = fake.name()
        # plné jméno je ve formátu 'jmeno prijmeni' -> rozděl text podle mezery, kdy první hodnota je jméno a druhá příjmení
        jmeno = full_name.split(" ")[0]
        prijmeni = full_name.split(" ")[-1]
        # vygeneruj náhodný věk
        vek = randint(vek_od, vek_do)
        # přidej do listu lidé všechny informace jako list
        lide.append((jmeno, prijmeni, vek))
    return lide

# %%
studenti = tuple(vygeneruj_nahodne_lidi(100))

sql = "INSERT INTO student (jmeno, prijmeni, vek) VALUES "

# constructing sql statment with multiple row values
for row in studenti:
    sql += "('{}','{}','{}'),".format(row[0], row[1], row[2])

sql = sql[:-1]

try:
  cursor.execute(sql)
  db.commit()
  print("Úspěch")
except Exception as error:
  print(f"Error: {error}")

# %%
ucitele = tuple(vygeneruj_nahodne_lidi(10, 25, 80))

sql = "INSERT INTO ucitel (jmeno, prijmeni, vek) VALUES "

# constructing sql statment with multiple row values
for row in ucitele:
    sql += "('{}','{}','{}'),".format(row[0], row[1], row[2])

sql = sql[:-1]

try:
  cursor.execute(sql)
  db.commit()
  print("Úspěch")
except Exception as error:
  print(f"Error: {error}")

# %%
ucitele = tuple(vygeneruj_nahodne_lidi(10, 25, 80))

sql = "INSERT INTO ucitel (jmeno, prijmeni, vek) VALUES "

# constructing sql statment with multiple row values
for row in ucitele:
    sql += "('{}','{}','{}'),".format(row[0], row[1], row[2])

sql = sql[:-1]

try:
  cursor.execute(sql)
  db.commit()
  print("Úspěch")
except Exception as error:
  print(f"Error: {error}")

# %%
mistnosti = []
for i in range(3):
    zeme = input("Zadej zemi: ")
    mesto = input("Zadej město: ")
    adresa = input("Zadej adresu: ")
    ucebna = input("Zadej název učebny: ")
    mistnosti.append((zeme, mesto, adresa, ucebna))

# %%
sql = "INSERT INTO misto (zeme, mesto, adresa, ucebna) VALUES "

# constructing sql statment with multiple row values
for row in mistnosti:
    sql += "('{}','{}','{}','{}'),".format(row[0], row[1], row[2], row[3])

sql = sql[:-1]

try:
  cursor.execute(sql)
  db.commit()
  print("Úspěch")
except Exception as error:
  print(f"Error: {error}")

# %%
sql = f"select iducitel from ucitel;"
cursor.execute(sql)
vysledek = cursor.fetchall()

ucitelska_id = [prvek[0] for prvek in vysledek]

# %%
from random import choice

# %%
predmety = []
for i in range(3):
    nazev = input("Zadej nazev: ")
    obor = input("Zadej obor: ")
    ucitel_iducitel = choice(ucitelska_id)
    predmety.append((nazev, obor, ucitel_iducitel))

# %%
sql = "INSERT INTO predmet (nazev, obor, ucitel_iducitel) VALUES "

# constructing sql statment with multiple row values
for row in predmety:
    sql += "('{}','{}','{}'),".format(row[0], row[1], row[2])

sql = sql[:-1]

try:
  cursor.execute(sql)
  db.commit()
  print("Úspěch")
except Exception as error:
  print(f"Error: {error}")

# %%
sql = f"select iducitel from ucitel;"
cursor.execute(sql)
vysledek = cursor.fetchall()

ucitel_id = [prvek[0] for prvek in vysledek]

sql = f"select idstudent from student;"
cursor.execute(sql)
vysledek = cursor.fetchall()

student_id = [prvek[0] for prvek in vysledek]

sql = f"select idpredmet from predmet;"
cursor.execute(sql)
vysledek = cursor.fetchall()

predmet_id = [prvek[0] for prvek in vysledek]

sql = f"select idmisto from misto;"
cursor.execute(sql)
vysledek = cursor.fetchall()

misto_id = [prvek[0] for prvek in vysledek]

# %%
zkousky = []
for i in range(3):
    termin = input("Zadej termín ve formátu '2024-10-05': ")
    online = input("Bude online: ")
    ucitel_iducitel = choice(ucitel_id)
    misto_idmisto = choice(misto_id)
    student_idstudent = choice(student_id)
    predmet_idpredmet = choice(predmet_id)
    zkousky.append((termin, online, ucitel_iducitel, misto_idmisto, student_idstudent, predmet_idpredmet))

# %%
sql = "INSERT INTO zkouska (termin, online, ucitel_iducitel, misto_idmisto, student_idstudent, predmet_idpredmet) VALUES "

# constructing sql statment with multiple row values
for row in zkousky:
    sql += "('{}','{}','{}','{}','{}','{}'),".format(row[0], row[1], row[2], row[3], row[4], row[5])

sql = sql[:-1]

try:
  cursor.execute(sql)
  db.commit()
  print("Úspěch")
except Exception as error:
  print(f"Error: {error}")

# %%
sql = f"select idzkouska from zkouska;"
cursor.execute(sql)
vysledek = cursor.fetchall()

zkouska_id = [prvek[0] for prvek in vysledek]

# %%
vysledky = []
for i in range(3):
    prospel = input("Zadej prospel: ")
    body = input("Zadej body: ")
    komentar = input("Zadej komentar: ")
    zkouska_idzkouska = choice(zkouska_id)
    vysledky.append((prospel, body, komentar, zkouska_idzkouska))

# %%
sql = "INSERT INTO vysledek (prospel, body, komentar, zkouska_idzkouska) VALUES "

# constructing sql statment with multiple row values
for row in vysledky:
    sql += "('{}','{}','{}','{}'),".format(row[0], row[1], row[2], row[3])

sql = sql[:-1]

try:
  cursor.execute(sql)
  db.commit()
  print("Úspěch")
except Exception as error:
  print(f"Error: {error}")


