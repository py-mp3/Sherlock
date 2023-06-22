-- Active: 1686847344535@@127.0.0.1@3306
create database go_user;

use go_user;

create table users(id int AUTO_INCREMENT primary key , username varchar(50) unique , password varchar(20));

insert into users(username , password) values("shubh" , "scam1992");

select * from users;

create table user_data(id int AUTO_INCREMENT PRIMARY key , )