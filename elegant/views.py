from django.shortcuts import render
# from django.utils import timezone
# from oauth2client.contrib import appengine

# from .models import Procedure
# import calendar



def client_list(request):
    # c = calendar.Calendar()
    return render(request, 'elegant/client_list.html')


# decorator = appengine.OAuth2DecoratorFromClientSecrets(
#     'client_secrets.json',
#     scope='https://www.googleapis.com/auth/calendar')
# class MainHandler(webapp.RequestHandler):
#    @decorator.oauth_required
#    def get(self):
#      http = decorator.http()
#      request = service.events().list(calendarId='primary')
