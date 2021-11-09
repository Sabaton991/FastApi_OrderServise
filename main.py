from datetime import datetime, timedelta

from fastapi import FastAPI, Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from starlette import status

from db_models.tokenModel import Token
from db_models.userModel import User
from routers import items
from jose import jwt
from passlib.context import CryptContext

app = FastAPI()

app.include_router(items.router)

SECRET_KEY = "3c924233c368c9a5b0c2f19c9b2904c05cf5a98b6c842a650328c1ee03fe93bb"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

test_users = {'oleg': {
    "hashed_password": "$2b$12$EixZaYVK1fsbw1ZfbX3OXePaWxn96p36WQoeG6Lruj3vjPGga31lW",
    "surname": "orlov",
    "name": "oleg",
    "last_name": "",
    "gender": "male",
    "phone": "+79999999999",
    'email': 'test@test.ru'
}}


@app.get('/')
def base_route():
    return {'data': 'Hello'}


def verify_password(user_password, hashed_password):
    return pwd_context.verify(user_password, hashed_password)


def get_password_hash(password):
    return pwd_context.hash(password)


def get_user(username, db):
    if username in db:
        user_dict = db[username]
        return User(**user_dict)


def authenticate_user(test_users, username: str, password: str):
    user = get_user(test_users, username)
    if not user:
        return False
    if not verify_password(password, user.hashed_password):
        return False
    return user


def create_access_token(data: dict, expires_delta):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=15)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt


@app.post("/token", response_model=Token)
async def login_for_access_token(form_data: OAuth2PasswordRequestForm = Depends()):
    user = authenticate_user(test_users, form_data.username, form_data.password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data={"sub": user.name}, expires_delta=access_token_expires
    )
    return {"access_token": access_token, "token_type": "bearer"}
