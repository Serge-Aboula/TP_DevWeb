from django.http import HttpResponse


def welcome(request):
    return HttpResponse('''\
    <!DOCTYPE html>\
    <html lang="fr">\
    <head>\
        <meta charset="UTF-8">\
        <meta name="viewport" content="width=device-width, initial-scale=1.0">\
        <title>Trombinoscoop</title>\
    </head>\
    <body>\
        <p>Bienvenue sur Trombinoscoop !\
    </body>\
    </html>                    ''')