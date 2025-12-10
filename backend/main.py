from datetime import datetime, timedelta
from typing import Optional

from fastapi import FastAPI, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from jose import JWTError, jwt
from passlib.context import CryptContext
from pydantic import BaseModel

app = FastAPI(
    title="Smart Plant Care System API",
    description="REST API for SPCS – telemetry & watering commands",
    version="1.0.0",
)
# -----------------------------
# JWT / Security configuration
# -----------------------------
SECRET_KEY = "change_this_secret_key_to_something_random_and_long"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

pwd_context = CryptContext(schemes=["pbkdf2_sha256"], deprecated="auto")
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/api/token")


class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    username: Optional[str] = None


class User(BaseModel):
    username: str
    full_name: Optional[str] = None
    disabled: Optional[bool] = None


class UserInDB(User):
    hashed_password: str


# Demo amaçlı basit kullanıcı veritabanı (hard-coded)
fake_users_db = {
    "demo-user": {
        "username": "demo-user",
        "full_name": "Demo User",
        "disabled": False,
        # password = "demo-password"
        "hashed_password": pwd_context.hash("demo-password"),
    }
}


def verify_password(plain_password: str, hashed_password: str) -> bool:
    return pwd_context.verify(plain_password, hashed_password)


def get_user(db, username: str) -> Optional[UserInDB]:
    if username in db:
        user_dict = db[username]
        return UserInDB(**user_dict)
    return None


def authenticate_user(username: str, password: str) -> Optional[UserInDB]:
    user = get_user(fake_users_db, username)
    if not user:
        return None
    if not verify_password(password, user.hashed_password):
        return None
    return user


def create_access_token(data: dict, expires_delta: Optional[timedelta] = None) -> str:
    to_encode = data.copy()
    expire = datetime.utcnow() + (expires_delta or timedelta(minutes=15))
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt


async def get_current_user(token: str = Depends(oauth2_scheme)) -> User:
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username: str = payload.get("sub")
        if username is None:
            raise credentials_exception
        token_data = TokenData(username=username)
    except JWTError:
        raise credentials_exception

    user = get_user(fake_users_db, username=token_data.username)
    if user is None:
        raise credentials_exception
    return user


async def get_current_active_user(current_user: User = Depends(get_current_user)) -> User:
    if current_user.disabled:
        raise HTTPException(status_code=400, detail="Inactive user")
    return current_user


class WateringRequest(BaseModel):
    duration_seconds: int

@app.post("/api/token", response_model=Token)
async def login_for_access_token(form_data: OAuth2PasswordRequestForm = Depends()):
    """
    OAuth2 password flow ile token üretir.
    Kullanıcı adı / şifre doğruysa access_token döner.
    """
    user = authenticate_user(form_data.username, form_data.password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )

    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data={"sub": user.username},
        expires_delta=access_token_expires,
    )
    return {"access_token": access_token, "token_type": "bearer"}


@app.get("/api/health")
def health_check():
    """
    Basit health endpoint – API ayakta mı?
    """
    return {
        "status": "ok",
        "service": "spcs-backend",
        "timestamp": datetime.utcnow().isoformat(),
    }


@app.get("/api/telemetry/latest")
async def get_latest_telemetry(current_user: User = Depends(get_current_active_user)):
    """
    Şimdilik dummy veri döndürüyoruz.
    Bu endpoint artık JWT ile korunuyor (Bearer token gerekli).
    """
    return {
        "device_id": "spcs-simulator-1",
        "soil_moisture": 41.5,
        "light_level": 73.2,
        "temperature": 24.3,
        "timestamp": datetime.utcnow().isoformat() + "Z",
        "user": current_user.username,
    }


@app.post("/api/water")
async def send_watering_command(
    body: WateringRequest,
    current_user: User = Depends(get_current_active_user),
):
    """
    Sulama komutu simülasyonu.
    Bu endpoint artık JWT ile korunuyor (Bearer token gerekli).
    """
    return {
        "device_id": "spcs-simulator-1",
        "command": "water",
        "duration_seconds": body.duration_seconds,
        "status": "accepted",
        "timestamp": datetime.utcnow().isoformat() + "Z",
        "user": current_user.username,
    }

