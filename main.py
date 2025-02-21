from fastapi import FastAPI, Request, Response

app = FastAPI()


@app.get("/")
def root(request: Request):
    data = f"""<!DOCTYPE html>
    <html lang="ko">
        <head>
            <meta charset="UTF-8" />
            <meta name="viewport" content="width=device-width, initial-scale=1.0" />
            <title>IP</title>
        </head>
        
        <body>
            <span id="ip">{request.client.host}</span>
        </body>
    </html>"""
    return Response(content=data, media_type="text/html")
