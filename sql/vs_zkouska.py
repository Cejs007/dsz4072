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
        lide.append([jmeno, prijmeni, vek])
    return lide

# %%
vygeneruj_nahodne_lidi(5, 80, 90)

# %%



