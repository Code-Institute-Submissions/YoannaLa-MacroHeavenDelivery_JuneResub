from django.shortcuts import render

# Create your views here.
def get_menu_list(request):
    return render(request, 'list/menu_list.html')


