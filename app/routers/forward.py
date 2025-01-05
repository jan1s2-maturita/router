from fastapi.responses import HTMLResponse, JSONResponse
import httpx
from fastapi import APIRouter, HTTPException, Header, Request, Cookie, Response
import json
from ..dependencies import service_map

router = APIRouter()

@router.api_route("/{full_path:path}", methods=["GET", "POST", "PUT", "DELETE"])
async def forward_request(request: Request, full_path: str):
    # Extract the first part of the path (like /auth, /users, /orders)
    path_parts = full_path.split('/')
    path_parts = path_parts[1:]
    if len(path_parts) < 1 or f"/{path_parts[0]}" not in service_map:
        raise HTTPException(status_code=404, detail=f"Service not found - {path_parts}")

    service_url = service_map[f"/{path_parts[0]}"]
    service_path = "/".join(path_parts[1:])
    
    # Forward the request to the appropriate service
    try:
        async with httpx.AsyncClient() as client:
            # Construct the full URL to the target microservice
            url = f"{service_url}/{service_path}"
            print(url)
            print(request.cookies.get("token"))
            headers = request.scope["headers"]
            print(headers)
            if all(t[0] != b"x-token" for t in headers):
                headers.append((b"x-token", request.cookies.get("token", b"")))

            # Forward the request with the same method and body
            response = await client.request(
                method=request.method,
                url=url,
                params=request.query_params,
                headers=headers,
                content=await request.body()
            )
            response_type = 'json'
            # if 'application/json' in response.headers['content-type']:
                # return JSONResponse(content=json.loads(response.content.decode()), status_code=response.status_code)
            # else:
                # return HTMLResponse(content=response.content.decode(), status_code=response.status_code)
            return Response(content=response.content, status_code=response.status_code, headers=response.headers, media_type=response.headers['content-type'])
            
    except httpx.HTTPError as e:
        raise HTTPException(status_code=500, detail=str(e))

