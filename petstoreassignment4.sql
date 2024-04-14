-- Create a new database named petstore_management
CREATE DATABASE petstore_management;
-- Switch to the petstore_management database
USE petstore_management;
-- Create a table named Pets_info to store information about books
CREATE TABLE Pets_info (
pet_id INT AUTO_INCREMENT PRIMARY KEY, -- Included a unique identifier for each pet, their name, breed and age 
pet_name VARCHAR(50),
breed VARCHAR (50),
age  INT,
price INT);
-- Insert data into the pets_info table
INSERT INTO Pets_info
-- Specify the columns and their corresponding values
(pet_name, breed, age, price)
-- Insert multiple rows of data using VALUES keyword
VALUES
('Dog', 'Poodle', '2', '500'),
('Cat', 'Ginger', '3', '300'),
('Bird', 'Parrot', '1', '200');
