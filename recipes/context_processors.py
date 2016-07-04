import os

def app_mode(request):
    return {
        'app_mode': os.environ.get('APP_MODE', 'production')
    }
