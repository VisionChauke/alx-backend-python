from django.views.decorators.cache import cache_page
from django.shortcuts import render
from messaging.models import Message
from django.contrib.auth.decorators import login_required
@login_required
@cache_page(60 * 15)  # Cache the view for 15 minutes
def my_view(request):
	# Your view logic here
	return render(request, 'template.html', {})