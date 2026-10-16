--CREATE USER fde_user WITH PASSWORD 'fdepwd';

CREATE TABLE invoices (
invoice_id VARCHAR(20) PRIMARY KEY,
vendor VARCHAR(100) NOT NULL,
amount NUMERIC(12, 2) NOT NULL,
status VARCHAR(30) NOT NULL,
approval VARCHAR(30) NOT NULL
);

 INSERT INTO invoices (invoice_id, vendor, amount, status, approval)
VALUES
('INV-101', 'ABC Ltd', 85000.00, 'PENDING', 'MANAGER_REVIEW'),
('INV-102', 'XYZ Corp', 142500.00, 'PENDING', 'FINANCE_REVIEW'),
('INV-103', 'Nova Inc', 15000.00, 'PENDING', 'STANDARD');