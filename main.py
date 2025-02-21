from js import Headers, Response


def on_fetch(request):
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
        }
    )
    return Response.new(data, headers=headers)
