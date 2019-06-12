from django.shortcuts import render

# Create your views here.

from home.models import CustomText, HomePage


def home(request):
    packages = [
	{'name':'eth-utils', 'url': 'http://pypi.python.org/pypi/eth-utils/0.7.4'},
	{'name':'django-allauth', 'url': 'http://pypi.python.org/pypi/django-allauth/0.34.0'},
	{'name':'django-bootstrap4', 'url': 'http://pypi.python.org/pypi/django-bootstrap4/0.0.5'},
    ]
    context = {
        'customtext': CustomText.objects.first(),
        'homepage': HomePage.objects.first(),
        'packages': packages
    }
    return render(request, 'home/index.html', context)
