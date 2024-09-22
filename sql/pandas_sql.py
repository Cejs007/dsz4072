# %%
import pandas as pd
import mysql.connector

# %%
# připojit k databázi - db object pro referenci na připojení
db = mysql.connector.connect(
  host="localhost", # server - u nás na PC localhost, jinak např. https://svatky.adresa.info/
  user="root", # přihlášení
  password="root",
  database="car_rental" # výběr schématu/db -> odpovídá sql: use nase_db;
)
# cursor -> object, přes který provádím sql příkazy pomocí execute
cursor = db.cursor()

# %%
sql = """select clients.first_name, clients.last_name, 
avg(bookings.total_amount) as 'Average_reservations_price', 
count(bookings.car_id) as 'Number_of_rented_cars'
from bookings
left join clients on
bookings.client_id=clients.client_id
group by bookings.client_id
having Number_of_rented_cars > 1
order by Number_of_rented_cars desc;
"""

# %%
tabulka = pd.read_sql(sql, db)
tabulka


