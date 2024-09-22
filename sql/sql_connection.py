# %%
import pandas as pd
import mysql.connector

# %%
# připojit k databázi - db object pro referenci na připojení
db = mysql.connector.connect(
  host="localhost", # server - u nás na PC localhost, jinak např. https://svatky.adresa.info/
  user="root", # přihlášení
  password="root",
  database="nase_db" # výběr schématu/db -> odpovídá sql: use nase_db;
)
# cursor -> object, přes který provádím sql příkazy pomocí execute
cursor = db.cursor()

# %%
# uživatel si zadá data
mesto = input("Zadej mesto: ")
populace = input("Zadej populace: ")
zaplavy = input("Zadej zaplavy: ")

# %%
# query na zapsání dat -> odladit ve workbenchy
sql = f"INSERT INTO mesta (nazev, populace, zaplavy) VALUES ('{mesto}', {populace}, {zaplavy});"
# zkus zapsat
try:
  cursor.execute(sql)
  db.commit()
  print("Úspěch")
except:
  print("Error")

# %%
# přečti data z tabulky města
sql = f"SELECT * from mesta;"
cursor.execute(sql)
vysledek = cursor.fetchall()

# %%
# přečti nastavení tabulky -> názvy sloupců, datové typy apod.
sql = "DESCRIBE mesta;"
cursor.execute(sql)
informace_sloupce = cursor.fetchall()
# extrakce pomocí list comprehension názvu sloupce z metadat
nazvy_sloupce = [col[0] for col in informace_sloupce]

# %%
# zpracuj výsledky -> názvy sloupců z sql describe a data z sql select
tabulka = pd.DataFrame.from_records(vysledek, columns=nazvy_sloupce, index="id")
tabulka


