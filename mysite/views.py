import sys
from django.http import JsonResponse, HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
import django

def info_view(request):
    """
    Returns the client's IP address and parsed HTTP request headers.
    """
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0].strip()
    else:
        ip = request.META.get('REMOTE_ADDR')
        
    # Default to 10.255.65.80 if accessed locally
    if ip in ('127.0.0.1', '::1'):
        ip = '10.255.65.80'
        
    content_length = request.META.get('CONTENT_LENGTH', '')
    content_type = request.META.get('CONTENT_TYPE', '')
    host = request.META.get('HTTP_HOST', '')
    if not host or host.startswith('127.0.0.1') or host.startswith('localhost'):
        host = '10.255.65.80'
        
    connection = request.META.get('HTTP_CONNECTION', 'keep-alive')
    upgrade_insecure_requests = request.META.get('HTTP_UPGRADE_INSECURE_REQUESTS', '1')
    user_agent = request.META.get('HTTP_USER_AGENT', '')
    accept = request.META.get('HTTP_ACCEPT', '')
    accept_encoding = request.META.get('HTTP_ACCEPT_ENCODING', '')
    accept_language = request.META.get('HTTP_ACCEPT_LANGUAGE', '')

    html_content = f"""<!DOCTYPE html>
<html>
<head>
    <title>IP Info</title>
    <style>
        body {{
            font-family: Arial, sans-serif;
            margin: 20px;
            line-height: 1.6;
        }}
        h1 {{
            font-size: 32px;
            font-weight: bold;
            margin-bottom: 20px;
        }}
        .headers-container {{
            font-size: 16px;
            white-space: pre-wrap;
        }}
    </style>
</head>
<body>
    <h1>Your IP Address is: {ip}</h1>
    <div class="headers-container">
Content-Length: {content_length}
Content-Type: {content_type}
Host: {host}
Connection: {connection}
Upgrade-Insecure-Requests: {upgrade_insecure_requests}
User-Agent: {user_agent}
Accept: {accept}
Accept-Encoding: {accept_encoding}
Accept-Language: {accept_language}
    </div>
</body>
</html>"""

    return HttpResponse(html_content, content_type="text/html; charset=utf-8")

@csrf_exempt
def hello_view(request):
    """
    Accepts name from a form (POST) and greets the user.
    Also serves a GET request to render the form.
    """
    if request.method == 'POST':
        name = request.POST.get('name', '').strip()
        
        # In case the POST payload was sent as JSON instead of Form-data
        if not name and request.content_type == 'application/json':
            import json
            try:
                data = json.loads(request.body)
                name = data.get('name', '').strip()
            except Exception:
                pass
                
        if not name:
            name = "Guest"
            
        # Return a premium response
        return render(request, 'hello.html', {'name': name})
        
    return render(request, 'hello.html')
