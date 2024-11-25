INSERT INTO company (id, name, address, phone) VALUES
(1, 'Company K', '808 Fir St', '123-456-7891'),
(2, 'Company L', '909 Maple St', '234-567-8902'),
(3, 'Company M', '1010 Spruce St', '345-678-9013'),
(4, 'Company N', '1111 Sycamore St', '456-789-0124'),
(5, 'Company O', '1212 Redwood St', '567-890-1235'),
(6, 'Company P', '1313 Cypress St', '678-901-2346'),
(7, 'Company Q', '1414 Alder St', '789-012-3457'),
(8, 'Company R', '1515 Sequoia St', '890-123-4568'),
(9, 'Company S', '1616 Beech St', '901-234-5679'),
(10, 'Company T', '1717 Magnolia St', '012-345-6780');

INSERT INTO terminal (id, company_id, address, gps, manufacturer, date) VALUES
(1, 1, '808 Fir St', '49.8410,24.0315', 'TermX', '2023-02-11'),
(2, 2, '909 Maple St', '49.8421,24.0320', 'TermY', '2023-02-12'),
(3, 3, '1010 Spruce St', '49.8431,24.0325', 'TermZ', '2023-02-13'),
(4, 4, '1111 Sycamore St', '49.8441,24.0330', 'TermA', '2023-02-14'),
(5, 5, '1212 Redwood St', '49.8451,24.0335', 'TermB', '2023-02-15'),
(6, 6, '1313 Cypress St', '49.8461,24.0340', 'TermC', '2023-02-16'),
(7, 7, '1414 Alder St', '49.8471,24.0345', 'TermD', '2023-02-17'),
(8, 8, '1515 Sequoia St', '49.8481,24.0350', 'TermE', '2023-02-18'),
(9, 9, '1616 Beech St', '49.8491,24.0355', 'TermF', '2023-02-19'),
(10, 10, '1717 Magnolia St', '49.8501,24.0360', 'TermG', '2023-02-20');

INSERT INTO service_type (id, name) VALUES
(1, 'Testing'),
(2, 'Installation and Setup'),
(3, 'Troubleshooting'),
(4, 'Upgrade Assistance'),
(5, 'Preventive Maintenance'),
(6, 'Software Update'),
(7, 'Hardware Replacement'),
(8, 'Diagnostics'),
(9, 'Calibration'),
(10, 'Inspection');

INSERT INTO client (id, name, phone) VALUES
(1, 'Client K', '123-456-7891'),
(2, 'Client L', '234-567-8902'),
(3, 'Client M', '345-678-9013'),
(4, 'Client N', '456-789-0124'),
(5, 'Client O', '567-890-1235'),
(6, 'Client P', '678-901-2346'),
(7, 'Client Q', '789-012-3457'),
(8, 'Client R', '890-123-4568'),
(9, 'Client S', '901-234-5679'),
(10, 'Client T', '012-345-6780');

INSERT INTO payment_method (id, name) VALUES
(1, 'Credit Card'),
(2, 'Cash'),
(3, 'Bank Transfer'),
(4, 'Mobile Payment'),
(5, 'Check'),
(6, 'PayPal'),
(7, 'Cryptocurrency'),
(8, 'Gift Card'),
(9, 'Wire Transfer'),
(10, 'Apple Pay');

INSERT INTO payment (id, payment_method_id, date, payment_amount) VALUES
(1, 1, '2023-02-11', 120.00),
(2, 2, '2023-02-12', 160.00),
(3, 3, '2023-02-13', 220.00),
(4, 4, '2023-02-14', 270.00),
(5, 5, '2023-02-15', 320.00),
(6, 6, '2023-02-16', 370.00),
(7, 7, '2023-02-17', 420.00),
(8, 8, '2023-02-18', 470.00),
(9, 9, '2023-02-19', 520.00),
(10, 10, '2023-02-20', 580.00);

INSERT INTO invoice (payment_id, id, client_id, date, total_amount) VALUES
(1, 1, 1, '2023-02-11', 120.00),
(2, 2, 2, '2023-02-12', 160.00),
(3, 3, 3, '2023-02-13', 220.00),
(4, 4, 4, '2023-02-14', 270.00),
(5, 5, 5, '2023-02-15', 320.00),
(6, 6, 6, '2023-02-16', 370.00),
(7, 7, 7, '2023-02-17', 420.00),
(8, 8, 8, '2023-02-18', 470.00),
(9, 9, 9, '2023-02-19', 520.00),
(10, 10, 10, '2023-02-20', 580.00);

INSERT INTO service (id, terminal_id, date, cost, invoice_client_id, invoice_payment_id, invoice_id, service_type_id) VALUES
(1, 1, '2023-02-11', 120.00, 1, 1, 1, 1),
(2, 2, '2023-02-12', 160.00, 2, 2, 2, 2),
(3, 3, '2023-02-13', 220.00, 3, 3, 3, 3),
(4, 4, '2023-02-14', 270.00, 4, 4, 4, 4),
(5, 5, '2023-02-15', 320.00, 5, 5, 5, 5),
(6, 6, '2023-02-16', 370.00, 6, 6, 6, 1),
(7, 7, '2023-02-17', 420.00, 7, 7, 7, 2),
(8, 8, '2023-02-18', 470.00, 8, 8, 8, 3),
(9, 9, '2023-02-19', 520.00, 9, 9, 9, 4),
(10, 10, '2023-02-20', 580.00, 10, 10, 10, 5);

INSERT INTO master (id, first_name, last_name, specialization) VALUES
(1, 'Ethan', 'Thomas', 'Plumber'),
(2, 'Olivia', 'Martin', 'Network Engineer'),
(3, 'Mia', 'Lee', 'IT Specialist'),
(4, 'Noah', 'Brown', 'Electrician'),
(5, 'Sophia', 'Harris', 'Software Developer'),
(6, 'Liam', 'Young', 'HVAC Technician'),
(7, 'Ava', 'Clark', 'Database Administrator'),
(8, 'Elijah', 'Lewis', 'Security Specialist'),
(9, 'Isabella', 'Walker', 'Cloud Engineer'),
(10, 'Lucas', 'Hall', 'Data Analyst');

INSERT INTO service_master (service_id, master_id, work_duration, cost) VALUES
(1, 1, 1.4, 120.00),
(2, 2, 2.0, 160.00),
(3, 3, 2.5, 220.00),
(4, 4, 1.8, 270.00),
(5, 5, 2.2, 320.00),
(6, 6, 3.0, 370.00),
(7, 7, 2.1, 420.00),
(8, 8, 1.7, 470.00),
(9, 9, 2.3, 520.00),
(10, 10, 3.1, 580.00);