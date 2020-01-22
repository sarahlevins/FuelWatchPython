from django.http import HttpResponse

def index(request):
    num = 1
    return HttpResponse('<p>My favourite number is {}</p>'.format(num))