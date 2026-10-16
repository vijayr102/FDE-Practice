CREATE TABLE users (
user_id VARCHAR(20) PRIMARY KEY,cls
name VARCHAR(100) NOT NULL,
amount NUMERIC(12, 2) NOT NULL
);

CREATE TABLE vendors (
vendor_id VARCHAR(20) PRIMARY KEY,
name VARCHAR(100) NOT NULL,
amount NUMERIC(12, 2) NOT NULL
);

CREATE TABLE transactions (
transaction_id VARCHAR(20) PRIMARY KEY, 
user_id VARCHAR(20) REFERENCES users(user_id),
vendor_id VARCHAR(20) REFERENCES vendors(vendor_id),
amount NUMERIC(12, 2) NOT NULL,
transaction_date TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
);

insert into users (user_id, name, amount) values
('U001', 'Alice', 1000.00),
('U002', 'Bob', 1500.00),
('U003', 'Charlie', 2000.00);

insert into vendors (vendor_id, name, amount) values
('V001', 'Vendor A', 5000.00),
('V002', 'Vendor B', 7500.00),
('V003', 'Vendor C', 10000.00);

insert into transactions (transaction_id, user_id, vendor_id, amount) values
('T001', 'U001', 'V001', 100.00),
('T002', 'U002', 'V002', 200.00),
('T003', 'U003', 'V003', 300.00);

SELECT * FROM transactions