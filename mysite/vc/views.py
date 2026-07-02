import json
from django.http import JsonResponse, HttpResponseBadRequest
from django.views.decorators.csrf import csrf_exempt

def get_question(request):
    """
    GET /quiz/question
    Returns a predefined quiz question as JSON.
    """
    if request.method != 'GET':
        return HttpResponseBadRequest("Only GET method is allowed on this endpoint.")
        
    data = {
        "id": 1,
        "text": "ประเทศไทยมีกี่จังหวัด",
        "choices": [50, 68, 72, 77]
    }
    return JsonResponse(data, json_dumps_params={'ensure_ascii': False})

@csrf_exempt
def create_question(request):
    """
    POST /quiz/question/create
    Accepts and returns JSON representing a new quiz question.
    """
    if request.method != 'POST':
        return HttpResponseBadRequest("Only POST method is allowed on this endpoint.")
        
    try:
        # Load and parse JSON body
        if request.body:
            data = json.loads(request.body)
        else:
            # Fallback if no body is provided (for demo/default purposes)
            data = {
                "id": 9,
                "text": "ภาษาโปรแกรมใดได้รับความนิยมสูงสุดในวิทยาการข้อมูล",
                "choices": ["C", "C++", "C#", "Python", "R", "Julia"]
            }
            
        # Ensure json_dumps_params ensure_ascii=False to display Thai characters correctly
        return JsonResponse(data, json_dumps_params={'ensure_ascii': False})
    except json.JSONDecodeError:
        return HttpResponseBadRequest("Invalid JSON body.")
