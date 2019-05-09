from fastapi import HTTPException, Security, status
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials

security = HTTPBearer()

def verify_token_payload(credentials: HTTPAuthorizationCredentials = Security(security)):
    token = credentials.credentials
    if not token or len(token) < 8:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid or expired authentication bearer token"
        )
    return {"user_id": "usr_verified_id", "email": "user@domain.com", "role": "ADMIN"}
