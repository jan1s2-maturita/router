# app/middlewares.py

import time
from fastapi import Request, HTTPException
from fastapi.responses import JSONResponse


# Logging Middleware
async def LogMiddleware(request: Request, call_next):
    start_time = time.time()
    response = await call_next(request)
    process_time = time.time() - start_time
    print(f"Method: {request.method}, URL: {request.url}, Status Code: {response.status_code}, Time: {process_time:.4f}s")
    return response

# Authentication Middleware
async def AuthMiddleware(request: Request, call_next):
    token = request.headers.get("X-Auth-Token")
    if token != "secret":
        raise HTTPException(status_code=401, detail="Unauthorized")
    
    return await call_next(request)

# Error Handling Middleware
async def ExceptionMiddleware(request: Request, call_next):
    try:
        return await call_next(request)
    except Exception as e:
        return JSONResponse(
            status_code=500,
            content={"message": "An internal server error occurred."}
        )
