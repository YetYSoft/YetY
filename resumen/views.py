from django.shortcuts import render

# Create your views here.







from resumen.models import Blog
def ver_resumen(request):
  
    return render  (request,"resumen.html")


