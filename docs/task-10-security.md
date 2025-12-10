# Bonus Task 10 – Security (HTTPS + JWT Authentication)

For Bonus Task 10 I added security to the Smart Plant Care System (SPCS) backend  
using **HTTPS** (Azure App Service) and **JWT tokens** for authentication in the REST API.

---

## 1. HTTPS

The backend is deployed on **Azure App Service**, which provides HTTPS/TLS by default.

Public URL:

- `https://spcs-backend-yunus-doruk-gafsc7h7fwa2g3em.switzerlandnorth-01.azurewebsites.net`

All API calls are made over **HTTPS**, so the communication between clients and the server  
is encrypted using TLS.

---

## 2. JWT Authentication in the REST API

I implemented **JWT-based authentication** using:

- `python-jose[cryptography]` – signing and verifying JWT tokens
- `passlib` – password hashing (pbkdf2_sha256)
- `python-multipart` – form-data parsing for the login endpoint
- FastAPI’s `OAuth2PasswordBearer` and `OAuth2PasswordRequestForm`

New dependencies added in `backend/requirements.txt`:

```text
python-jose[cryptography]
passlib
python-multipart
