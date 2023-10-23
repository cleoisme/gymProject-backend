from django.http import HttpResponse


# Create your views here.
def check_project(request):
    return HttpResponse("This is the Notification Sender Project!")
