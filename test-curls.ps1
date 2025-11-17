curl -Uri http://127.0.0.1:5000/students -Method POST -Body '{"name": "Alice", "major": "Business", "email": "avail@floridapoly.edu"}' -ContentType "application/json"
curl -Uri http://127.0.0.1:5000/students -Method POST -Body '{"name": "John", "major": "CS", "email": "jceleste@floridapoly.edu"}' -ContentType "application/json"
curl -Uri http://127.0.0.1:5000/housing -Method POST -Body '{"student_id": 1, "housing_status": "pending"}' -ContentType "application/json"

curl -Uri 127.0.0.1:5000/students/1/verify -Method GET
curl -Uri 127.0.0.1:5000/students/2/verify -Method GET

curl -Uri 127.0.0.1:5000/housing/1 -Method PUT -Body '{"housing_status": "verified"}' -ContentType "application/json"

curl -Uri 127.0.0.1:5000/students/1/verify -Method GET

curl -Uri 127.0.0.1:5000/housing/1 -Method DELETE

curl -Uri 127.0.0.1:5000/students/1/verify -Method GET

curl -Uri 127.0.0.1:5000/students/1 -Method DELETE
curl -Uri 127.0.0.1:5000/students/2 -Method DELETE