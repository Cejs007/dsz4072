# %%
from sqlalchemy import create_engine
import pandas as pd

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import sessionmaker
from sqlalchemy import text

# %%
# base for table classes
Base = declarative_base()

# %%
# class -> musí přesně odpovídat tabulce v databázi
class Mesta(Base):
    # název tabulky - stejný
    __tablename__ = 'mesta'

    # sloupce a datové typy - stejné
    id = Column(Integer, primary_key=True)
    nazev = Column(String)
    populace = Column(Integer)
    zaplavy = Column(Integer)

    # klasický init -> když chci založit nový záznam, ať mám všechno
    def __init__(self, nazev, populace, zaplavy):
        self.nazev = nazev
        self.populace = populace
        self.zaplavy = zaplavy

# %%
# sample class mapping table from database
class Starostove(Base):
    __tablename__ = 'starostove'

    # fields and their types
    idstarostove = Column(Integer, primary_key=True)
    jmeno = Column(String)
    prijmeni = Column(String)
    vek = Column(Integer)
    mesta_id = Column(Integer)

    def __init__(self, jmeno, prijmeni, vek, mesta_id):
        self.jmeno = jmeno
        self.prijmeni = prijmeni
        self.vek = vek
        self.mesta_id = mesta_id

# %%
# připojení na db - odpovídá "mysql.connector.connect"
engine = create_engine('mysql+pymysql://root:root@localhost/nase_db')
# sessions -> odpovídá kurzoru
Session = sessionmaker(bind=engine)
session = Session()

# %%
# bez použití sql -> vytvořím objekt podle třídy starosta -> propíše se do databáze po commitu
starosta = Starostove('Michal', "Maliszewski", 31, 7)
session.add(starosta)

# %%
mesto = Mesta('Brno', 400000, 0)
session.add(mesto)

# %%
# provést změny na databázi
session.commit()

# %%
# načtení dat pomocí orm
with engine.connect() as con:
    query = f"SELECT * FROM mesta;"
    data = con.execute(text(query))

# %%
# zpracuj výsledky -> názvy sloupců z sql describe a data z sql select
tabulka = pd.DataFrame.from_records(data)
tabulka


