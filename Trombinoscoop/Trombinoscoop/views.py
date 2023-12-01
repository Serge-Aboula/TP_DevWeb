from datetime import datetime
from django.shortcuts import render

def welcome(request):
    return render(request, 'welcome.html',
                  {'current_date_time': datetime.now()})
