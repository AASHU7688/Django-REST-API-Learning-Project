from django.http import HttpResponse,JsonResponse
def home_page(request):
    print("Home page request received")
    friends=["Alice", "Bob", "Charlie"]
    return JsonResponse(friends, safe=False)