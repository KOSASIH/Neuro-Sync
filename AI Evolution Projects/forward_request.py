async def forward_request(request: Request):
    try:
        async with httpx.AsyncClient() as client:
            target_url = f"{TARGET_SERVER_HOST}{request.url.path}"
            method = request.method
            headers = dict(request.headers)
            if "host" in headers:
                del headers["host"]
            if request.method in ["POST", "PUT", "PATCH"]:
                request_body = await request.json()
            else:
                request_body = None
            response = await client.request(
                method,
                target_url,
                headers=headers,
                json=request_body,
                params=request.query_params,
            )
            return JSONResponse(
                response.json(),
                status_code=response.status_code,
                headers=dict(response.headers),
            )
    except httpx.HTTPError as e:
        return JSONResponse(
            {"error": str(e)},
            status_code=e.response.status_code,
            headers=dict(e.response.headers),
        )
