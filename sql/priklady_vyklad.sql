-- vytvoř databázi
create database nase_db;
-- vyber pracovní databázi
use nase_db;
-- vytvoř tabulku s primarním klíčem, názvem a velikostí populace
create table mesta(
id int primary key auto_increment,
nazev varchar(100) not null,
populace int);
-- ukaž mi sloupce z tabulky
show columns from mesta;
describe starostove;
-- alter -> přidej sloupec
ALTER TABLE mesta ADD zaplavy varchar(10);
-- alter -> change data type
ALTER TABLE mesta MODIFY COLUMN zaplavy TINYINT;
-- create and drop table
create table if not exists k_nicemu(id int);
drop table if exists k_nicemu;

select * from mesta;
INSERT INTO mesta (nazev, populace, zaplavy) VALUES ('Krnov', 24000, 1);
INSERT INTO mesta (nazev, populace, zaplavy) VALUES ('Opava', 80000, 1);
INSERT INTO mesta (nazev, populace, zaplavy) VALUES ('Praha', 1200000, 0);
INSERT INTO mesta (nazev, populace, zaplavy) VALUES ('Havířov', 90000, 1);

select id from mesta where nazev='Praha';
UPDATE mesta SET populace=1000000 WHERE id=3;

delete from mesta where id=3;

select * from mesta;
DESCRIBE mesta;

select * from starostove;
DESCRIBE starostove;


