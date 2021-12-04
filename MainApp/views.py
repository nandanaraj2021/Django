from django.shortcuts import render

# Create your views here.
def index(request):
    #get: requesting information from the database
    #post: positing information to the database
    return render(request, 'MainApp/index.html')
