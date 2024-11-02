from typing import Annotated
from fastapi import HTTPException, Header
from .config import SECRET_KEY
service_map = {
    "/auth": "http://auth-svc",
    "/deploy": "http://deployer-svc",
    "/list": "http://lister-svc",
    "/delete": "http://deleter-svc",
    "/admin": "http://admin-svc",
}

async def get_token_header(X_TOKEN: Annotated[str, Header()]):
    if X_TOKEN != SECRET_KEY:
        raise HTTPException(status_code=400, detail="X-Token header invalid")
