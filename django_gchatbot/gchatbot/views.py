from django.shortcuts import render

# Create your views here.
from django.http import JsonResponse, HttpResponse


def on_event(request):
    """Handles an event from Google Chat."""
    event = {}
    event['type'] = "MESSAGE"
    event['message'] = {'text': "Raj"}
    if event['type'] == 'ADDED_TO_SPACE':
        text = 'Thanks for adding me to "%s"!' % (
            event['space']['displayName'] if event['space']['displayName'] else 'this chat')
    elif event['type'] == 'MESSAGE':
        text = 'You said: `%s`' % event['message']['text']
    else:
        return {}
    return JsonResponse({'text': text})