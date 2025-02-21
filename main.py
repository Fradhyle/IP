from js import Headers, Response


def on_fetch(request):
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
    headers = Headers.new({"Content-Type": "text/html;charset=UTF-8"}.items())
    return Response(data, headers=headers)
