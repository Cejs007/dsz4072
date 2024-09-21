create database if not exists car_rental;
use car_rental;

create table if not exists cars(
car_id int primary key,
manufacturer varchar(50),
model varchar(50),
year int,
horse_power int,
price_per_day int);

create table if not exists clients(
client_id int primary key,
first_name varchar(50),
last_name varchar (50),
address varchar (50),
city varchar (50));

create table if not exists bookings(
booking_id int primary key,
client_id int,
car_id int,
total_amount int,
start_date datetime,
end_date datetime);

alter table cars MODIFY car_id INT AUTO_INCREMENT;
show columns from cars;
alter table clients MODIFY client_id INT AUTO_INCREMENT;
show columns from clients;
alter table bookings MODIFY booking_id INT AUTO_INCREMENT;
show columns from bookings;

ALTER TABLE bookings ADD CONSTRAINT
cars_fk FOREIGN KEY (car_id)
REFERENCES cars(car_id);

ALTER TABLE bookings ADD CONSTRAINT
clients_fk FOREIGN KEY (client_id)
REFERENCES clients(client_id);

show columns from bookings;

insert into clients (first_name, last_name, address, city) values
('John', 'Smith', 'Front Street 12', 'Los Angeles'),
('Andrew', 'Jones', 'Back Street 43', 'New York');

insert into clients (first_name, last_name, address, city) values ('John', 'Smith', 'Front Street 12', 'Los Angeles');
insert into clients (first_name, last_name, address, city) values ('Andrew', 'Jones', 'Back Street 43', 'New York');
select * from clients;
insert into cars (manufacturer, model, year, horse_power, price_per_day) values ('Seat', 'Leon', 2016, 80, 200);
insert into cars (manufacturer, model, year, horse_power, price_per_day) values ('Toyota', 'Avensis', 2014, 72, 100);
select * from cars;
insert into bookings (client_id, car_id, start_date, end_date, total_amount) values (1, 2, '2020-07-05', '2020-07-06', 100);
insert into bookings (client_id, car_id, start_date, end_date, total_amount) values (2, 2, '2020-07-10', '2020-07-12', 200);
select * from bookings;

update clients set first_name='Michal', last_name='Maliszewski', address='ČR', city='Těrlicko' where client_id=1;
select booking_id from bookings where client_id=1;
delete from bookings where booking_id=1;
delete from clients where client_id=1;

insert into clients (first_name, last_name, address, city) values ('Miloš', 'Zeman', 'Vysočina', 'Les');
insert into clients (first_name, last_name, address, city) values ('Petr', 'Pavel', 'Pražský hrad', 'Praha');

delete from bookings where booking_id > 0;
alter table bookings AUTO_INCREMENT = 1;
delete from clients where client_id > 0;
alter table clients AUTO_INCREMENT = 1;
delete from cars where car_id > 0;
alter table cars AUTO_INCREMENT = 1;

INSERT INTO clients (first_name, last_name, address, city) VALUES
 ('Michal', 'Taki', 'os. Srodkowe 12', 'Poznan'),
 ('Pawel', 'Ktory', 'ul. Stara 11', 'Gdynia'),
 ('Anna', 'Inna', 'os. Srednie 1', 'Gniezno'),
 ('Alicja', 'Panna', 'os. Duze 33', 'Torun'),
 ('Damian', 'Papa', 'ul. Skosna 66', 'Warszawa'),
 ('Marek', 'Troska', 'os. Male 90', 'Radom'),
 ('Jakub', 'Klos', 'os. Polskie 19', 'Wadowice'),
 ('Lukasz', 'Lis', 'os. Podlaskie 90', 'Bialystok');
 
INSERT INTO cars (manufacturer, model, year, horse_power, price_per_day) VALUES
 ('Mercedes', 'CLK', 2018, 190, 400),
 ('Hyundai', 'Coupe', 2014, 165, 300),
 ('Dacia', 'Logan', 2015, 103, 150),
 ('Saab', '95', 2012, 140, 140),
 ('BMW', 'E36', 2007, 110, 80),
 ('Fiat', 'Panda', 2016, 77, 190),
 ('Honda', 'Civic', 2019, 130, 360),
 ('Volvo', 'XC70', 2013, 180, 280);
 
 INSERT INTO bookings (client_id, car_id, start_date,
end_date, total_amount) VALUES
 (3, 3, '2020-07-06', '2020-07-08', 400),
 (6, 4, '2020-07-10', '2020-07-16', 1680),
 (4, 5, '2020-07-11', '2020-07-14', 450),
 (5, 4, '2020-07-11', '2020-07-13', 600),
 (7, 3, '2020-07-12', '2020-07-14', 800),
 (5, 7, '2020-07-14', '2020-07-17', 240),
 (3, 8, '2020-07-14', '2020-07-16', 380),
 (5, 2, '2020-07-15', '2020-07-18', 1080),
 (6, 3, '2020-07-16', '2020-07-20', 1120),
 (8, 4, '2020-07-16', '2020-07-19', 600),
 (3, 2, '2020-07-16', '2020-07-21', 500),
 (2, 6, '2020-07-17', '2020-07-19', 280),
 (3, 4, '2020-07-17', '2020-07-19', 720),
 (3, 7, '2020-07-18', '2020-07-21', 240),
 (5, 4, '2020-07-18', '2020-07-22', 1200);

select * from cars where year > 2015;
select * from bookings where total_amount between 1000 and 2555;
select client_id from clients where first_name like 'A%' and last_name like '%a';

select * from clients where client_id in (3, 4);

select * from bookings;

SELECT clients.first_name, bookings.total_amount FROM clients, bookings;

select * from bookings;

SELECT clients.first_name, bookings.total_amount
FROM clients
LEFT JOIN bookings ON
clients.client_id=bookings.client_id
order by clients.first_name asc;
