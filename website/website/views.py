from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def mainpage(request):

    #return render(request, "index.html")
    return HttpResponse("""<h1>This is the main page!</h1>""")
    #                     <br>
    #                     <a href="http://127.0.0.1:8000/myfirstapp/">pokedex</a>
    #                     <br>
    #                     <a href="http://127.0.0.1:8000/admin/">admin</a>
    # """)
