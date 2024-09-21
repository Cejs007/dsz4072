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