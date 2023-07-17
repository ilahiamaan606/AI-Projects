#1

    CREATE TABLE Customers (
        id INT PRIMARY KEY,
        name VARCHAR(100),
        email VARCHAR(100),
        address VARCHAR(255),
        phone_number VARCHAR(50)
    );

#2

    INSERT INTO Customers (id, name, email, address, phone_number)
    VALUES (1, 'Amaan', 'varunbhatt@gmail.com', 'Home', '123-456-7890'),
        (2, 'Zeeshan', 'mohsin@gmail.com', 'Home', '555-678-9012'),
        (3, 'Mohit', 'mohit@gmail.com', 'Home', '777-888-9900'),
        (4, 'Faizal', 'faizal@gmail.com', 'Home', '999-000-1111'),
        (5, 'Annanya', 'annanya@gmail.com', 'Home', '222-333-4444');

#3

    SELECT * FROM Customers;

#4

    SELECT name,email FROM Customers;

#5

    SELECT * FROM Customers WHERE id = 3;

#6

    SELECT * FROM Customers WHERE name LIKE 'A%';

#7

    SELECT * FROM Customers ORDER BY name DESC;

#8

    UPDATE Customers SET address = 'India' WHERE id=1;

#9

    SELECT * FROM Customers ORDER BY id ASC LIMIT 3;

#10

    DELETE FROM Customers WHERE id = 2;

#11

    SELECT COUNT(*) FROM Customers;

#12

    SELECT * FROM Customers ORDER BY id ASC LIMIT 2 OFFSET 2;

#13

    SELECT * FROM Customers WHERE id > 2 AND name LIKE 'B%';

#14

    SELECT * FROM Customers WHERE id < 3 OR name LIKE '%s';

#15

    SELECT * FROM Customers WHERE phone_number IS NULL;