from django.http import HttpResponse
import json
import time
from datetime import datetime, timezone

def index(request):
    current_time = time.time()
    iso_datetime = datetime.fromtimestamp(current_time, tz=timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ')
    data = {
        "email": "oluwatimileyin962@gmail.com".title(),
        "current_datetime": iso_datetime,
        "github_url": "https://github.com/Thimmy962/HNG"
    }
    response = HttpResponse(
        json.dumps(data, indent=4),  # Pretty-print with 4 spaces
        content_type="application/json"
     )
    return response

