## 🛠️ Installation

### 1. Clone the repo

```bash
git clone https://github.com/rejoy96/snipbox-machine-task.git
cd snipbox-machine-task


python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

cd snipbox_backend


Login

curl --location 'http://localhost:8000/api/token/' \
--header 'Content-Type: application/json' \
--data '{"username": "admin1", "password": "admin1"}'


Refresh token 

curl --location 'http://localhost:8000/api/token/refresh/' \
--header 'Content-Type: application/json' \
--data '{
    "refresh": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTc1NDg5MDQ3OCwiaWF0IjoxNzUyMjk4NDc4LCJqdGkiOiI0OGM1MWI3OWNhYTk0OTY3OTBiMDBmMzE5ZDZkODg3MSIsInVzZXJfaWQiOjJ9.wCiL_THrd2_CWZcr85msSXNBT1FZjfH720-PEJXtReA"
  }'

Kindly replace the refresh tokens and ids in the url as needed

Create snippet

curl --location 'http://localhost:8000/api/snippets/create/' \
--header 'Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzUyMjk3NzQ2LCJpYXQiOjE3NTIyOTc0NDYsImp0aSI6IjcxZDg2YWFlYjgxYjRhZGVhNTY1OGE4ZGQ4NGI3MjcyIiwidXNlcl9pZCI6Mn0.gtp5ajQY5fQWhA19sK8vN_jnqolguRltMuxbh_iqwg8' \
--header 'Content-Type: application/json' \
--data '{
    "title": "Test Snippet 1",
    "note": "This is a test.",
    "tag": "demo"
  }'



detail 

curl --location 'http://localhost:8000/api/snippets/1/' \
--header 'Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzUyMjk4NTg0LCJpYXQiOjE3NTIyOTgyODQsImp0aSI6ImI2OWZjYTA3MTk5MzQ3NTZhMWMzZWFjMjdmYmMzZTRhIiwidXNlcl9pZCI6Mn0.Xqlb3HMO7YKdPsGkuwvaZUD2gjDLGVhUHQ5GhHzaJM0'



Edit

curl --location --request PUT 'http://localhost:8000/api/snippets/1/update/' \
--header 'Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzUyOTAzMjc4LCJpYXQiOjE3NTIyOTg0NzgsImp0aSI6Ijg2OTllYTU2M2U0MDQ2NTc4MzkxYmQwYWJhNzVlOGRlIiwidXNlcl9pZCI6Mn0.WoZgD4g4LRVSV_FlEtuGcnIfvocFmy9F7h3QsjdDHHE' \
--header 'Content-Type: application/json' \
--data '{
    "title": "Updated Snippet",
    "note": "Updated note content.",
    "tag": "updated-tag"
  }'


Delete

curl --location --request DELETE 'http://localhost:8000/api/snippets/3/delete/' \
--header 'Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzUyOTAzMjc4LCJpYXQiOjE3NTIyOTg0NzgsImp0aSI6Ijg2OTllYTU2M2U0MDQ2NTc4MzkxYmQwYWJhNzVlOGRlIiwidXNlcl9pZCI6Mn0.WoZgD4g4LRVSV_FlEtuGcnIfvocFmy9F7h3QsjdDHHE'


Tag list 

curl --location 'http://localhost:8000/api/tags/' \
--header 'Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzUyOTAzMjc4LCJpYXQiOjE3NTIyOTg0NzgsImp0aSI6Ijg2OTllYTU2M2U0MDQ2NTc4MzkxYmQwYWJhNzVlOGRlIiwidXNlcl9pZCI6Mn0.WoZgD4g4LRVSV_FlEtuGcnIfvocFmy9F7h3QsjdDHHE'


Tag Detail
curl --location 'http://localhost:8000/api/tags/1/' \
--header 'Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzUyOTAzMjc4LCJpYXQiOjE3NTIyOTg0NzgsImp0aSI6Ijg2OTllYTU2M2U0MDQ2NTc4MzkxYmQwYWJhNzVlOGRlIiwidXNlcl9pZCI6Mn0.WoZgD4g4LRVSV_FlEtuGcnIfvocFmy9F7h3QsjdDHHE'



overview
curl --location 'http://localhost:8000/api/snippets/' \
--header 'Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzUyOTAzMjc4LCJpYXQiOjE3NTIyOTg0NzgsImp0aSI6Ijg2OTllYTU2M2U0MDQ2NTc4MzkxYmQwYWJhNzVlOGRlIiwidXNlcl9pZCI6Mn0.WoZgD4g4LRVSV_FlEtuGcnIfvocFmy9F7h3QsjdDHHE'