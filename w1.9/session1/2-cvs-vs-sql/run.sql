SELECT COUNT(*) FROM orders o 
JOIN customers c ON o.customer_id = c.customer_id JOIN restaurants r 
ON o.restaurant_id = r.restaurant_id 
WHERE c.name = 'Amara Okafor' AND r.cuisine = 'Italian';

UPDATE restaurants SET postcode = 'LS6 3QR' WHERE name = 'Bella Napoli’;
