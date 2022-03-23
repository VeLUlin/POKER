from django.shortcuts import render
from .forms import Calculate

# Create your views here.
def index(request):
	params = {
		'title': '偏差値POKER',
		'forms': Calculate(),
		'answer': 'いくらの収支になるかな...'
	}
	if request.method == 'POST':
		result = int(request.POST['balance']) / int(request.POST['compression']) / 60
		if result < 0:
			params['answer'] = str(result) + '円 Lost...'
			params['forms'] = Calculate(request.POST)
		elif result >= 0:
			params['answer'] = str(result) + '円 Get!!!'
			params['forms'] = Calculate(request.POST)
	return render(request, 'score/index.html', params)