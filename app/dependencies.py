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
