from urllib.parse import urlparse

from js import Headers, Response


async def on_fetch(request):
    url = urlparse(request.url)
    ip_address = request.headers.get("CF-Connecting-IP")
    html_template = """<!DOCTYPE html>
    <html lang="ko">
        <head>
            <meta charset="UTF-8" />
            <meta name="viewport" content="width=device-width, initial-scale=1.0" />
            <title>IP</title>
        </head>
        
        <body>
            <span id="ip">{ip_address}</span>
        </body>
    </html>"""
    data = html_template.format(ip_address=ip_address)
    headers = Headers.new(
        {
            "Content-Type": "text/html;charset=UTF-8",
        }.items()
    )

    if url.path == "/favicon.ico":
        return Response.new("")

    return Response.new(data, headers=headers)
