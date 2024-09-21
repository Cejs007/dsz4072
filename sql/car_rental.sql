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
