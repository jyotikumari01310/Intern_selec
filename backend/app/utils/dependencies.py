from fastapi import Depends, HTTPException
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from jose import jwt, JWTError

SECRET_KEY = "supersecret"
ALGORITHM = "HS256"

security = HTTPBearer()

def get_current_user(credentials: HTTPAuthorizationCredentials = Depends(security)):
    print("----- DEBUG START -----")

    if credentials is None:
        print("NO CREDENTIALS")
        raise HTTPException(status_code=401, detail="No token")

    print("RAW HEADER:", credentials)

    token = credentials.credentials
    print("TOKEN:", token)

    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        print("DECODED PAYLOAD:", payload)
        print("----- SUCCESS -----")
        return payload
    except JWTError as e:
        print("JWT ERROR:", str(e))
        print("----- FAILED -----")
        raise HTTPException(status_code=401, detail="Invalid token")